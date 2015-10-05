from Constraint import Constraint

def require(rtype,func):
    return Constraint(lambda x: isinstance(x,rtype) and func(x))
 
