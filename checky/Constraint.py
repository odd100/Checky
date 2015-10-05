class Constraint(object):

    def __init__(self,checkFunction):
        self._check = checkFunction

    def __instancecheck__(self,other):
        return self._check(other)

    def __str__(self):
        return "Simple function-constraint"

    def errorString(self):
        return "Value did not match " + str(self._check)

    def __or__(self,other):
        return Constraint(lambda x: isinstance(x,self) or isinstance(x,other))

    def __and__(self,other):
        return Constraint(lambda x: isinstance(x,self) and isinstance(x,other))

    def __xor__(self,other):
        return Constraint(lambda x: isinstance(x,self) ^ isinstance(x,other))

    def __ior__(self,other):
        currentCheck = self._check
        self._check = lambda x: currentCheck(x) or isinstance(x,other)
        return self

    def __iand__(self,other):
        currentCheck = self._check
        self._check = lambda x: currentCheck(x) and isinstance(x,other)
        return self

    def __ixor__(self,other):
        currentCheck = self._check
        self._check = lambda x: currentCheck(x) ^ isinstance(x,other)
        return self

    def __add__(self,other):
        return (self or other) 

    def __sub__(self,other):
        return Constraint(lambda x: isinstance(x,self) and not isinstance(x,other))

    def __iadd__(self,other):
        currentCheck = self._check
        self._check = lambda x: currentCheck(x) and isinstance(x,other)
        return self

    def __isub__(self,other):
        currentCheck = self._check
        self._check = lambda x: currentCheck(x) and not isinstance(x,other)
        return self
