import random

def hangman(word):
  wrong = 0
  stages = ["",
            "______     ",
            "|     |    ",
            "|     |    ",
            "|     0    ",
            "|    /|\   ",
            "|    / \   ",
            "|          "
            ]
  rletters = list(word)
  board = ["_"] * len(word)
  win = False
  print("Gra w wisielca")
  while wrong < len(stages) - 1:
    print("\n")
    msg = "Odgadnij literę: "
    guess = input(msg)
    if guess in rletters:
      cind = rletters.index(guess)
      board[cind] = guess
      rletters[cind] = '$'
    else:
      wrong += 1
    
    print((" ".join(board)))
    e = wrong + 1
    print("\n".join(stages[0: e]))
    if "_" not in board:
      print("Wygrałeś!")
      print(" ".join(board))
      win = True
      break
  if not win:
    print("\n".join(stages[0: wrong]))
    print("\nPrzegrałeś! Miałeś odgadnąć: {}.".format(word))

listOfWords = ['pies', 'kot', 'ptak', 'kangur']
hangman(random.choice(listOfWords))