docker_nginx_build:
	docker build -t vespapp/nginx dockerfile_nginx/
docker_nginx_push:
	docker push vespapp/nginx
docker_build:
	docker build -t vespapp/vespapp-web .
docker_push:
	docker push vespapp/vespapp-web
devel:
	docker-compose run --rm --service-ports dev
gulp-watch:
	docker-compose run --rm -T gulp watch
