# open files:

def read_employees():
  # modes: r(read), w(write), a(append info onto the end of the file), r+(read and write)
  employees_file = open("text/employees.txt", "r")
  # make sure is posible to read this file:
  if employees_file.readable():
    # return all the content in a string
    readable_file_string = employees_file.read()
    # return an array within each line:
    readable_file_array = employees_file.readlines()
    
  else:
    print('Couldn\'t read')
  # Close file:
  employees_file.close()

def write_employees():
  employees_file = open("./text/employees.txt", "a")
  if employees_file.writable():
   employees_file.write("\nSamantha - Receptionist")
  else:
    print("You can not write this file")
  employees_file.close()

def overwrite_employess_file():
  employees_file = open("./text/employees.txt", "w")
  if employees_file.writable():
    employees_file.write("Alexis - Product manager")
  else:
    print("Could not overwrite this file")
  employees_file.close()
overwrite_employess_file()