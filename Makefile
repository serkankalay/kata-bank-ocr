.PHONY: clean format migrate init

init:
	pip install -U -r requirements.txt

format:
	black ./ 
	isort -rc ./

# run-api:
# 	python api.py