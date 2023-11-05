class Employee:
    def __init__(self, name):
        self.name = name
        
    def workinghours(self):
        print(self.name) 


employeeone = Employee("Monu")
employeetwo = Employee("Mathew")

employeeone.workinghours()
employeetwo.workinghours()


 