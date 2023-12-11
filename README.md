# Vendor_management_system_using_Django_Djangorest_framework


# Vendor Management System

This project implements a Vendor Management System using Django and Django REST Framework. It includes three apps: `vendor`, `purchase_order`, and `vendor_history`. The system manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Setup Instructions

 1. Clone the Repository
```bash
git clone https://github.com/ajmal4414/Vendor_management_system_using_Django_Djangorest_framework.git

cd vendor_management_system

Create virtual enviroment

venv\Scripts\activate

Install requirements

pip install -r requirements.txt

Apply migrations

python manage.py makemigrations
python manage.py migrate

Run server

python manage.py runserver



API Endpoints
Vendor App

List/Create Vendors:

List

Endpoint: GET /vendor/api/vendors/

Create

Endpoint: POST /vendor/api/createvendors/

Retrieve/Update/Delete Vendor:

Retrieve

Endpoint: GET /vendor/api/vendors/{vendor_id}/

Update

Endpoint: PUT /vendor/api/vendors/update/{vendor_id}/

Delete

Endpoint: DELETE /vendor/api/vendors/{vendor_id}/delete/


Purchase Order App

List/Create Purchase Orders:

List

Endpoint: GET /purchase_order/api/purchase_orders/

Create

Endpoint: POST /purchase_order/create/purchase_orders/

Retrieve/Update/Delete Purchase Order:

Retrieve

Endpoint: GET /purchase_order/api/purchase_orders/{po_id}/

Update

Endpoint: PUT /purchase_order/purchase_orders/{po_id}/

Delete

Endpoint: DELETE /purchase_order/purchase_orders/{po_id}/delete/


Vendor History App

Retrieve Vendor Perfomance

Endpoint: GET /vendor_history/api/vendors/4/performance/


Create an Account:

Endpoint: POST /vendor/register/

Get Authentication Token

Endpoint: POST /api-token-auth/

Payload: Include the registered username and password

Copy the Token

Once  receive a response from the token endpoint and copy the generated token.

Authorization in Postman

Open Postman and create a new request.

In the request headers, create an Authorization header

Key: Authorization
Value: Token <token>
Replace <token> with the token you obtained.

it can now use this token for making authenticated requests to protected API endpoints.


