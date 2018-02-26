### Industrial Programming 2018


# Task_1

Firts docker image contain producer, second is docker-compose and contain three images: image for rabbitmq, image for data base (I use postgresql), and image for consumer, who read data from container with rabbit and write this data to db.

For first container (we in Task_1 folder):

build : $docker build -t producer ./producer/

run : $docker run -i --network task1_net_123 producer



For second container (we in Task_1 folder):

build : $docker-compose build

run : $docker-compose up
