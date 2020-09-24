# Speedrun Fast Go Go

[![build status](https://git.cssnr.com/shane/speedrun-web/badges/master/build.svg)](https://git.cssnr.com/shane/speedrun-web/commits/master) [![coverage report](https://git.cssnr.com/shane/speedrun-web/badges/master/coverage.svg)](https://git.cssnr.com/shane/speedrun-web/commits/master)

This is a basic Django Framework for a Twitch that goes fast...

# Features

### Twitch Oauth

Twitch Oauth managed from Django admin.

### Frameworks

- Django (2.1.5) https://www.djangoproject.com/
- Bootstrap (4.2.1) http://getbootstrap.com/
- Font Awesome (5.6.3) http://fontawesome.io/
- JQuery (3.3.1) https://jquery.com/

# Development

### Deployment

To deploy this project on the development server:

```
git clone https://git.cssnr.com/shane/speedrun-web.git
cd shane/speedrun-web
pyvenv venv
source venv/bin/activate
python -m pip install -r requirements.txt
cp settings.ini.example settings.ini
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata site-fixtures.json
python manage.py runserver 0.0.0.0:8000
```

*Note: Make sure to update the `settings.ini` with the necessary details...*

### Copying This Project

To clone a clean copy of this project int your repository:

```
git clone https://git.cssnr.com/shane/speedrun-web.git
cd django-twitch-basic
rm -rf .git
git init
git remote add origin https://github.com/your-org/your-repo.git
git push -u origin master
```

*Note: make sure to replace `your-org/your-repo.git` with your actual repository location...*
