dep-install:
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt

config:
	cp -vf `pwd`/configs/config.py.example `pwd`/configs/config.py
	mkdir -p `pwd`/data/logs
