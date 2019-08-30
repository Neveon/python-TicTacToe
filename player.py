import board

class player:
  arr = [[[1],[2],[3]], [[4],[5],[6]], [[7],[8],[9]]] # arr init
  board.Init(arr)
  # CheckGame will change gameCondition
  gameCondition = False
  target = 0
  letter = 'X'

  while gameCondition == False:
    # while not board.ValidSpace(arr, target) or :
      target = int(input('Where would you place {}?: '.format(letter)))
      # If space inputted is empty returns True
      conditional = board.ValidSpace(arr, target)

      if not conditional:
        print('Not a valid space')
      else:
        # Switching letter each board update
        if letter == 'X':
          board.UpdateBoard(arr, target, letter)

          # Check if game win/draw
          (gameCondition, output) = board.CheckGame(arr, letter)
          print(gameCondition)
          if output != None:
            print(output)
          
          # Change letter after check
          letter = 'Y'
        elif letter == 'Y':
          board.UpdateBoard(arr, target, letter)
          
          # Check if game win/draw
          (gameCondition, output) = board.CheckGame(arr, letter)
          print(gameCondition)
          if output != None:
            print(output)

          # Change letter after check
          letter = 'X'

  print('-------GAME END-------')

    

  


test = player()

