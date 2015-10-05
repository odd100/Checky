# Checky

Welcome to Checky's repository.
Checky is an open source python library that aims to sort of type-check your program to make easier debugging and less error prone code.
The library can be extended further by adding more useful constraints and mechanisms to check correcness of code.
The library adds major overhead for the checking mechanism, therefore it is extremely recommended to pass python the optimization flag (-O) in order to cancel the checking mechanism. 

## Example uses:
```
from checky.TypeCheck import TypeCheck

@TypeCheck(str)
def greet(name):
  print "Hello, %s! Have a nice day" % name
```
results in exception provided with non string parameter.

```
from checky.TypeCheck import TypeCheck
from checky.CommonConstraints import CMethod

@TypeCheck(CMethod("next"),object)
def safeIterate(iterator,callback):
  try:
    while True:
      callback(iterator.next())
  except StopIteration:
    pass
    
@TypeCheck(value=int)
def printPlusOne(value):
  print str(value+1)
  
@TypeCheck(CMethod("__iter__"))
def plusOne(intContainer):
  safeIterate(iter(intContainer),printPlusOne)
```

running `plusOne(xrange(1,10))` will result in printing the numbers from 2 to 10 while running `plusOne("Hello")` will result in TypeError:
> TypeError: Constraint mismatch for function plusOne, argument intContainer, Value has no method named `__iter__`

note that Constraints are also composable:

```
iterator_constraint = CMethod("__iter__") + CMethod("next")

def getSetConstraint(attrName):
  return CMethod("get" + attrName) and CMethod("set" + attrName)
  
hasAge = CAttribute("age",int) + CAttribute("age",float)

```
operators +/and, -, or ,xor and etc.. can be used on constraints..
Futhermore, there are also "Container constraints:"
```
has_getset_age = CAttribute("age")
has_getset_age *= CMethod("get",0) + CMethod("set",1)
```
this constraint will require object with age attribute that has get and set method(get without parameters and set with one)

Note: there is also CStaticMethod for static methods.
Please report any problem you face using this library

**This library has been tested on linux machine with python 2.7, but it should work on any python bigger than 2.4(allowing decorators and inspect)**
