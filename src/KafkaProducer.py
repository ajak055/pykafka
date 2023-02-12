from pykafka import KafkaClient

from Producer import Producer

class KafkaProducer(Producer):
    def __init__(self, topic):
        super().__init__("172.25.177.84:9092")
        self._producer= None
        self.topic = topic

    def connect(self):
        client = KafkaClient(hosts=self.host)
        topic = client.topics[self.topic]
        self._producer = topic.get_sync_producer()

    def send_message(self, message):
        self._producer.produce(message.encode('ASCII'))

kafkaproducer = KafkaProducer('my_first')
kafkaproducer.connect()
kafkaproducer.send_message("hello kafka")