# Library APP DRF

## Overview

This is a Django REST framework (DRF) project that provides an API for managing Books and Authors.

## Features

- **Superuser Authentication:**
  - Secure API access using superuser credentials with Basic Auth.

- **Authors:**
  - CRUD operations.
  - Search functionality for listing page.
  - Pagination support for listing page.
  - Detailed view for a specific author.
  
- **Books:**
  - CRUD operations.
  - Automatic generation of book_id based on creation time.
  - Prevent creation of books with the same Book name.
  - Search functionality for listing page.
  - Pagination support for listing page.
  - Detailed view for a specific book.
  
- **Book-Author Mapping:**
  - CRUD operations, with mapping to respective authors.
  - Assign multiple books to one author.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Khailas12/Library-APP-DRF.git
   ```
2. Navigate to the project directory::
   ```bash
   cd Library-APP-DRF
      ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
      ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
5. Install dependencies:
   ```bash
   pip install requirements.txt
   ```

# Connecting to PostgreSQL
This Django project uses PostgreSQL as its database engine. PostgreSQL is a powerful, open-source relational database management system. Connecting Django to PostgreSQL involves configuring the DATABASES setting in the settings.py file.

DATABASES Configuration
In the settings.py file, the DATABASES setting is configured to use the ```django.db.backends.postgresql``` engine for PostgreSQL. The parameters such as NAME, USER, PASSWORD, HOST, and PORT define the connection details:

### Refer this to [Connect PostgreSQL database to Django](https://codinggear.blog/how-to-connect-postgresql-database-to-django/)


Create a file named ```.env``` in the root of your Django project and add your confidential keys:
#### .env
```
NAME=mydatabase
USER=mydatabaseuser
PASSWORD=mypassword
```
### Load Environment Variables
The python-dotenv package is used to load environment variables from the .env file. 
#### settings.py
```
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("NAME"), 
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}
```
---
### or 
### If the ```PostgreSQL``` is not required then please Uncomment the Sqlite Database's code instead in the ```settings.py``` 
---

### 6. Apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

### 7. Create SuperUser:
```
python manage.py createsuperuser
```

### 8. Run the development server:
```
python manage.py runserver
```

---
# Testing with Postman

To test the API endpoints using Postman, follow these steps:

1. Open Postman and create a new request.

2. Set the request method (GET, POST, etc.) based on the endpoint you want to test.

3. Include the API endpoint URL, for example:
   - `http://localhost:8000/books/` for listing books.

4. Go to the "Authorization" tab in Postman.

5. Choose "Basic Auth" as the type of authorization.

6. Enter the superuser credentials:
   - **Username:** your_superuser_username
   - **Password:** your_superuser_password

7. Send the request to test the API endpoint.

**Note:** Superuser credentials are often created during the Django project setup.


# Conclusion

Thank you for exploring the Library APP DRF project! I hope this README provides clear and concise instructions for setting up, configuring, and testing the application. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or contribute to the project.
#### Happy coding!
