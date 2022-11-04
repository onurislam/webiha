# Requirements
Django==4.1.3 <br>
psycopg2==2.9.5
```shell
pip install -r requirements.txt
```
# Settings Configration
File Location: webiha/settings.py
## DataBase Config
```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbName',
        'USER': 'dbUser',
        'PASSWORD': 'dbPass',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
```

## Upload IMG Config
```shell
MEDIA_ROOT = os.path.join(BASE_DIR,'static/upload')
```

# Project RUN (VM):
Python VM Activate:
```shell
.\ihaenv\Scripts\activate
```
Django Server RUN
```shell
python .\manage.py runserver
```

# Docker RUN:
```shell
docker run webiha
```
