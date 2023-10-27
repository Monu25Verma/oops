class Verma:         #verma - class
    #def __init__(self):       #default constructor/no argument cons / no parameterized constructor
    #    self.family_member = 3
    def __init__(self, family_member):          # argument cons/parameterized constructor
        self.family_member = family_member
        
    def job(self, child):
        print("most of verma's are doctor except", child)
        
        
# surendra = Verma()              #object of default constructor 
# print(surendra.family_member)           

arvind = Verma(6)               #object of paramterized cons
print(arvind.family_member)         
print(type(arvind))
arvind.job(3)

ravind = Verma(4)
print(ravind.family_member)         
ravind.job(2)

surendra = Verma(3)
print(surendra.family_member)         
surendra.job(1)

#diffrence between method and constuctor -> method is explicit is called but constructor is implicit no need to call 