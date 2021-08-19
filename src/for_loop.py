#For loop through a string:
def loop_string():
  for letter in "Hello World":
   print(letter)

numbers = [1, 2, 3, 4, 5]
def loop_number():
  for num in numbers:
   print(num)

def loop_range():
  for index in range(len(numbers)):
   print(index)

loop_range()