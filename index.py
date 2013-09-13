from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/provisioner.json/activate',methods=['GET', 'POST'])
def provisioner():
	return 'Provisioner...'


if __name__ == '__main__':
    app.run()