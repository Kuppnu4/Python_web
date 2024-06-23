from abc import ABC, abstractmethod

class ABCInterface(ABC):

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def search():
        pass

    @abstractmethod
    def edit():
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def save():
        pass

    @abstractmethod
    def load():
        pass

    @abstractmethod
    def view():
        pass

    @abstractmethod
    def exit():
        pass
