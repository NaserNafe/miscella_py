"""
__getattr__ is [only] invoked if the attribute is not defined in
 the instance, and it was not found.

__getattribute__ is invoked before looking for the attribute in
 the object instance. It has precedence over __getattr__
"""


class Descriptor:
    def __init__(self, name):
        self.name = name

    # When an instance is being called
    # def __get__(self, instance, owner):
    #     return instance.__dict__

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
