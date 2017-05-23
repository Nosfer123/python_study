class A:
    def method(self):
        print("A")


class B:
    def method(self):
        print("B")


class C(A, B):
    pass


class D(B, A):
    pass

c = C()
c.method()

