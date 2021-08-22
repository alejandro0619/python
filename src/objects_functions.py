class Student:
  def __init__(self, name, major, gpa) -> None:
      self.name = name
      self.major = major
      self.gpa = gpa

  def on_honor_roll(self) -> bool:
    if self.gpa >= 3.5:
      return True
    else:
      return False


print(Student("Alejandro", "CS", 5).on_honor_roll())
