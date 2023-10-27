class hotel:
    hotel_name = "Dalhousie hotel"

class chef(hotel):
    todays_special  = "chicken"
    price = "350rupee"

class Orderfood(chef):
    def __init__(self):
        print("Sir welcome to the {} would you like to order our todays specaial {} in just {} only.".format(self.hotel_name, self.todays_special, self.price))



orderfood = Orderfood()




     