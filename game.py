from board import Board
from vehicle import Vehicle


board = Board()
file_lines = []
vehicles = {}
has_won = False

with open("./challenge_cards/challenge_40.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    file_lines.append(line.strip().split(","))

for i in range(1, len(file_lines)):
    vehicle_name = file_lines[i][0]
    vehicle_x = int(file_lines[i][1])
    vehicle_y = int(file_lines[i][2])
    vehicle_orientation = file_lines[i][3]
    vehicle_size = int(file_lines[i][4])

    vehicles[vehicle_name] = Vehicle(vehicle_name, vehicle_x, vehicle_y, vehicle_orientation, vehicle_size)
    board.add_vehicle(vehicles[vehicle_name])

while not has_won:
    board.print_board()
    vehicle_choice = input("Enter the vehicle name: ")

    while vehicle_choice not in vehicles:
        vehicle_choice = input(f"The vehicle {vehicle_choice} does not exist, enter the vehicle name: ")

    direction_choice = input("Enter the direction of movement: ")

    while direction_choice not in ['U', 'D', 'L', 'R']:
        direction_choice = input(f"The direction {direction_choice} does not exist, enter the direction of movement: ")

    if vehicles[vehicle_choice].name == 'X' and vehicles[vehicle_choice].x == 4:
        has_won = True
        print("You have won!")
    elif board.can_move(vehicles[vehicle_choice], direction_choice):
        vehicles[vehicle_choice].move(direction_choice)
        board.update_board()
    else:
        print("You can't move this vehicle in this direction.")
