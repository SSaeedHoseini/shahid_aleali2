file := local.yml

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