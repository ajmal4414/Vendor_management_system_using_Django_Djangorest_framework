
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder
from django.db import models
from django.db.models import Avg, Count

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def update_vendor_performance(sender, instance, **kwargs):
    vendor = instance.vendor

    # On-Time Delivery Rate Calculation
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date'))
    vendor.on_time_delivery_rate = (on_time_deliveries.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0.0

    # Quality Rating Average Calculation
    completed_pos_with_rating = completed_pos.exclude(quality_rating__isnull=True)
    vendor.quality_rating_avg = completed_pos_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

    # Average Response Time Calculation
    acknowledged_pos = completed_pos.exclude(acknowledgment_date__isnull=True)
    response_times = (acknowledged_pos.values('acknowledgment_date', 'issue_date')
                      .annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date')))
    avg_response_time = response_times.aggregate(Avg('response_time'))['response_time__avg']
    vendor.average_response_time = avg_response_time.total_seconds() if avg_response_time else 0.0

    # Fulfilment Rate Calculation
    successful_pos = completed_pos.filter(status='completed', quality_rating__gte=0)
    vendor.fulfillment_rate = (successful_pos.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0.0

    vendor.save()
