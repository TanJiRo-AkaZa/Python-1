from abc import ABC, abstractmethod
class ABsclass(ABC):
    def print(self,x):
        print("this the the value of x:",x)
    @abstractmethod
    def task(self):
        print("we are in ABsclass task method" )
class test_class(ABsclass):
    def task(self):
        print("we are in test_class task method" )
obj=test_class()
obj.task()
obj.print(100)