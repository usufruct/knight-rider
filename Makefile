deps:
	pip install -r requirements.txt

test:
	python -m unittest  discover -s ./tests -v -p "*_test.py"

.PHONY: deps test