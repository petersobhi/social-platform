# social-platform

### Start the project:
1. `docker-compose up` 
2. Database migration: `docker-compose exec server python manage.py migrate`
3. Visit `localhost:8000/swagger` to check the API documentation

### Admin panel:
1. Create super user: `docker-compose exec server python manage.py createsuperuser`
2. Visit `localhost:8000/admin`