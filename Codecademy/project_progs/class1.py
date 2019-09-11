class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Anderson", 36)
sloth = Animal("Monthy", 6)
ocelot = Animal("Gaston", 3)
hippo.description()
print hippo.health
print sloth.health
print ocelot.health
