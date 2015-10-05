def internal__check__if__builtin(func):
    rep = str(func)
    return (rep.rfind("bound method") == -1 and rep.rfind("function") == -1)

def internal__is__function(obj):
    return '__call__' in dir(obj)

def internal__has__function(obj,funcname):
    return funcname in dir(obj) and internal__is__function(obj.__getattribute__(funcname))

def internal__num__args(nonbuiltinfunc):
    return nonbuiltinfunc.func_code.co_argcount 
