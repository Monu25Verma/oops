#checkt the employee wheater they achievd weekly target

class Employee:
    name= "Monu"
    salesAchieve = 7
    designation = "Engineer"
    
    def __init__(self):
        print("inside constructor")
    
    def achieve_target(self):          # default parameter is used to access to attribute of class
        if self.salesAchieve >= 4:
            print("target has achieve successfully")
        else:
            print("target has not achieve successfully")
            
            
employeeOne = Employee()            #will have to create object to access
print(employeeOne.name, employeeOne.designation)
employeeOne.achieve_target()

employeeTwo = Employee()
print(employeeTwo.name, employeeTwo.designation)



            
        