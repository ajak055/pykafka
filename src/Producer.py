from abc import ABC, abstractmethod

class Producer(ABC):

    def __init__(self, host):
        self.host = host

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send_message(self):
        pass