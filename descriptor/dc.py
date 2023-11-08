"""
__getattr__ is [only] invoked if the attribute is not defined in
 the instance, and it was not found.

__getattribute__ is invoked before looking for the attribute in
 the object instance. It has precedence over __getattr__

 setattr(object, name, value)

 The setattr() function takes three parameters:

    object - object whose attribute has to be set
    name - attribute name
    value - value given to the attribute

getattr(object, name[, default])
The above syntax is equivalent to:
    object.name

getattr() method takes multiple parameters:

    object - object whose named attribute's value is to be returned
    name - string that contains the attribute's name
    default (Optional) - value that is returned when the named attribute is not found
"""


class Descriptor:
    def __init__(self, name):
        self.name = name

    # When an attribute is being called
    def __get__(self, instance, owner):
        return instance.__dict__

    # When an instance is being assigned to a value
    def __set__(self, instance, value):
        instance.__dict__[self.name] = " ".join([e.capitalize() for e in value.split()])

    # def __getattribute__(self, item):
    #     print(
    #         "__getattribute__ is invoked before looking for the attribute in "
    #         "the object instance. It has precedence over __getattr__",
    #         item
    #         )


class Person:
    name = Descriptor("name")

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print(
            "__getattr__ is called to answer to getattr(object, attribute, default) function, "
            f'There is no "{item}"'
        )


p = Person("naser nafe")
print(p.name)
p.name = "mohsen namjo"
print(p.name)
getattr(p, "name2")
