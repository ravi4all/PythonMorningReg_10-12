Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> a = 12
>>> math.sqrt(a)
3.4641016151377544
>>> math.pow(a,4)
20736.0
>>> a = 12.4
>>> round(a)
12
>>> math.floor(a)
12
>>> math.ceil(a)
13
>>> a = -5
>>> abs(a)
5
>>> math.isnan(a)
False
>>> a = "Hello"
>>> math.isnan(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    math.isnan(a)
TypeError: must be real number, not str
>>> 
