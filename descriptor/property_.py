"""
    property, getter, setter, deleter
"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('The Value must be string')
        self._name = None

    @name.deleter
    def name(self):
        self._name = None


p = Person(454)
p.name = 12

print(p.name)
