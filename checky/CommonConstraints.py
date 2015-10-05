from ContainerConstraint import ContainerConstraint
from InternalHelpers import *

class CMethod(ContainerConstraint):

    def __init__(self,name,argcount=None):
        def check_method(obj):
                    if not internal__has__function(obj,name):
                        return False
                    if argcount == None:
                        return True
                    if internal__check__if__builtin(obj):
                        return True
                    else:
                        return internal__num__args(obj) == argcount + 1
        super(CMethod,self).__init__(check_method)
        self._name = name
        self._argcount = argcount

    def __str__(self):
        if self._argcount == None:
            return "Method constraint : `{}` with {} arguments".format(self._name,self._argcount)
        else:
            return "Method constraint: `{}`".format(self._name)

    def errorString(self):
        if self._argcount == None:
            return "Value has no method named `{}`".format(self._name)
        else:
            return "Value has no method named `{}` with {} arguments".format(self._name,self._argcount)

    def _getContainedValue(self,x):
        return x.__getattribute__(self._name)

class CStaticMethod(ContainerConstraint):

    def __init__(self,name,argcount = None):
        def check_static_method(obj):
            if not internal__has__function(obj.__getattribute__(name)):
                return False
            if argcount == None:
                return True
            if internal__check__if__builtin(obj.__getattribute__(name)):
                return True
            else:
                return internal__num__args(obj) == argcount
        super(CStaticMethod,self).__init__(check_static_method)
        self._name = name
        self._argcount = argcount

    def __str__(self):
        if self._argcount == None:
            return "Static method constraint: `{}`".format(self._name)
        else:
            return "Static method constraint: `{}` with {} arguments".format(self._name,self._argcount)

    def errorString(self):
        if self._argcount == None:
            return "Value has no static method `{}`".format(self._name)
        else:
            return "Value has no static method `{}` with {} arguments".format(self._name)

    def _getContainedValue(self,x):
        return x.__getattribute__(self._name)

class CConstructor(ContainerConstraint):
    
    def __init__(self,argcount=None):
        def check_constructor(obj):
            if not internal__has__function(obj,'__init__'):
                return False
            if argcount == None:
                return True
            if internal__check__if__builtin(obj.__init__):
                return True
            else:
                return internal__num__args(obj.__init__) == argcount+1
        super(CConstructor,self).__init__(check_constructor) 
        self._argcount = argcount

    def __str__(self):
        if self._argcount == None:
            return "Has constructor constraint"
        else:
            return "Has constructor with {} arguments constraint".format(self._argcount)

    def errorString(self):
        if self._argcount == None:
            return "Value has no constructor"
        else:
            return "Value has no constructor with {} arguments".format(self._argcount)

    def _getContainedValue(self,x):
        return x.__init__

class CAttribute(ContainerConstraint):
    def __init__(self,aname,atype=None):
        if atype != None:
            super(CAttribute,self).__init__(lambda x: aname in dir(x) and isinstance(x.__getattribute__(aname),atype))
        else:
            super(CAttribute,self).__init__(lambda x: aname in dir(x))
        self._name = name
        self._atype = atype

    def __str__(self):
        if self._atype == None:
            return "Attribute constraint: `{}` with no type check".format(self._name)
        else:
            return "Attribute constraint: `{}` with type `{}`".format(self._name,self._atype)

    def errorString(self):
        if self._atype == None:
            return "Value has no attribute `{}`".format(self._name)
        else:
            return "Value has no attribute `{}` with type `{}`".format(self._name,self._atype)

    def _getContainedValue(self,x):
        return x.__getattribute__(self._name)
 
