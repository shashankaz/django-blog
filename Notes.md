## Django (Web Framework)

### Create Virtual Environment

- **Using py**:
  ```bash
  py -m venv .venv
  ```
- **Using uv**:
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

### Freeze Requirements
```bash
pip freeze > requirements.txt
```

### Install from Requirements
```bash
pip install -r requirements.txt
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
- **Root level**: Contains the virtual environment, `manage.py`, and the project directory.
- **Project level**: Contains settings, URLs, and WSGI/ASGI configuration.
- **App level**: Contains models, views, admin, and app-specific files.

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

### Register the App
- **Add the app to `INSTALLED_APPS` in `settings.py`**:
  ```python
  INSTALLED_APPS = [
      ...,
      'appname',
  ]
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
- **Add to `settings.py`**:
  ```python
  TAILWIND_APP_NAME = 'theme'
  INTERNAL_IPS = ['127.0.0.1']
  NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
  ```

- **Install Tailwind**:
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

- **Add to `settings.py`**:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

- **Add to `urls.py`**:
  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

### Migrations
- **Create Migrations**:
  ```bash
  python manage.py makemigrations appname
  ```

- **Apply Migrations**:
  ```bash
  python manage.py migrate
  ```

### Modify admin.py
- Custom modifications as per your requirement.

### List All Database Objects to Views
- Custom modifications as per your requirement.

### Modify Template
- Custom modifications as per your requirement.

### Whenever Models Change
```bash
python manage.py makemigrations appname
python manage.py migrate
```

### Additional Important Steps

### Install and Configure Static Files
- **Add to `settings.py`**:
  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```

- **Collect Static Files**:
  ```bash
  python manage.py collectstatic
  ```

### Using the Django Shell
```bash
python manage.py shell
```

### Debugging
- **Use Django Debug Toolbar**:
  ```bash
  pip install django-debug-toolbar
  ```

- **Add to `INSTALLED_APPS` and `MIDDLEWARE`**:
  ```python
  INSTALLED_APPS = [
      ...,
      'debug_toolbar',
  ]

  MIDDLEWARE = [
      ...,
      'debug_toolbar.middleware.DebugToolbarMiddleware',
  ]
  ```

- **Add to `urls.py`**:
  ```python
  import debug_toolbar
  from django.conf import settings
  from django.urls import include, path
  
  if settings.DEBUG:
      urlpatterns = [
          path('__debug__/', include(debug_toolbar.urls)),
      ] + urlpatterns
  ```

### Logging
- **Configure Logging in `settings.py`**:
  ```python
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'file': {
              'level': 'DEBUG',
              'class': 'logging.FileHandler',
              'filename': 'debug.log',
          },
      },
      'loggers': {
          'django': {
              'handlers': ['file'],
              'level': 'DEBUG',
              'propagate': True,
          },
      },
  }
  ```
