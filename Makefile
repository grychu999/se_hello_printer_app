.PHONY: test


deps:
	sudo pip install -r requirements.txt; \
	sudo pip install -r test_requirements.txt


lint:
	sudo flake8 hello_world test


test:
	PYTHONPATH=. py.test  --verbose -s


run:
	python main.py
