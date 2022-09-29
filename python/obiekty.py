import math

class Orange:
  def __init__(self, w, c):
    self.weight = w
    self.color = c
    print("Utworzono pomarańcze\nwaga: {},\nkolor: {}".format(w, c))
  
  def rot(self, days, temp):
    self.mold = days * temp

class Apple:
  def __init__(self, size, weight, color, taste):
    self.size = size
    self.weight = weight
    self.color = color
    self.taste = taste


class Circle:
  def field(self, r):
    return math.pi * math.pow(r, 2)

# orange1 = Orange(120, "ciemnopomarańczowy")

circle = Circle()

print(circle.field(2))

class Triangle:
  def area(self, a, h):
    return (a * h)/2

triangle = Triangle()

print(triangle.area(2, 2))
# print(orange1.color)
# print(orange1.weight)
# orange1.rot(10,29)
# print(orange1.mold)