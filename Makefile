ENV_NAME?=env
ENV_ACTIVATE=. $(ENV_NAME)/bin/activate
PYTHON=${ENV_NAME}/bin/python3

all:
	- python3 -m venv env
	- $(ENV_ACTIVATE)
	- ${PYTHON} -m pip install -r requirements.txt
	- sudo apt-get install rabbitmq-server
	- docker run -d -p 5672:5672 rabbitmq
	- docker run -d -p 6379:6379 redis

celery:
	- celery -A tasks worker --loglevel=INFO

containers:
	- docker run -d -p 5672:5672 rabbitmq
	- docker run -d -p 6379:6379 redis