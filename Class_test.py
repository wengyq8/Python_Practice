class MyClass:
    def myNoActionMethod(self):
        print 'Test push'
mc = MyClass()
mc.myNoActionMethod()
print dir(MyClass)
print MyClass.__name__
print MyClass.__doc__
