# DADataType.py

from docassemble.base.util import DAObject
import docassemble.base.util
import re

__all__ = ['DADTBoolean', 'DADTContinue', 'DADTNumber', 'DADTString', 'DADTEmail', 'DADTDate', 'DADTTime', 'DADTDateTime', 'DADTYesNoMaybe', 'DADTFile', 'DADTEnum', 'DADTObjectRef']

# Generally speaking, "of" is a better default preposition than "in" in English,
# so we modify the 'a_in_the_b' language function for english to use "of" instead.


def a_of_the_b(a, b, **kwargs):
  return str(a) + " of the " + str(b)

docassemble.base.util.update_language_function('en', 'a_in_the_b', a_of_the_b)


# This is the root type for the package from which all the other types are derived.

class DADataType(DAObject):
    def init(self, input_type="default", *pargs, **kwargs):
      self.intput_type = input_type
      super().init(*pargs, **kwargs)
    def __str__(self):
        return str(self.value)
    def __dir__(self):
        return dir(self.value)
    def __contains__(self, item):
        return self.value.__contains__(item)
    def __iter__(self):
        return self.value.__iter__()
    def __len__(self):
        return len(self.value)
    def __reversed__(self):
        return reversed(self.value)
    def __getitem__(self, index):
        return self.value.__getitem__(index)
    def __repr__(self):
        return repr(self.value)
    def __add__(self, other):
        return self.value.__add__(other)
    def __sub__(self, other):
        return self.value.__sub__(other)
    def __mul__(self, other):
        return self.value.__mul__(other)
    def __floordiv__(self, other):
        return self.value.__floordiv__(other)
    def __mod__(self, other):
        return self.value.__mod__(other)
    def __divmod__(self, other):
        return self.value.__divmod__(other)
    def __pow__(self, other):
        return self.value.__pow__(other)
    def __lshift__(self, other):
        return self.value.__lshift__(other)
    def __rshift__(self, other):
        return self.value.__rshift__(other)
    def __and__(self, other):
        return self.value.__and__(other)
    def __xor__(self, other):
        return self.value.__xor__(other)
    def __or__(self, other):
        return self.value.__or__(other)
    def __div__(self, other):
        return self.value.__div__(other)
    def __truediv__(self, other):
        return self.value.__truediv__(other)
    def __radd__(self, other):
        return self.value.__radd__(other)
    def __rsub__(self, other):
        return self.value.__rsub__(other)
    def __rmul__(self, other):
        return self.value.__rmul__(other)
    def __rdiv__(self, other):
        return self.value.__rdiv__(other)
    def __rtruediv__(self, other):
        return self.value.__rtruediv__(other)
    def __rfloordiv__(self, other):
        return self.value.__rfloordiv__(other)
    def __rmod__(self, other):
        return self.value.__rmod__(other)
    def __rdivmod__(self, other):
        return self.value.__rdivmod__(other)
    def __rpow__(self, other):
        return self.value.__rpow__(other)
    def __rlshift__(self, other):
        return self.value.__rlshift__(other)
    def __rrshift__(self, other):
        return self.value.__rrshift__(other)
    def __rand__(self, other):
        return self.value.__rand__(other)
    def __ror__(self, other):
        return self.value.__ror__(other)
    def __neg__(self):
        return self.value.__neg__()
    def __pos__(self):
        return self.value.__pos__()
    def __abs__(self):
        return abs(self.value)
    def __invert__(self):
        return self.value.__invert__()
    def __complex__(self):
        return complex(self.value)
    def __int__(self):
        return int(self.value)
    def __long__(self):
        return long(self.value)
    def __float__(self):
        return float(self.value)
    def __oct__(self):
        return self.octal_value
    def __hex__(self):
        return hex(self.value)
    def __index__(self):
        return self.value.__index__()
    def __le__(self, other):
        return self.value.__le__(other)
    def __ge__(self, other):
        return self.value.__ge__(other)
    def __gt__(self, other):
        return self.value.__gt__(other)
    def __lt__(self, other):
        return self.value.__lt__(other)
    def __eq__(self, other):
        return self.value.__eq__(other)
    def __ne__(self, other):
        return self.value.__ne__(other)
    def __hash__(self):
        return hash(self.value)
    def __bool__(self):
        return bool(self.value)
      
class DADTBoolean(DADataType):
  #TODO Add validation for input types.
  pass

class DADTContinue(DADataType):
  pass

class DADTNumber(DADataType):
  pass

class DADTString(DADataType):
  pass

class DADTEmail(DADataType):
  pass

class DADTDate(DADataType):
  pass

class DADTTime(DADataType):
  pass

class DADTDateTime(DADataType):
  pass

class DADTYesNoMaybe(DADataType):
  pass

class DADTFile(DADataType):
  pass

class DADTEnum(DADataType):
  pass

class DADTObjectRef(DADataType):
  pass