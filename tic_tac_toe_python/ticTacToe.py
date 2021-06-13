#TEST=True
TEST=False

# tic tac toe string
# empty  :   ---------
#        :   X O X O X
# 0: TL, 1: TC, 2: TR
# 3: CL, 4: CC, 5: CR
# 6: BL, 7: BC, 8: BR
#

# hasWinner: tttString
#  return:
#    O - if tttString has an O winner
#    X - if tttString has an X winner
#    None - if tttString has no winner
def hasWinner(tttString):
  # test if O winner
  if hasWinnerHelper(tttString, 'O'):
    return 'O'
  if hasWinnerHelper(tttString, 'X'):
    return 'X'
  return None


def hasWinnerHelper(tttString, testChar):
  top_row = [0,1,2]
  middle_row = [3,4,5]
  bottom_row = [6,7,8]
  left_col = [0,3,6]
  center_col = [1,4,7]
  right_col = [2,5,8]
  diagonal1 = [0,4,8]
  diagonal2 = [2,4,6] 
  return (testTriplet(tttString, testChar, top_row) or
          testTriplet(tttString, testChar, middle_row) or
          testTriplet(tttString, testChar, bottom_row) or
          testTriplet(tttString, testChar, left_col) or
          testTriplet(tttString, testChar, center_col) or
          testTriplet(tttString, testChar, right_col) or
          testTriplet(tttString, testChar, diagonal1) or
          testTriplet(tttString, testChar, diagonal2))
  
def testTriplet(tttString, testChar, triplet):
  if (tttString[triplet[0]] == testChar and
      tttString[triplet[1]] == testChar and
      tttString[triplet[2]] == testChar):
    return True
  return False


def displayBoard(tttString):
  print ("+-+-+-+")
  print ("|"+tttString[0]+"|"+tttString[1]+"|"+tttString[2]+"|")
  print ("+-+-+-+")
  print ("|"+tttString[3]+"|"+tttString[4]+"|"+tttString[5]+"|")
  print ("+-+-+-+")
  print ("|"+tttString[6]+"|"+tttString[7]+"|"+tttString[8]+"|")
  print ("+-+-+-+")


MOVES=["TL","TC","TR","CL","CC","CR","BL","BC","BR"]
def getPlayerMove(playerName, tttString):
  moveIsGood = False
  while (not moveIsGood):
    print("enter move for player "+playerName)
    move = input()
    # validate user input
    if move not in MOVES:
      print ("invalid move "+move+" is not one of: "+str(MOVES))
      continue
    # validate the move
    movePos = MOVES.index(move)
    if tttString[movePos] != ' ':
      print ("invalide move "+move+", space is occupied")
      continue
    moveIsGood=True
  return movePos


def tttGame():
  OsTurn = True
  tttString = "         "
  while True:
    displayBoard(tttString)
    if OsTurn:
      move = getPlayerMove("O player", tttString)
      tttString = tttString[:move] + 'O' + tttString[move+1:]
      if (hasWinner(tttString)):
        displayBoard(tttString)
        print ("O player wins")
        break
      OsTurn=False
    else:
      move = getPlayerMove("X player", tttString)
      tttString = tttString[:move] + 'X' + tttString[move+1:]
      if (hasWinner(tttString)):
        displayBoard(tttString)
        print ("X player wins")
        break
      OsTurn=True
    if ' ' not in tttString:
      print ("it's a tie!")
      break

##################################################
# test cases
def testHasWinner(tttString):
  print(' hasWinner('+tttString+'):', hasWinner(tttString))

def testDisplayBoard(tttString):
  print(' displayBoard('+tttString+'):')
  displayBoard(tttString)

if TEST:
  print("test winning combinations:")
  testHasWinner("X  X  X  ")
  testHasWinner("O  O  O  ")
  testHasWinner(" X  X  X ")
  testHasWinner(" O  O  O ")
  testHasWinner("  X  X  X")
  testHasWinner("  O  O  O")
  testHasWinner("X  X  X  ")
  testHasWinner("O  O  O  ")
  testHasWinner(" X  X  X ")
  testHasWinner(" O  O  O ")
  testHasWinner("  X  X  X")
  testHasWinner("  O  O  O")
  testHasWinner("X   X   X")
  testHasWinner("O   O   O")
  testHasWinner("  X X X  ")
  testHasWinner("  O O O  ")
  print("test non-winning combinations:")
  testHasWinner("X  O  X  ")
  testHasWinner("O  O  X  ")
  testHasWinner(" O  X  X ")
  testHasWinner(" O  X  O ")
  testHasWinner("  X  O  X")
  testHasWinner("  X  O  O")
  testHasWinner("O  X  X  ")
  testHasWinner("O  O  X  ")
  testHasWinner(" X  O  X ")
  testHasWinner(" X  O  O ")
  testHasWinner("  X  X  O")
  testHasWinner("  X  O  O")
  testHasWinner("X   O   X")
  testHasWinner("O   O   X")
  testHasWinner("  O X X  ")
  testHasWinner("  O O X  ")

  print("test display board")
  testDisplayBoard("X  X  X  ")
  testDisplayBoard("XO XOXOX ")

tttGame()

