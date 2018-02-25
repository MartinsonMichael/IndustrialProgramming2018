#!/usr/bin/env python
import pika
import time

if __name__ == "__main__":

	print("Start recieve...")
	print()

	time.sleep(20)

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue'))
	channel = connection.channel()

	channel.queue_declare(queue='hello_2')

	def callback(ch, method, properties, body):
	    print(" [x] Received :'%r'" % body, flush=True)
	

	channel.basic_consume(callback,
		              queue='hello_2',
		              no_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
