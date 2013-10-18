import pika 
from configs.loader import Loader

def send(queue_name, str_json):
    settings = Loader.get_by_main_key('rabbitmq')

    user = settings['user']
    password = settings['password']
    host = settings['host']

    queue = 'provisioning-%s' % queue_name

    connection = pika.BlockingConnection(pika.ConnectionParameters(
           host))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=str_json
    )
    connection.close()

def worker(queue_name):

    def callback(ch, method, properties, body):
        print "%s" % (body)

    settings = Loader.get_by_main_key('rabbitmq')

    user = settings['user']
    password = settings['password']
    host = settings['host']

    queue = 'provisioning-%s' % queue_name

    connection = pika.BlockingConnection(pika.ConnectionParameters(
               host))
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    channel.basic_consume(callback,
                          queue=queue,
                          no_ack=True)

    channel.start_consuming()