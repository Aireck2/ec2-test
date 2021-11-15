# Api Mineria Python

## Installation:
```
~ virtualenv vEnv -p python3.9
~ source vEnv/bin/activate
(vEnv) ~ 
```

## Database:
```
~ brew install postgresql
~ pip install psycopg2
```

## AWS EC2:
```
~ chmod 400 credentials.pem
```

## Deploy:
```
[WITHOUT DOCKER-COMPOSE]
~ docker build -t api-flask:latest .
~ docker run -d -p 80:5000 api-flask
[WITH DOCKER-COMPOSE]
~ docker-compose up -d
```