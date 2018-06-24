# -*- coding: utf-8 -*-
class ClassMethod_StaticMethod():
    def foo(self, x):
        print "foo(%s, %s)"%(self, x)
    @classmethod
    #classmethod默认入参是cls不是self
    def Class_Foo(cls, x):
        print "Class_Foo(%s, %s)"%(cls, x)
    @staticmethod
    def Static_Foo(x):
    #staticmethod没有隐藏的入参
        print "Static_Foo(%s)"%x

def TestThreeMethod():
    obj = ClassMethod_StaticMethod()
    obj.foo('test')
    obj.Class_Foo('test')
    #classmethod和staticmethod都可以直接以类名调用方法
    ClassMethod_StaticMethod.Class_Foo('test')
    obj.Static_Foo('test')
    ClassMethod_StaticMethod.Static_Foo('test')

if __name__ == '__main__':
    TestThreeMethod()

