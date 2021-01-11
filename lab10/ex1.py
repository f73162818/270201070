class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height

  def area(self):
    return (2*3.14*(self.radius**2))+(self.height*2*3.14*self.radius)
  
  def volume(self):
    return 3.14*(self.radius**2)*self.height

cylinder = Cylinder(3,5)
print(cylinder.area())
print(cylinder.volume())