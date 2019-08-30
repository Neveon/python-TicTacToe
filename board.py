# Initiate empty array - empty board
def Init(arr):
  print('NOTE: Numbers 1-9 represent a spot to mark')
  print('START GAME')
  BoardPrint(arr)


def BoardPrint(arr):
  for row in arr:
    print(row)

def ValidSpace(arr, target):
  for row in arr:
    for element in row:
      if target == element[0]:
        return True
  
  return False

def UpdateBoard(arr, target, letter):
  for row in arr:
    for element in row:
      if target in element:
        print('\nBOARD UPDATED\n')
        element[0] = letter
        BoardPrint(arr)

def CheckGame(arr, le):
  # check for vertical/horizontal/diagnol matches - return if theres a match
  if le in arr[0][0] and le in arr[0][1] and le in arr[0][2]: # Across top
    return (True, '{} WINS!'.format(le))
  if le in arr[0][0] and le in arr[1][1] and le in arr[2][2]: # Diagnol, top->right
    return (True, '{} WINS!'.format(le))
  if le in arr[0][2] and le in arr[1][1] and le in arr[2][0]: # Diagnol, top->left
    return (True, '{} WINS!'.format(le))
  if le in arr[2][0] and le in arr[2][1] and le in arr[2][2]: # Across bot
    return (True, '{} WINS!'.format(le))
  if le in arr[1][0] and le in arr[1][1] and le in arr[1][2]: # Across middle
    return (True, '{} WINS!'.format(le))
  if le in arr[0][1] and le in arr[1][1] and le in arr[2][1]: # Down middle
    return (True, '{} WINS!'.format(le))
  if le in arr[0][0] and le in arr[1][0] and le in arr[2][0]: # Left
    return (True, '{} WINS!'.format(le))
  if le in arr[0][2] and le in arr[1][2] and le in arr[2][2]: # Right
    return (True, '{} WINS!'.format(le))

  # If no empty arr spaces, end game as draw
  unmarked = []
  for row in arr:
    for element in row:
      if element[0] in range(1,10): # check if element is a number (1-9)
        unmarked.append(element[0])
  if len(unmarked) == 0:
    return (True, 'GAME IS A DRAW')
  else:
    # return False and output is None, game goes on
    return (False, None)
