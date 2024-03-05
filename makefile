up:
	docker-compose -f production.yml up --build -d

down:
	docker-compose -f production.yml down

down-v:
	docker-compose -f production.yml down -v

restart:
	docker-compose -f production.yml restart

migrate:
	docker-compose -f production.yml run --rm django python manage.py migrate

migrate:
	docker-compose -f production.yml run --rm django python manage.py makemigrations

createsuperuser:
	docker-compose -f production.yml run --rm django python manage.py createsuperuser