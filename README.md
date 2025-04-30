# Courier-Delivery-Service-API

This is a RESTful API built with Django and Django REST Framework for managing courier deliveries. It supports role-based user management, parcel tracking, and delivery proof image uploads.

## 🚀 Features
- JWT Authentication (via SimpleJWT)
- Role-based access control (`admin`, `courier`, `customer`)
- CRUD operations for:
  - Users
  - Parcels
  - Delivery proofs
- Swagger UI for API documentation
- PostgreSQL database support
- File uploads for delivery proof

## 📂 Project Structure

courierAPI/ ├── courierAPI/ ├── deliveries/ ├── manage.py ├── .env

## 🔧 Installation

### 1. Clone the Repository

git clone https://github.com/anageguchadze/Courier-Delivery-Service-API.git

2. Create and Activate Virtual Environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

3. Install Requirements
pip install -r requirements.txt

4. Set Environment Variables
Create a .env file in the root directory:
env

SECRET_KEY=your-secret-key
DATABASE_NAME=your-db-name
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
DATABASE_PORT=5432

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

7. Create Superuser (Optional)
python manage.py createsuperuser

8. Run the Server
python manage.py runserver

🔐 Authentication
This project uses JWT Authentication.

Obtain Token:
POST /api/token/
{
  "username": "yourusername",
  "password": "yourpassword"
}

Refresh Token:
POST /api/token/refresh/

Verify Token:
POST /api/token/verify/
Include the token in the Authorization header for protected endpoints:
Authorization: Bearer your_token_here

🧾 API Endpoints
Method	Endpoint	Description
GET	/api/users/	List users
POST	/api/users/	Create user
GET	/api/parcels/	List parcels
POST	/api/parcels/	Create parcel
GET	/api/delivery_proofs/	List delivery proofs
POST	/api/delivery_proofs/	Upload delivery proof
GET	/swagger/	Swagger API Documentation

📸 Image Upload
Delivery proof images are stored under media/delivery_proofs/.

Make sure you configure your MEDIA_URL and MEDIA_ROOT in production.

🛠 Tech Stack
Python

Django

Django REST Framework

PostgreSQL

SimpleJWT

drf-yasg (Swagger Docs)

🧼 To-Do
Add permissions based on user roles

Add pagination and filtering

Add tests

Improve error handling and validations

📄 License
This project is open source and available under the MIT License.
