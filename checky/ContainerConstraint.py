from TypeCheck import TypeCheck
from Constraint import Constraint

class ContainerConstraint(Constraint):

    def __init__(self,func):
        super(ContainerConstraint,self).__init__(func)
        self._subconstraint = None

    def _getContainedValue(self,x):
        raise NotImplementedError("Non-implemented Container Constraint")

    def __mul__(self,other):
        self._subconstraint = other

    def __str__(self):
        return "Simple container constraint"

    def errorString(self):
        if self._subconstraint == None:
            return "Value did not match constraint {}".format(self._func)
        else:
            return "Value did not match constraint {} with sub-constraint {}".format(self._func,self._subconstraint)

    def __instancecheck__(self,other):
        if not self._check(other):
            return False
        elif self._subconstraint != None:
            return isinstance(self._getContainedValue(other),self._subconstraint)
        else:
            return True
 
