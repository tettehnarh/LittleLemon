# Description

Meta Backend Developer Capstone Project
<br> <br>

# Project Structure

The project consists of two apps: api and restaurant. The api app serves the project's API endpoints, while the restaurant app serves its frontend.
<br> <br>

# Installation

Activate the virtual environment

```bash
pipenv shell
```

Install the dependencies

```bash
pipenv install
```

<br>

# Setup

Please ensure to update any system-specific details, such as the port or IP address, to match your own configuration if they differ from the ones provided below.

Default database settings are

```jsx
DATABASES = {
  default: {
    ENGINE: "django.db.backends.mysql",
    NAME: "littlelemon",
    HOST: "localhost",
    PORT: "3307",
    USER: "root",
    PASSWORD: "root_password",
    OPTIONS: {
      init_command: "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  },
};
```

Apply the migrations

```bash
python manage.py migrate
```

<br>

# API Endpoints

In Insomnia, add under Bearer tab. Under Prefix enter "Token"
<br>

### Endpoints for `api` app

```bash
http://127.0.0.1:8000/api/menu/
http://127.0.0.1:8000/api/menu/1/
http://127.0.0.1:8000/api/booking/
http://127.0.0.1:8000/api/booking/1/
```

### Endpoints for `djoser` app (To setup user and auth)

```bash
http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/token/login/
```

# Testing

Run the tests

```jsx
python manage.py test
```

<br>

It should output something similar to this

```bash
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
----------------------------------------------------------------------
Ran 2 tests in 0.209s

OK
Destroying test database for alias 'default'...
```
