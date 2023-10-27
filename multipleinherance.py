class operatingstatem:
    multitasking = True


class apple:
    manufactureybrand = "www.apple.in"


class mackbook(operatingstatem, apple):
        def __init__(self):
            if self.multitasking is True:
                self.manufactureyear = 2017
                print("Want to buy the macbook of year {} from webiste {}".format(self.manufactureyear,self.manufactureybrand))


Mackbook = mackbook()
