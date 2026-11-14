#!/usr/bin/python3
"""Square model for the almost_a_circle project."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square with a single side value."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Validate and set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a readable string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """Assign attributes with positional or keyword arguments."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for index, value in enumerate(args[:4]):
                if attributes[index] == "size":
                    self.size = value
                else:
                    setattr(self, attributes[index], value)
            return

        for key, value in kwargs.items():
            if key == "size":
                self.size = value
            else:
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
