class Assignment:
    def __init__(self):
        self.__onlyRead = 10 #sirf read karna not write
        self.__onlyWrite = 35 #sirf write karna not read
        self.__bothReadWrite = 26 #both read & write
        self.__noReadnoWrite = 30 #do nothing

#A
    def getOnlyRead(self):
        return self.__onlyRead
#B
    def setOnlywrite(self, value): 
        print("Before write the value {}".format(self.__onlyWrite))
        self.__onlyWrite = value
        print("After write the value {}".format(self.__onlyWrite))

#C
    def getBothReadWrite(self):
        return self.__bothReadWrite
    
    def setBothReadWrite(self, value):
        self.__bothReadWrite = value
#D
# noReadnoWrite is not accessible!

assignment1 = Assignment()
print(assignment1.getOnlyRead())
assignment1.setOnlywrite(45)
assignment1.setBothReadWrite(85)
print(assignment1.getBothReadWrite())
