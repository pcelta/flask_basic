from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from src.validators.json_validator import RequestValidator
from src.services.provisioner import Provisioner

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    
    from src.builders.factory_builder import FactoryBuilder
    factory = FactoryBuilder('interpartner')
    builder = factory.create('activate')
   


    return 'Running...'

@app.route('/provisioner.json/activate',methods=['POST'])
def provisioner():
    json = request.data
    validator = RequestValidator()
    if (validator.validate(json)) :
        provisioner = Provisioner()
        return provisioner.activate(json)

    return 'INVALID JSON'



if __name__ == '__main__':
    app.debug = True
    app.run()
