#Apple show which has mac book and contact us on apple webiste
#Apple is the base class
# mac book is the derived class

class Apple:
    manufacture = "Apple.in"
    manufacturename = "Apple.co.in/contacs"

    def contactdetails(self):
        print("Want to buy then contact us on ", self.manufacturename)

class Macbook(Apple):
    def __init__(self):
        self.yearofmanufacture = 2017

    def manufacturedet(self):
        print("this mackbook was manufacted in year {} by {}".format(self.yearofmanufacture, self.manufacture))

mackbook = Macbook()

mackbook.manufacturedet()
mackbook.contactdetails()