Bookstore API
This project is a RESTful API for managing a books inventory.

Table of Contents

Features
Prerequisites
Installation
Usage
API Endpoints

Features

Manage book inventory (add, update, delete books)
User authentication and authorization
Search functionality for books by id

Prerequisites

Python 3.7+
Django 3.2+
Django REST Framework 3.12+

Installation

Clone the repository or download the zip:
Copygit clone https://github.com/harshongithub/bookstore_api.git
cd bookstore_api

Create a virtual environment and activate it:
Copypython -m venv venv #if you clone the repo
python -m venv .venv # if downloaded zip

# On Windows, use `venv\Scripts\activate`
# On Mac ,use source venv/bin/activate 

Install the required packages:
Copypip install -r requirements.txt

Apply migrations:
Copypython manage.py migrate

Create a superuser:
Copypython manage.py createsuperuser


Usage

To run the development server:
Copypython manage.py runserver
The API will be available at http://localhost:8000.

API Endpoints

/api/books/: List all books or create a new book (Authentication required for Creating new book)
/api/books/<id>/: Retrieve, update, or delete a specific book (Authentication required for Update and delete)
/api/login/: To login 
/api/register/: To register as a new user
/api/token/refresh/: To get new access token
/api/admin/: to open admin panel

For detailed documentation of the API endpoints, visit [documentation](https://documenter.getpostman.com/view/38144718/2sAXjRV9E1)

