def input_valid_coordinates(prompt):
  while True:
    try:
      inputStr = input(prompt)
      x, y = inputStr.split(" ")
      x, y = int(x), int(y)
      if 0 <= x < 5 and 0 <= y < 5:
        return inputStr
      else:
        print("Ungültige Koordinaten. Bitte versuche es erneut.")
    except ValueError:
      print("Ungültige Eingabe. Bitte gib zwei Zahlen zwischen 0 und 4 ein.")


def print_grid(grid):
  for row in grid:
    print(" ".join(row))
  print()


def play_game():

  grid1 = [["~" for x in range(5)] for x in range(5)]
  grid2 = [["~" for x in range(5)] for x in range(5)]

  ship1_coords = input_valid_coordinates(
      "Spieler 1, bitte gib die Koordinaten für dein Schiff ein (z.B. 0 0):")
  ship2_coords = input_valid_coordinates(
      "Spieler 2, bitte gib die Koordinaten für dein Schiff ein (z.B. 0 0):")

  current_player = 1
  hit = False
  while hit is not True:
    print("Spieler " + str(current_player) + " ist am Zug:")

    attack_coords = input_valid_coordinates("Koordinaten für den Angriff:")
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
      print("Treffer!")
      print("Spieler " + str(current_player) + " gewinnt!")
      hit = True
    else:
      current_grid[y][x] = "O"

    print_grid(current_grid)

    if current_player == 1:
      current_player = 2
    else:
      current_player = 1


play_game()
