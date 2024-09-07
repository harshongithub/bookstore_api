# Bookstore API

This project is a RESTful API for managing a book inventory.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)

## Features

- Manage book inventory (add, update, delete books)
- User authentication and authorization
- Search functionality for books by ID

## Prerequisites

- Python 3.7+
- Django 3.2+
- Django REST Framework 3.12+

## Installation

1. **Clone the Repository** or **Download the Zip**:

   ```bash
   git clone https://github.com/harshongithub/bookstore_api.git
   cd bookstore_api
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv venv 
   ```

   - **On Windows**: `venv\Scripts\activate`
   - **On macOS/Linux**: `source venv/bin/activate`

3. **Install the Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```
    ```bash
   python manage.py makemigrations
   ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

## Usage

To run the development server:

```bash
python manage.py runserver
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **`/api/books/`**: List all books or create a new book (Authentication required for creating a new book)
- **`/api/books/<id>/`**: Retrieve, update, or delete a specific book (Authentication required for update and delete)
- **`/api/login/`**: To log in
- **`/api/register/`**: To register as a new user
- **`/api/token/refresh/`**: To get a new access token
- **`/api/admin/`**: To access the admin panel

For detailed documentation of the API endpoints, visit [Postman Documentation](https://documenter.getpostman.com/view/38144718/2sAXjRV9E1).

