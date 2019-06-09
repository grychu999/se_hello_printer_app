.PHONY: test


deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt


lint:
	flake8 hello_world test


test:
	PYTHONPATH=. py.test  --verbose -s


run:
	python main.py


docker_build:
	sudo docker build -t hello-world-printer .


docker_run: docker_build
		docker run \
		--name hello-world-printer-dev \
		-p 5000:5000 \
		-d hello-world-printer

USERNAME=grychu999
TAG=$(USERNAME)/hello_world_printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello_world_printer $(TAG); \
	docker push $(TAG); \
	docker logout;
