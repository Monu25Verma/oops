#class attribute

class Employee:
    NoofWorkingHours = 40               #attributes assigned 40
    
employeeone = Employee()                #creating object
employeetwo = Employee()
Employee.NoofWorkingHours= 45               #updating the class of attribute values as 45
print(employeeone.NoofWorkingHours)     #print object of attributes

    
    
    
#instance attribute        #each and every object has there own instance 

employeeone.name = "Monu"       #as instance attr has there diffrent attribute so assigned it
print(employeeone.name)
#print(employeetwo.name)         #here u will get error because u have not assigned name for employeetwo

#how to solve this 
# soln here is assigned the value to attribute

employeetwo.name = "John"
print(employeetwo.name)

