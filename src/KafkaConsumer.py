import sys
from pykafka import KafkaClient

#sys.path.insert(1, 'src/lib/consumer')

from Consumer import Consumer

class KafkaConsumer(Consumer):
    
    def __init__(self, topic):
        super().__init__("172.25.177.84:9092")
        self._consumer= None
        self.topic = topic

    def connect(self):
        client = KafkaClient(hosts=self.host)
        topic = client.topics[self.topic]
        self._consumer = topic.get_simple_consumer()

    def get_message(self):
        for message in self._consumer:
            if message is not None:
                print(message.value.decode('ASCII'))
        
kafkaConsumer = KafkaConsumer('my_first')
kafkaConsumer.connect()
kafkaConsumer.get_message()