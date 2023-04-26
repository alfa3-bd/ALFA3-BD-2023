run:
	pyhthon manage.py runserver

create_mongodb:
	docker run -d -p 27017:27017 --name alfa3bd-mongo mongo:latest

start_mongodb:
	docker start alfa3bd-mongo

configure: clean
	python manage.py makemigrations escola
	python manage.py migrate
	python manage.py createsuperuser --email admin@logistica.local --username admin

clean: 
	rm -rf ./escola/migrations
	# rm -f db.sqlite3
	