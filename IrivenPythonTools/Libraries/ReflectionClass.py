#coding: utf-8
import inspect
class Iriven_ReflectionClass(object):
    def __init__(self, clsobj):
        self.clsobj = clsobj

    def GetProperties(self):
        prop = {}
        for name in dir(self.clsobj):
            value = getattr(self.clsobj, name)
            if not name.startswith('__') and not inspect.ismethod(value):
                prop[name] = value
        return prop
    
    def GetMethods(self):
        method = {}
        for name in dir(self.clsobj):
            attr = getattr(self.clsobj, name)
            if not name.startswith('__') and inspect.ismethod(attr):
                method[name] = attr
        return method
    '''
    def all_members(self, aClass):
        try:
            # Try getting all relevant classes in method-resolution order
            mro = list(aClass.__mro__)
        except AttributeError:
            # If a class has no _ _mro_ _, then it's a classic class
            def getmro(aClass, recurse):
                mro = [aClass]
                for base in aClass.__base__: 
                    mro.extend(recurse(base, recurse))
                return mro
            mro = getmro(aClass, getmro)
        mro.reverse()
        members = {}
        for someClass in mro: 
            members.update(vars(someClass))
        return members
    '''
    
if __name__ == "__main__":
    sys.exit(main())
