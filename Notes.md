## Django (Web Framework)

### Create Virtual Environment

- **Using venv**:
  ```bash
  py -m venv .venv
  ```
- **Using pip**:
  ```bash
  pip install uv
  uv venv
  ```

#### Activate/Deactivate Virtual Environment
- **Activate**:
  ```bash
  .venv\Scripts\activate
  ```
- **Deactivate**:
  ```bash
  deactivate
  ```

### Install Django
- **Using uv**:
  ```bash
  uv pip install Django
  ```

### Start a Django Project
```bash
django-admin startproject projectname
```

### Run the Server
```bash
python manage.py runserver
# Or to run on a specific port
python manage.py runserver 8001
```

### Folder Structure
- **Root level**
- **Project level**
- **App level**

### Application Flow
```
user -> req -> urls.py -> views.py -> res
```

### Templating Engine
- **Jinja (Django Templating Engine)**

### Create an App
```bash
python manage.py startapp appname
```

### Tailwind Integration

- **Install Tailwind**:
  ```bash
  uv pip install django-tailwind
  uv pip install 'django-tailwind[reload]'
  ```

- **Alternative installation**:
  ```bash
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip
  pip install 'django-tailwind[reload]'
  ```

- **Add Tailwind to App**:
  ```bash
  uv pip install cookiecutter
  python manage.py tailwind init
  ```

### Add Theme to App
```python
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

```bash
python manage.py tailwind install
```

### Modify `layout.html`
- Custom modifications as per your requirement.

### Start Tailwind
```bash
python manage.py tailwind start
```

### Add `django_browser_reload` to App

- **Add to Middleware**:
  ```python
  django_browser_reload.middleware.BrowserReloadMiddleware
  ```

- **Add to urls.py**:
  ```python
  path("__reload__/", include("django_browser_reload.urls"))
  ```

### Handle Migrations
```bash
python manage.py migrate
```

### Run the Server
```bash
python manage.py runserver
```

### Create Super User
```bash
python manage.py createsuperuser
```

### Change User Password
```bash
python manage.py changepassword <user_name>
```

### Handle Model
- **Install Pillow**:
  ```bash
  python -m pip install pillow
  ```

- **Add to settings.py**:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = 'path_to_media_root'
  ```

- **Add to urls.py**:
  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

### Migrations
- **Create Migrations**:
  ```bash
  python manage.py makemigrations m01
  ```

- **Apply Migrations**:
  ```bash
  python manage.py migrate
  ```

### Modify admin.py
- Custom modifications as per your requirement.

### List All Database Objects to Views
- Custom modifications as per your requirement.

### Modify Template (e.g., m01)
- Custom modifications as per your requirement.

### Whenever Models Change
```bash
python manage.py makemigrations m01
python manage.py migrate
```
