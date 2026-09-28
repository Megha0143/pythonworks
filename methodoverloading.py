class A:
    def f(self):
        print("in first function f")
    def f(self,a):
        print("in second function f")
    def f(self,b):
        print("in third function f")
a=A()
# a.f()
# a.f(10)
a.f(20,30)