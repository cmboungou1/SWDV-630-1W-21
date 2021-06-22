
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
   def __init__(self, name, id_number, hourly_rate):   
       self.name = name
       self.id_number = id_number  
       self.hourly_rate = hourly_rate 

   @abstractmethod
   def get_role(self):
       pass

   def __str__(self):
       return "{} - Name: {}, ID Number: {}, Hourly Rate: {}".format(self.__class__. __name__, self.name, self.id_number, self.hourly_rate)

class Manager(Employee):
   def get_role(self):
      return "manager"

class Full_Time_Employee(Employee):
   def get_role(self):
      return "full time employee"

class Part_Time_Employee(Employee):
   def get_role(self):
      return "part time employee"

class EmployeeFactory(object):
   @classmethod
   def create(cls, name, *args):
      name = name.lower().strip()

      if name == 'manager':
         return Manager(*args)
      elif name == 'full time employee':
         return Full_Time_Employee(*args)
      elif name == 'part time employee':
         return Part_Time_Employee(*args)

def main():
   print (EmployeeFactory.create('manager', 'David', 8, 30)) 
   print (EmployeeFactory.create('full time employee', 'Christ', 1, 25))
   print (EmployeeFactory.create('part time employee', 'Cara', 28, 20))
   pt_emp = EmployeeFactory.create('part time employee', 'Tim', 32, 15)
   print(pt_emp.get_role())

main()
