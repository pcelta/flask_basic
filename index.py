from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/provisioner.json/activate',methods=['GET'])
def provisioner():
    print request.args
    json = request.args.get('json')
    return 'Provisioner...%s' % json

@app.route('/')
def brincando():
	from src.pedrin.carro import Carro
	car = Carro()
	return ''

if __name__ == '__main__':
    app.debug = True
    app.run()