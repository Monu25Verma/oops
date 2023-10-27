class A:
    def method(self):
        print("this belongs to class A")
    pass

class B(A):
    def method(self):
        print("this belong to class B")
    pass

class C(A):
    def method(self):
        print("This belongs to class C")
    pass

class D(B, C):
    pass

d = D()
d.method()


