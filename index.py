from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from src.views.provisioning import Provisioning
from src.validators.json_validator import JsonValidator
from src.services.provisioning import ProvisioningService
from src.builders.factory_builder import FactoryBuilder
from src.adapters.factory_adapter import FactoryAdapter

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'TNT-Provisioning 2.0 Running...'

@app.route('/provisioner.json/activate',methods=['POST'])
def provisioner():
    json = request.data
    provisioning_service = ProvisioningService(FactoryBuilder(), FactoryAdapter())
    provisioning = Provisioning(JsonValidator(), provisioning_service)
    response = provisioning.provision(json)

    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
