.PHONY: clean format migrate init

init:
	pip install -U -r requirements.txt

format:
	black ./ --line-length 79
	isort -rc ./ --line-width 79

# run-api:
# 	python api.py