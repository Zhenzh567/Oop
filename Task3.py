from typing import TypeVar, Generic

class Animal:
    def __init__(self, name: str = ""):
        self.name = name

class Dog(Animal): pass

T_contra = TypeVar("T_contra", contravariant=True)

class Validator(Generic[T_contra]):
    def validate(self, item: T_contra) -> bool:
        raise NotImplementedError

class AnimalValidator(Validator[Animal]):
    def validate(self, item: Animal) -> bool:
        return bool(item.name)

def check(v: Validator[Dog], d: Dog) -> bool:
    return v.validate(d)

result = check(AnimalValidator(), Dog("Rex"))
print(result)
