class Employee:
  
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def information(self):
    return self.name,self.salary

  def getName(self):
    return self.name
  
  def getSalary(self):
    return self.salary

  def setName(self,name):
    self.name = name

  def setSalary(self,salary):
    self.salary = salary

  