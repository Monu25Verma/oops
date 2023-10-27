class Square:
    def __init__(self, side):
        self.side  = side


    def __add__(oneside, twoside):
        return((oneside.side * 4) + (twoside.side * 4))

oneside = Square(5)         #5 * 4 = 20            #35 + 28 -> 63   
twoside = Square(7)         #7 * 4 = 28  
         
#print("Sum of two side are: ", (oneside * 4) + (twoside * 4))
print("sum of two square is: ",oneside+twoside)