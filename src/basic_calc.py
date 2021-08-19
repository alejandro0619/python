def calculator():
  num1 = float(input("Enter a number:"))
  op = input("Enter a operator:")
  num2 = float(input("Enter a number:"))
  if op == '+':
    return round(num1 + num2)
  elif op == '-':
    return round(num1 - num2)
  elif op == '*':
    return round(num1 + num2)
  elif op == '/':
    return round(num1 + num2)
  else:
    return print('Enter a valid operator')

print(calculator()) 