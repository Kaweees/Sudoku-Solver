def display(board):
  grid = []
  for i in range(len(board)):
    if (i+1) == 1:
      grid += ["+-------+-------+-------+"]
    s = ""
    for j in range(len(board[i])):
      if (j + 1) == 1:
        s += "| "
      s += str(board[i][j])
      s += " "
      if (j+1) % 3 == 0:
        s += "| "
    grid += [s]
    if (i+1) % 3 == 0:
      grid += ["+-------+-------+-------+"]
  
  for i in range(len(grid)):
    print(grid[i])
