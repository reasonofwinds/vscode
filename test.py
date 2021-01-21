import os

class Person:
    def __init__(self, last_name, first_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def getName(self):
        name = self.last_name + self.first_name
        return name
    
    def say(self):
        name = self.getName()
        text = name + ':' + str(self.age)
        return text

person = Person("chao-hsien", "Ting", 25)
text = person.say()

print(text)