# Mini E-Commerce Backend

Full-stack Django + DRF + PostgreSQL backend for a small e-commerce platform.

## Tech Stack
- Python + Django 5.x
- Django REST Framework (DRF)
- PostgreSQL database
- Git + GitHub

## Features
- Product & Category models with admin panel
- REST API endpoint: `/api/products/` (guest accessible)
- CORS enabled for Flutter web
- Order model + basic creation endpoint (`/api/orders/create/`)
- Guest order support

## Setup & Run (local)

1. Clone the repo
2. Create virtual environment:

python -m venv venv
source venv/Scripts/activate   # Windows
text3. Install dependencies:
pip install -r requirements.txt
text(or `pip install django djangorestframework psycopg2-binary django-cors-headers`)
4. Apply migrations & create superuser:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
text5. Run server:
python manage.py runserver
textAPI: http://127.0.0.1:8000/api/products/  
Admin: http://127.0.0.1:8000/admin/