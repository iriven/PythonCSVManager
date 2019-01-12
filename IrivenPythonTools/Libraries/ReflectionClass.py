#coding: utf-8
import inspect
class Iriven_ClassInfos(object):
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
    
    
if __name__ == "__main__":
    sys.exit(main())
