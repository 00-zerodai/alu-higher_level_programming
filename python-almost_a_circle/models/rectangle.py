#!/usr/bin/python3
"""Rectangle model for the almost_a_circle project."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class with width, height, x, and y attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle dimensions and position."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and set the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and set the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the x position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validate and set the x position."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the y position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validate and set the y position."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a readable string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assign attributes using positional arguments or keyword arguments."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args[:5]):
                setattr(self, attributes[index], value)
            return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
