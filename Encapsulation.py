class human:
    def __init__(self, name, age):
        self.__name = name #private attributes/properties/variables
        self.__age = age
        self.__onlyRead = 10
        self.__onlyWrite = int(input)
        self.__bothReadWrite = 26
        self.__noReadnoWrite = 30

#Encapsulation
    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setAge(self,age): #setter method
        self.__age = age

    def getAge(self): #getter method
        return self.__age
    
    def __show(self):
        print(f'His/her name is {self.__name} and age is {self.__age}.' )

    def getShow(self):
        self.__show()

himali = human("himali", 23) #reference/object variable
sonu = human("sonu", 20)

print("Before one year: ", himali.getAge())
himali.setAge(24)
print("After one year: ", himali.getAge())
himali.getShow()
