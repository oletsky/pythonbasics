from typing import Any


class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __getName(self):
        return __name

    def __getAge(self):
        return __age

    def introduce(self):
        print("I am "+self.__name+". I am "+str(self.__age)+" years old.")

p1=Person("Ivanov",102)
p2=Person("Petrova",25)
p1.introduce()
p2.introduce()

