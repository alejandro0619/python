class Chef:
  def make_chicken(self):
    print("The chef makes a chicken")
  
  def make_salad(self):
    print("The chef makes a salad")
  
  def make_special_dish(self):
    print("The chef makes a bbq ribs")

class ChineseChef (Chef): # inheritate chef methods
  def make_fried(self):
    print("The Chinese cheff akes fried rice")

myChef = ChineseChef().make_chicken()
