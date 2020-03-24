import msgpack
from kafka import KafkaProducer

message = {
    'imageName': 'ubuntu',
    'commandText': 'echo hmm',
}

message_pack = msgpack.dumps(message)

topic_name = 'next-containers'
producer = KafkaProducer()
producer.send(topic_name, message_pack)
producer.flush()

