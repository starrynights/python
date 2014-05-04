__metaclass__ = type
class MyClass:
    @staticmethod
    def smethod():
        print "This is a static method"

    @classmethod
    def cmethod(cls):
        print "This is a class method"

MyClass.smethod()
c = MyClass()
c.cmethod()
