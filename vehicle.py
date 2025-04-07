class Vehicle:
    """A class to represent a vehicle."""
    
    def __init__(self, name: str, x: int, y: int, orientation: str, size: int) -> None:
        """Constructor of class Vehicle.

        Args:
            name: Name of the vehicle.
            x: Position x of the vehicle.
            y: Position y of the vehicle.
            orientation: Orientation of the vehicle.
            size: Size of the vehicle.

        Examples:
        >>> vehicle = Vehicle('A', 0, 0, 'H', 2)

        >>> vehicle.name
        'A'

        >>> vehicle.x
        0

        >>> vehicle.y
        0

        >>> vehicle.orientation
        'H'

        >>> vehicle.size
        2
        """

        self.name = name
        self.x = x
        self.y = y
        self.orientation = orientation
        self.size = size

    def vehicle_positions(self) -> list[tuple[int, int]]:
        """Return the positions of a vehicle on the game board.

        Returns:
            The positions of the vehicle on the game board.

        Examples:
        >>> vehicle_1 = Vehicle('A', 0, 0, 'H', 2)

        >>> vehicle_1.vehicle_positions()
        [(0, 0), (1, 0)]

        >>> vehicle_2 = Vehicle('O', 5, 0, 'V', 3)

        >>> vehicle_2.vehicle_positions()
        [(5, 0), (5, 1), (5, 2)]
        """

        positions = []

        if self.orientation == 'H':
            for i in range(self.size):
                positions.append((self.x + i, self.y))
        elif self.orientation == 'V':
            for i in range(self.size):
                positions.append((self.x, self.y + i))

        return positions

    def move(self, direction: str) -> None:
        """Move a vehicle in a given direction.

        Args:
            direction: The direction of movement.

        Examples:
        >>> vehicle = Vehicle('A', 0, 0, 'H', 2)

        >>> vehicle.vehicle_positions()
        [(0, 0), (1, 0)]

        >>> vehicle.move('R')

        >>> vehicle.vehicle_positions()
        [(1, 0), (2, 0)]
        """

        if direction == 'U' and self.orientation == 'V':
            self.y -= 1
        elif direction == 'D' and self.orientation == 'V':
            self.y += 1
        elif direction == 'L' and self.orientation == 'H':
            self.x -= 1
        elif direction == 'R' and self.orientation == 'H':
            self.x += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
