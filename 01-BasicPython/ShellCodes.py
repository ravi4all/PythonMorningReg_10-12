Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> c = a+b
>>> print(c)
30
>>> a = "Hello"
>>> b = "World"
>>> c = a+b
>>> print(c)
HelloWorld
>>> 10+20
30
>>> a = 10
>>> b = 20
>>> print(a+b)
30
>>> print(a-b)
-10
>>> print(a*b)
200
>>> print(a/b)
0.5
>>> a = 11
>>> if a/2 == 0:
	print("Even Number")
else:
	print("Odd Number")

Odd Number
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/01-PythonSyntax.py 
Odd Number
>>> a = "Hello"
>>> print(a*5)
HelloHelloHelloHelloHello
>>> type(a)
<class 'str'>
>>> a = 12
>>> type(a)
<class 'int'>
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> a = "10"
>>> b = 10
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a+b)
TypeError: must be str, not int
>>> int(a) + b
20
>>> a = 15
>>> b = 12
>>> a/b
1.25
>>> a//b
1
>>> a * a
225
>>> a * a * a
3375
>>> a ** 5
759375
>>> a*a*a*a*a
759375
>>> a == b
False
>>> b = 15
>>> a == b
True
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/02-BasicCalculator.py 
Basic Calculator
22
-2
0.8333333333333334
120
0
1000
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/02-BasicCalculator.py 
Basic Calculator
22
-2
0.8333333333333334
120
0
1000
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/03-TakingInput.py 
Enter first number : 10
Enter second number : 12
1012
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/03-TakingInput.py 
Enter first number : 12
Enter second number : 22
34
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/03-TakingInput.py 
Enter first number : 12
Enter second number : 11
23
Odd Number
>>> import pyamg
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    import pyamg
ModuleNotFoundError: No module named 'pyamg'
>>> a = 30
>>> print("Area of rectange is"a)
SyntaxError: invalid syntax
>>> print("Area of rectange is",a)
Area of rectange is 30
>>> a,b = 10,12
>>> a = 10,12
>>> a
(10, 12)
>>> type(a)
<class 'tuple'>
>>> a,b = 10
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a,b = 10
TypeError: 'int' object is not iterable
>>> a,b = 10,12
>>> a,b = b,a
>>> print(a,b)
12 10
>>> print("Hello World, Welcome to "Python"")
SyntaxError: invalid syntax
>>> print('Hello World, Welcome to "Python"')
Hello World, Welcome to "Python"
>>> print("Hello /n World")
Hello /n World
>>> print("Hello \n World")
Hello 
 World
>>> print(r"Hello \n World")
Hello \n World
>>> print("Hello \t World")
Hello 	 World
>>> print("My name is 'Ravi'")
My name is 'Ravi'
>>> print(r"My name is "Ravi"")
SyntaxError: invalid syntax
>>> print('My name is "Ravi"')
My name is "Ravi"
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
>>> a = "Hello"
>>> a[1]
'e'
>>> a[0]
'H'
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> a[4]
'o'
>>> a[0:2]
'He'
>>> a[0:4]
'Hell'
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello 
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
ython
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Pytho
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
12
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
>>> a = "hello"
>>> a.capitalize
<built-in method capitalize of str object at 0x0295F7E0>
>>> a.capitalize()
'Hello'
>>> a.upper()
'HELLO'
>>> a.lower()
'hello'
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
HELLO PYTHON
hello python
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
HELLO PYTHON
hello python
Hello PythonProgramming
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
HELLO PYTHON
hello python
Hello Python Programming
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
HELLO PYTHON
hello python
Hello Python Programming
PHello PythonrHello PythonoHello PythongHello PythonrHello PythonaHello PythonmHello PythonmHello PythoniHello PythonnHello Pythong
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
HELLO PYTHON
hello python
Hello Python Programming
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello Python
Hello
Hello Python
Hello P
Python
n
nohtyP olleH
Hello Pytho
Length is 12
Hello python
HELLO PYTHON
hello python
Hello Python Programming
['Hello Python']
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/04-StringManipulations.py 
Hello, Python
Hello
Hello, Python
Hello, 
 Pytho
n
nohtyP ,olleH
Hello, Pytho
Length is 13
Hello, python
HELLO, PYTHON
hello, python
Hello, Python Programming
['Hello', ' Python']
>>> 
