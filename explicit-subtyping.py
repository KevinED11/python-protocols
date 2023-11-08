from typing import Protocol, Iterable
from abc import abstractmethod


class Animal(Protocol):
    @abstractmethod
    def make_sound(self) -> None:
        pass


class Dog(Animal):
    def make_sound(self) -> None:
        print("Woof!")


class Cat(Animal):
    def make_sound(self) -> None:
        print("Meow!")


class Elephant(Animal):
    def make_sound(self) -> None:
        print("Roar!")


def make_sound(animal: Animal) -> None:
    animal.make_sound()


def make_sounds(animals: Iterable[Animal]) -> None:
    for animal in animals:
        make_sound(animal=animal)


def main() -> None:
    animals = [Dog(), Cat(), Elephant()]
    make_sounds(animals=animals)


if __name__ == "__main__":
    main()
