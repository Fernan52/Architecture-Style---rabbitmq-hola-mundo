import pika

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='¡Hola desde RabbitMQ!')

    print(" [x] Enviado '¡Hola desde RabbitMQ!'")
    connection.close()

if __name__ == '__main__':
    send_message()
