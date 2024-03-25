start:
	docker run -d -p 5000:3000 -v ./server/app:/app/app --rm --name flask_app flask_app:latest
stop:
	docker stop flask_app

build:
	docker build -t flask_app .