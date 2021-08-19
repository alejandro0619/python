def while_loop():
  i = 1
  while i <= 220:
    print(i, "\n")
    i += 1

# just did a fizzbuzz 
def fizz_buzz():
  i = 0
  while i<= 100:
    if i % 15== 0:
      print('FizzBuzz')
    elif i % 5 == 0:
      print("Buzz")
    elif i % 3 == 0:
      print("Fizz")
    else:
      print(i)
    i += 1
fizz_buzz()