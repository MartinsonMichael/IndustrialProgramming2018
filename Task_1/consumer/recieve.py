#!/usr/bin/env python
import pika
import time
import psycopg2

if __name__ == "__main__":

	print("Start recieve...")
	print()

	time.sleep(20)

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue'))
	channel = connection.channel()
	channel.queue_declare(queue='hello_2')


	db_conn = psycopg2.connect(dbname='postgres', user='postgres', host='db', password='q12q', port='5432')
	cursor = db_conn.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS strings (str CHAR(255))")
	db_conn.commit()

	def callback(ch, method, properties, body):
	    s = str(body, 'utf-8')
	    print(" [x] Received %r" % s, flush=True)
	    cursor.execute("INSERT INTO strings (str) VALUES (\'{}\')".format(s))
	    db_conn.commit()
	

	channel.basic_consume(callback,
		              queue='hello_2',
		              no_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
