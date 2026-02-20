# 1, John, 35
id = 1
name = 'John'
age = 35

john = [1, 'John', 35]
john[2]

john = {id: 1, name: 'John', age: 35}
john[id] = 4

class Person:
    def __init__(self, id, name: str, age: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("Id must be an integer")
        self.id = id
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name should be a non-empty string")
        self._name = value.strip()

john = Person(1, 'John', 35)
print(john.name)

from dataclasses import dataclass

@dataclass
class EasyPerson:
    id: int
    name: str
    age: int

    def __post_init__(self):
        if not isinstance(id, int) or id < 0:
            raise ValueError("Id must be an integer greater than 0")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name should be a non-empty string")
        self.name = self.name.strip()

john = EasyPerson(1, "John", 35)
print(john)