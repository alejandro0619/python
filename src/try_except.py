# We can handling errors:
def convert_to_int():
  try:
    print(10/0)
    inputValue = int(input("Enter a number:"))
    print(inputValue)

  except ZeroDivisionError as err:
      print(err)
  except:
    print("Invalid input")

convert_to_int()