
def guessing_game(secret):
  secret_word = secret
  guess = " "
  while secret_word != guess:
    guess = input("Enter the secret word \n")
    if secret_word == guess:
      return print("You won the game! ")

guessing_game("Hola")