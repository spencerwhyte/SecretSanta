
class Person:

  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.partner = None

  def setPartner(self, person):
    self.partner = person

  def getPartner(self):
    return self.partner

  def getName(self):
    return self.name

  def getEmail(self):
    return self.email
