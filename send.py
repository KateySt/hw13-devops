import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_first_queue')

channel.basic_publish(exchange='', routing_key='my_first_queue', body='My first massage')
print(" [x] Sent 'My first massage'")
connection.close()