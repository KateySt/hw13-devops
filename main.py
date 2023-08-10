import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='my_first_queue')

    def callback(ch, method, properties, body):
        print(f" [x] Massage {body}")

    channel.basic_consume(queue='my_first_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] I`m waiting ... To you ...')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stop')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)