dep-install:
	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
