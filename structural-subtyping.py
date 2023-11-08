from typing import Protocol, Iterable, NamedTuple


type DrawableType = "circle" | "square" | "triangle" | "rectangle"
type DrawableIterable = Iterable[Drawable]


class Drawable(Protocol):
    def draw(self) -> None:
        ...


class Circle:
    def draw(self) -> None:
        print("Drawing a circle")


class Square:
    def draw(self) -> None:
        print("Drawing a square")


class Triangle:
    def draw(self) -> None:
        print("Drawing a triangle")


class Rectangle:
    def draw(self) -> None:
        print("Drawing a rectangle")


def drawable_factory(drawable: DrawableType) -> Drawable:
    factories = {
        "circle": Circle,
        "square": Square,
        "triangle": Triangle,
        "rectangle": Rectangle,
    }

    return factories[drawable]()


def factory(drawables: Iterable[str]) -> tuple[Drawable, ...]:
    return tuple(drawable_factory(drawable=drawable) for drawable in drawables)


def draw_objects(objects: DrawableIterable) -> None:
    for obj in objects:
        obj.draw()


def main(drawables: DrawableIterable) -> None:
    draw_objects(objects=drawables)


class Drawables(NamedTuple):
    circle: Circle = "circle"
    square: Square = "square"
    triangle: Triangle = "triangle"
    rectangle: Rectangle = "rectangle"


if __name__ == "__main__":
    drawables: tuple[Drawable, ...] = factory(drawables=Drawables())
    main(drawables=drawables)
