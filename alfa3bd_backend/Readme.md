# Como rodar

## Banco de Dados
### 1. Configurar o banco de dados
make create_mongodb
ou
docker run -d -p 27017:27017 --name alfa3bd-mongo mongo:latest
### 2. Rodar o banco
Somente da primeira vez é necessário configurar o banco. 
Das próximas vezes pode-se inicializá-lo com:

make start_mongodb
ou
docker start alfa3bd-mongo

## Servidor Django
### 1. Configurar o ambiente
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip  
pip install -r requirements.txt

### 2. Rodar o Servidor django
python manage.py runserver

### 3. Acessar a API
Rota: localhost:8000

Para consumir a api utilize a aplicação do frontend (alfabd3_frontend)

# Referencias do projeto backend
https://www.django-rest-framework.org
https://www.mongodb.com/compatibility/mongodb-and-django
https://sourcery.blog/how-to-build-api-with-django-rest-framework-and-mongodb/
https://www.howtogeek.com/devops/how-to-run-mongodb-in-a-docker-container/
