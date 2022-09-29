class Shape():
  def what_am_i(self):
    print("Jestem figurą")

class Rectangle(Shape):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def calculate_perimeter(self):
    print(self.a + self.b + self.c)

class Square(Shape):
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def calculate_perimeter(self):
    print(self.a * 2 + self.b * 2)
  
  def change_size(self, a, b):
    self.a += a
    self.b += b


rq = Rectangle(5,2,1)
rq.calculate_perimeter()

sq = Square(2,5)
sq.calculate_perimeter()

sq.change_size(2, -1)

sq.calculate_perimeter()

rq.what_am_i()

class Rider():
  def __init__(self, name):
    self.name = name

class Horse():
  def __init__(self, name, rider):
    self.name = name
    self.rider = rider

rider = Rider("Mike Tyson")
horse = Horse("klacz", rider)

print(horse.rider.name)
