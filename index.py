from flask import Flask, request
from src.views.provisioning import Provisioning
from src.validators.json_validator import JsonValidator

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'TNT-Provisioning 2.0 Running...'

@app.route('/activate',methods=['POST'])
def activate():
    json = request.data
    provisioning = Provisioning.create()
    return provisioning.activate(json)

@app.route('/upgrade',methods=['PUT'])
def upgrade():
    json = request.data
    provisioning = Provisioning.create()
    return provisioning.upgrade(json)   

@app.route('/downgrade',methods=['PUT'])
def downgrade():
    json = request.data
    provisioning = Provisioning.create()
    return provisioning.downgrade(json)       

@app.route('/cancel', methods=['PUT'])
def cancel():
    json = request.data
    return 'Not Implemented'

if __name__ == '__main__':
    app.debug = True
    app.run()
