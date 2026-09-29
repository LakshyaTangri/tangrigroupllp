.PHONY: validate fetch-eve-amd64

validate:
	python3 -m pip install -r manifests/requirements.txt
	python3 manifests/validate.py

fetch-eve-amd64:
	bash eve-images/fetch-amd64-lts.sh
