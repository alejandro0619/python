def guessing_game(secret):
  secret_word = secret
  guess = " "
  attemps = 0
  while secret_word != guess and attemps < 3:
    guess = input("Enter the secret word \n")
    attemps += 1
    if secret_word != guess and attemps >= 3:
      return print("You lose")
    if secret_word == guess and attemps <= 3:
      return print("You won the game!")

guessing_game("Hola")