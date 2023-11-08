"""
attribute = property(get, set, del, doc)
"""


class Person:
    def setName(self, name):
        self._name = " ".join([e.capitalize() for e in name.split()])

    def getName(self):
        return self._name

    name = property(getName, setName)


p = Person()
p.name = "naser nafe"
print(p.name)
# print(Person.__dict__)
