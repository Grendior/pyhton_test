class Dog():
  def __init__(self, name, bread, owner):
    self.name = name
    self.bread = bread
    self.owner = owner

class Person():
    def __init__(self, name):
      self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)

print(stan.owner.name)