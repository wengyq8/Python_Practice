class ClassMethod_StaticMethod():
    def foo(self, x):
        print "foo(%s, %s)"%(self, x)
    @classmethod
    def Class_Foo(cls, x):
        print "Class_Foo(%s, %s)"%(cls, x)
    @staticmethod
    def Static_Foo(x):
        print "Static_Foo(%s)"%x

def TestThreeMethod():
    obj = ClassMethod_StaticMethod()
    obj.foo('test')
    obj.Class_Foo('test')
    ClassMethod_StaticMethod.Class_Foo('test')
    obj.Static_Foo('test')
    ClassMethod_StaticMethod.Static_Foo('test')

if __name__ == '__main__':
    TestThreeMethod()

