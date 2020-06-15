def find_empty_space(board, found_coordinates):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        found_coordinates[0] = row
        found_coordinates[1] = col
        return True
  return False

def num_in_row(board, row, num):
  for i in range(9):
    if(board[row][i] == num):
      return True
  return False

def num_in_col(board, col, num):
  for i in range(9):
    if(board[i][col] == num):
      return True
  return False

def num_in_box(board, row, col, num):
  for i in range(3):
    for j in range(3):
      if board[i + row][j + col] == num:
        return True
  return False

def legal_num_can_be_played(board, row, col, num):
  return not(num_in_row(board, row, num)) and not(num_in_col(board, col, num)) and not(num_in_box(board, row - row % 3, col - col % 3, num)) 

def solve(board):
  found_coordinates =  [0, 0]
  if (not(find_empty_space(board, found_coordinates))):
    return True
  row = found_coordinates[0]
  col = found_coordinates[1]
  for n in range(1, 10):
    if legal_num_can_be_played(board, row, col, n):
      board[row][col]= n
      if solve(board): 
        return True
      board[row][col] = 0
  return False
