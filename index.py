from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from src.validators.json_validator import RequestValidator
from src.services.provisioner import Provisioner

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/provisioner.json/activate',methods=['POST'])
def provisioner():
    json = request.data
    validator = RequestValidator()
    if (validator.validate(json)) :
        provisioner = Provisioner()
        provisioner.activate(json)
        return 'VALID JSON'

    return 'INVALID JSON'

@app.route('/')
def brincando():
    from src.pedrin.carro import Carro
    car = Carro()
    return ''

if __name__ == '__main__':
    app.debug = True
    app.run()
