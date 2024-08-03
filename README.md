# Chai Store Project

## Overview
The Chai Store is a Django-based web application designed to showcase various types of chai (tea) varieties, allow users to review them, and manage chai stores. This project includes features for managing chai varieties, user reviews, stores, and chai certificates.

## Features
- **Chai Varieties Management**: Add, update, and view different types of chai.
- **User Reviews**: Users can review chai varieties, providing ratings and comments.
- **Store Management**: Manage stores that offer different chai varieties.
- **Chai Certificates**: Manage certificates for chai varieties, including issue and validity dates.

## Installation

### Prerequisites
- Python 3.x
- Django
- Pillow (for image handling)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/shashankaz/django-blog.git
   cd django-blog
   ```

2. Create and activate a virtual environment:
   ```sh
   py -m venv .venv
   source .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser for the admin interface:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

7. Open your web browser and go to `http://127.0.0.1:8000/admin` to access the admin interface.

## Project Structure
```
project01/
├── chai/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── project01/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
└── requirements.txt
```

## URLs

### Main URLs
- `/admin/`: Admin interface.
- `/`: Home page.
- `/about/`: About page.
- `/contact/`: Contact page.
- `/chai/`: Includes URLs from the `chai` app.

### Chai App URLs (`chai/urls.py`)
- `/chai/`: Home page for chai varieties.
- `/chai/<int:chai_id>/`: Detail page for a specific chai variety.
- `/chai/store/`: Page listing all stores.
