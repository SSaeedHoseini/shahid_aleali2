file := production.yml

up:
	docker-compose -f ${file} up --build -d

down:
	docker-compose -f ${file} down

down-v:
	docker-compose -f ${file} down -v

restart:
	docker-compose -f ${file} restart

migrate:
	docker-compose -f ${file} run --rm django python manage.py migrate

makemigrations:
	docker-compose -f ${file} run --rm django python manage.py makemigrations

createsuperuser:
	docker-compose -f ${file} run --rm django python manage.py createsuperuser

collectstatic:
	docker-compose -f ${file} run --rm django python manage.py collectstatic --clear

load-theme:
	docker-compose -f ${file} run --rm django python manage.py loaddata admin_interface_theme_django.json
	docker-compose -f ${file} run --rm django python manage.py loaddata admin_interface_theme_bootstrap.json
	docker-compose -f ${file} run --rm django python manage.py loaddata admin_interface_theme_foundation.json
	docker-compose -f ${file} run --rm django python manage.py loaddata admin_interface_theme_uswds.json