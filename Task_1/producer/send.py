#!/usr/bin/env python3
import pika
import time

if __name__ == "__main__":

	print("Start sending...")

	print("Type message to send (exit - to exit):\n")

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue'))
	channel = connection.channel()
	channel.queue_declare(queue='hello_2')

	while True:
		s = input()
		if s == 'exit':
			break
		channel.basic_publish(exchange='',
				      routing_key='hello_2',
				      body=s)

		print(" [x] Sent '", s, "'", sep='', end='\n')

	print('[x] Close connection...')
	connection.close()
