from vehicle import Vehicle


class Board:
    """A class to represent a game board."""

    def __init__(self) -> None:
        """Constructor of class Board.
        
        Examples:
        >>> board = Board()

        >>> board.grid
        [['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]

        >>> board.vehicles
        []
        """

        self.grid = [['.' for _ in range(6)]for _ in range(6)]
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the game board.

        Args:
            vehicle: A vehicle from the class Vehicle.
        
        Examples:
        >>> board = Board()

        >>> vehicle = Vehicle('A', 0, 0, 'H', 2)

        >>> board.add_vehicle(vehicle)

        >>> board.grid[0][0], board.grid[0][1]
        ('A', 'A')
        """

        self.vehicles.append(vehicle)
        self.update_board()

    def cell_is_empty(self, x: int, y: int) -> bool:
        """Check if a box is empty or not.

        Args:
            x: Position x of the cell.
            y: Position x of the cell.

        Returns:
            True if the cell is empty, False otherwise.

        Examples:
        >>> board = Board()

        >>> board.cell_is_empty(0, 0)
        True
        """

        return self.grid[y][x] == '.'

    def update_board(self) -> None:
        """Update the game board."""
        for row in range(6):
            for col in range(6):
                self.grid[row][col] = '.'

        for vehicle in self.vehicles:
            x = vehicle.x
            y = vehicle.y

            if vehicle.orientation == 'H':
                for i in range(vehicle.size):
                    self.grid[y][x + i] = vehicle.name
            elif vehicle.orientation == 'V':
                for i in range(vehicle.size):
                    self.grid[y + i][x] = vehicle.name

    def print_board(self) -> None:
        """Display the game board.

        Examples:
        >>> board = Board()

        >>> board.print_board()
        . . . . . . 
        . . . . . . 
        . . . . . . > 
        . . . . . . 
        . . . . . . 
        . . . . . . 
        """

        for row in range(6):
            for col in range(6):
                print(self.grid[row][col], end=' ')

                if row == 2 and col == 5:
                    print('>', end=' ')
            
            print()

    def can_move(self, vehicle: Vehicle, direction: str) -> bool:
        """Check if a vehicle can move in the given direction.

        Args:
            vehicle: A vehicle from the class Vehicle.
            direction: The direction of the movement.

        Returns:
            True if the movement is possible, False otherwise.

        Examples:
        >>> board = Board()

        >>> vehicle = Vehicle('A', 0, 0, 'H', 2)

        >>> board.can_move(vehicle, 'R')
        True

        >>> board.can_move(vehicle, 'U')
        False
        """

        positions = vehicle.vehicle_positions()

        if vehicle.orientation == 'H' and direction not in ('L', 'R'):
            return False
        if vehicle.orientation == 'V' and direction not in ('U', 'D'):
            return False

        if direction == 'U':
            for x, y in positions:
                if y == 0 or (not self.cell_is_empty(x, y - 1) and self.grid[y - 1][x] != vehicle.name):
                    return False
        elif direction == 'D':
            for x, y in positions:
                if y == 5 or (not self.cell_is_empty(x, y + 1) and self.grid[y + 1][x] != vehicle.name):
                    return False
        elif direction == 'L':
            for x, y in positions:
                if x == 0 or (not self.cell_is_empty(x - 1, y) and self.grid[y][x - 1] != vehicle.name):
                    return False
        elif direction == 'R':
            for x, y in positions:
                if x == 5 or (not self.cell_is_empty(x + 1, y) and self.grid[y][x + 1] != vehicle.name):
                    return False
        else:
            return False
        
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
