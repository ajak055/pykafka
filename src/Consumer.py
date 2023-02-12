from abc import ABC, abstractmethod

class Consumer(ABC):

    def __init__(self, host):
        self.host = host

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_message(self):
        pass