from typing import TypeVar, Generic

class Animal: pass
class Dog(Animal): pass

T_co = TypeVar("T_co", covariant=True)

class ReadOnlyStack(Generic[T_co]):
    def __init__(self) -> None:
        self._items: list[T_co] = []

    def push(self, item: T_co) -> None:
        self._items.append(item)

    def peek(self) -> T_co:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]

dog_stack: ReadOnlyStack[Dog] = ReadOnlyStack()
animal_stack: ReadOnlyStack[Animal] = dog_stack
