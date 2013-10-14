dep-install:
	sudo apt-get install python-virtualenv
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt

configs:
	cp -vf `pwd`/configs/config.py.example `pwd`/configs/config.py
