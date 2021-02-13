.PHONY: init

init:
	@python3 -m venv venv
	@./venv/bin/python3 -m pip install -U pip
	@./venv/bin/python3 -m pip install -r requirements/requirements_dev.txt
	@./venv/bin/python3 -m pip install -r requirements/requirements.txt
	@echo "Run source venv/bin/activate to activate your environment."

build-image:
	docker build . -f src/Dockerfile -t huggingface-sentiment:latest

run-dev:
	docker run -d -p 5000:5000 --rm huggingface-sentiment
