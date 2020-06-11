

from abc import ABC, abstractmethod
class EnterInfo(ABC):
    def Names(self, name):
        print("You have entered {} as your name.".format(name))
    @abstractmethod
    def skept(self, name):
        pass

class RejInfo(EnterInfo):
    def skept(self, name):
        print("Your name can't possibly be:",name)

abst = RejInfo()
abst.Names("John"),abst.skept("John")
