from Constraint import Constraint 

class TypeCheck(object):

    def _getArgs(self,f):
        return f.func_code.co_varnames[:f.func_code.co_argcount]

    def __init__(self,*args,**kargs):
        if __debug__:
            for i in xrange(len(args)):
                if args[i].__class__ != type and not isinstance(args[i], Constraint):
                    raise TypeError("Got non-type or constraint constraint for argument type check.. ")
            self._argList = args
            for (k,v) in kargs.iteritems():
                if v.__class__ != type and  v.__class__ != Constraint:
                    raise TypeError("Got non-type constraint for argument type check..")
            self._argDict = kargs

    def __call__(self,f):
        if __debug__ :
            def checked_f(*args,**kargs):
                f_args = self._getArgs(f)
                f_dict = {}
                for i in xrange(len(args)):
                    if i < len(self._argList):
                        if not isinstance(args[i],self._argList[i]):
                            if isinstance(self._argList[i],Constraint):
                                raise TypeError("Constraint mismatch for function {}, argument {}, {}".format(f.func_name,f_args[i],self._argList[i].errorString()))
                            else:
                                raise TypeError("Got invalid type for function '" + f.func_name + "' argument : '" +  f_args[i] + "' got " + str(type(args[i])) + " instead of " + str(self._argList[i]))
                    else:
                        try:
                            name = f_args[i]
                            if name in self._argDict:
                                if not isinstance(args[i],self._argDict[name]):
                                    if isinstance(self._argDict[name],Constraint):
                                        raise TypeError("Constraint mismatch for function {}, argument {}, {}".format(f.func_name,name,self._argDict[name].errorString()))
                                    else:
                                        raise TypeError("Got invalid type for function '" + f.func_name + "' argument : '" + name+ "' got " + str(type(args[i])) + " instead of " + str(self._argDict[name]))
                            else:
                                raise TypeError("No type check existing for argument " + name + " of " + f.func_name)
                        except IndexError:
                            raise TypeError("Too many arguments for function " + f.func_name)
                for (k,v) in kargs:
                    if k in self._argDict:
                        if not isinstance(v,self._argDict[k]):
                            if isinstance(self._argDict[k],Constraint):
                                raise TypeError("Constraint mismatch for function {}, argument {}, {}".format(f.func_name,k,self._argDict[k].errorString()))
                            else:
                                raise TypeError("Got invalid type for function '" + f.func_name + "' argument: '" + k + "' got " + str(type(v)) + " instead of " + str(self._argDict[k]))
                    else:
                        try:
                            ind = f_args.index(k)
                            try:
                                if not isinstance(v,self._argList[ind]):
                                    if isinstance(self._argList[ind],Constraint):
                                        raise TypeError("Constraint mismatch for function {}, argument {}, {}".format(f.func_name,k,self._argList[ind].errorString()))
                                    else:
                                        raise TypeError("Got invalid type for function '" + f.func_name + "' argument: '" + k + "' got " + str(type(k)) + " instead of " + str(self._argList[ind]))
                            except:
                                raise TypeError("No type-check available for argument " + k + " of function " + f.func_name)
                        except:
                            raise TypeError("No such argument: " + k + " for function " + f.func_name)
                return f(*args,**kargs)
            return checked_f
        else:
            return f
