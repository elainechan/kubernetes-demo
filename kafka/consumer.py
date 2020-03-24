import msgpack
from kafka import KafkaConsumer

topic_name = 'next-containers'
consumer = KafkaConsumer(topic_name)
for packet in consumer:
    value = packet.value
    message = msgpack.loads(value)

    image_name = message['imageName']
    command_text = message['commandText']

