from abc import ABC, abstractmethod

class DomainEventHandler(ABC):

    @abstractmethod
    def listen():
        ...
        