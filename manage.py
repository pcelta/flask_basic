#!/usr/bin/env python
from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@manager.command
def server():
    from flask import request
    from src.views.provisioning import Provisioning

    @app.route('/', methods=['GET'])
    def index():
        return 'TNT-Provisioning 2.0 Running...'


    @app.route('/activate', methods=['POST'])
    def activate():
        json = request.data
        provisioning = Provisioning.create()
        return provisioning.activate(json)


    @app.route('/upgrade', methods=['PUT'])
    def upgrade():
        json = request.data
        provisioning = Provisioning.create()
        return provisioning.upgrade(json)


    @app.route('/downgrade', methods=['PUT'])
    def downgrade():
        json = request.data
        provisioning = Provisioning.create()
        return provisioning.downgrade(json)


    @app.route('/cancel', methods=['PUT'])
    def cancel():
        json = request.data
        provisioning = Provisioning.create()
        return provisioning.cancel(json)


    @app.route('/reactivate', methods=['PUT'])
    def reactivate():
        json = request.data
        provisioning = Provisioning.create()
        return provisioning.reactivate(json)


    app.debug = True
    app.run()


@manager.command
@manager.option('-q', '--queue', 'queue name')
def worker(queue_name):
    from src.message_queue.manager import worker
    worker(queue_name)


if __name__ == "__main__":
    manager.run()
