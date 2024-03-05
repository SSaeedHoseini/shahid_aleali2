up:
	docker-compose -f production.yml up --build -d

down:
	docker-compose -f production.yml down

down-v:
	docker-compose -f production.yml down -v

restart:
	docker-compose -f production.yml restart
