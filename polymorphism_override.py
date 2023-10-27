class Employee:
    def numberofworkinghours(self):
        self.workinghours = 45

    def staff(self):
        print(self.workinghours)


class Traine(Employee):
    def workinghoursstaff(self):
        self.numberofworkinghours = 40


    def resetworkhours(self):
        super().numberofworkinghours()
        

 
employee = Employee()
employee.numberofworkinghours()
print("number of working hours is :", end= " ")
employee.staff()
traine = Traine()
traine.numberofworkinghours()
print("the updated number of working hours is:", traine.workinghours)
traine.resetworkhours()
print("the updated number of reet working hours is:", traine.resetworkhours)
traine.staff()