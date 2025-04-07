def input_valid_coordinates(prompt):
  while True:
    try:
      inputStr = input(prompt)
      x, y = inputStr.split(" ")
      x, y = int(x), int(y)
      if 0 <= x < 5 and 0 <= y < 5:
        return inputStr
      else:
        print("Invalid coordinates. Please try again")
    except ValueError:
      print("Invalid input. Please enter two digits between 0 and 4.")


def print_grid(grid):
  for row in grid:
    print(" ".join(row))
  print()


def play_game():

  grid1 = [["~" for x in range(5)] for x in range(5)]
  grid2 = [["~" for x in range(5)] for x in range(5)]

  ship1_coords = input_valid_coordinates(
      "Player 1, please enter the coordinates for your ship (e.g. 0 0):")
  ship2_coords = input_valid_coordinates(
      "Player 2, please enter the coordinates for your ship (e.g. 0 0):")

  current_player = 1
  hit = False
  while hit is not True:
    print("It's your turn, player " + str(current_player))

    attack_coords = input_valid_coordinates("Coordinates for an attack:")
    x, y = attack_coords.split(" ")
    x, y = int(x), int(y)
    oppenent_ship_coords = ""
    current_grid = []

    if current_player == 1:
      opponent_ship_coords = ship2_coords
      current_grid = grid1
    elif current_player == 2:
      opponent_ship_coords = ship1_coords
      current_grid = grid2

    if attack_coords == opponent_ship_coords:
      current_grid[y][x] = "X"
      print("Hit!")
      print("Player " + str(current_player) + " wins!")
      hit = True
    else:
      current_grid[y][x] = "O"

    print_grid(current_grid)

    if current_player == 1:
      current_player = 2
    else:
      current_player = 1


play_game()
