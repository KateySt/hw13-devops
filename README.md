RabbitMQ Consumer and Producer Documentation
===========================================

This is a simple RabbitMQ example with a consumer and a producer.

Consumer (receive.py)
---------------------
The `receive.py` script connects to a RabbitMQ broker, declares a queue named "my_first_queue",
and waits for messages to arrive in the queue. When a message is received, it prints the message to the console.

Producer (send.py)
-------------------
The `send.py` script also connects to the RabbitMQ broker, declares the same queue "my_first_queue",
and sends a message "My first message" to the queue.

Running the Consumer (receive.py)
---------------------------------
1. Make sure RabbitMQ is installed and running on your localhost.
2. Run the `receive.py` script. It will listen for messages in the "my_first_queue" and print them.

```plaintext
[*] I`m waiting ... To you ...
```

Running the Producer (send.py)
-------------------------------
1. Make sure RabbitMQ is installed and running on your localhost.
2. Run the `send.py` script. It will send the message "My first message" to the "my_first_queue" queue.

```plaintext
[x] Sent 'My first massage'
```

After running send.py in the console of the receive.py file

```plaintext
[*] I'm waiting ... To you ...
[x] Message b'My first message'
```

Note: To stop the consumer, you can use `CTRL+C`.

This is a basic example of using RabbitMQ with Python's Pika library.
