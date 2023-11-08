class Descriptor:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    # When an instance is being called
    # def __get__(self, instance, owner):
        # return instance.__dict__

    # When an instance is being assigned to a value
    def __set__(self, instance, value):
        # if instance
        instance.__dict__[self.name] = " ".join([e.capitalize() for e in value.split()])


class Person:
    name = Descriptor("name", "id_number")
    # id_number = Descriptor("id_number")

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


p = Person("naser nafe", 1)
print(p.id_number)
print(p.name)
