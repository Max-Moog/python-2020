class Person:
   age: 0
   name: "Rafantony"
   nachname: "batistiedemann"
   hobby: "Fussball"

   def __init__(self, name, age, nachname, hobby):
      self.name = name
      self.age = age
      self.nachname = nachname
      self.hobby = hobby

   def get_name(self):
      return self.name

   def get_age(self):
      return self.age

   def set_age(self, age):
      self.age = age

   def toString(self):
      return "name: " + self.name + ", age: " + str(self.age)
