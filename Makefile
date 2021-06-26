.PHONY: test

deps:
	pip install -r requirements.txt;\
	pip install -r test_requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

run:
	python3 main.py

lint:
	flake8 hello_world test

docker_build:
	docker build -t hello-world-printer .

docker_run: docker_build
		docker run\
				--name hello-world-printer-dev \
				-p 5000:5000 \
				-d hello-world-printer

USERNAME=danka24
TAG=$(USERNAME)/hello-world-hello_world_printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $$[DOCKER_PASSWORD};\
	docker tag hello-world-printer $(TAG);\
	docker push $(TAG);\
	docker logout;

	test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml  --cov-report term

	test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml --cov-report term --junit-xml=test_results.xml
