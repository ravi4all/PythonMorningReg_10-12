Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,'Hi',10.5,'Hello',True]
>>> print(a)
[1, 2, 'Hi', 10.5, 'Hello', True]
>>> a[0]
1
>>> a[3]
10.5
>>> a[-1]
True
>>> a[:-1]
[1, 2, 'Hi', 10.5, 'Hello']
>>> a[::-1]
[True, 'Hello', 10.5, 'Hi', 2, 1]
>>> len(a)
6
>>> a = []
>>> a.append(1)
>>> a
[1]
>>> a.append(2)
>>> a
[1, 2]
>>> a.append('Hi')
>>> a
[1, 2, 'Hi']
>>> a.append(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append(1,2,3,4)
TypeError: append() takes exactly one argument (4 given)
>>> a.append([1,2,3,4])
>>> a
[1, 2, 'Hi', [1, 2, 3, 4]]
>>> a.pop()
[1, 2, 3, 4]
>>> a
[1, 2, 'Hi']
>>> a.pop()
'Hi'
>>> a
[1, 2]
>>> a.insert(2,'Hello')
>>> a
[1, 2, 'Hello']
>>> a.insert(0,10)
>>> A
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> a
[10, 1, 2, 'Hello']
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
>>> a.remove(10)
>>> a
[1, 2, 'Hello']
>>> a.extend(9,8,7,6,5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.extend(9,8,7,6,5)
TypeError: extend() takes exactly one argument (5 given)
>>> a.extend([9,8,7,6])
>>> a
[1, 2, 'Hello', 9, 8, 7, 6]
>>> a = [1,2,3,4,5]
>>> b = [6,7,8,9,10]
>>> a + b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.reverse()
>>> a
[5, 4, 3, 2, 1]
>>> a.index(10)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.index(10)
ValueError: 10 is not in list
>>> a.index(9)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.index(9)
ValueError: 9 is not in list
>>> a.index(5)
0
>>> a
[5, 4, 3, 2, 1]
>>> del(a[3])
>>> a
[5, 4, 3, 1]
>>> a = [4,5,32,1,45,22,11,7,8,9]
>>> a.sort()
>>> a
[1, 4, 5, 7, 8, 9, 11, 22, 32, 45]
>>> a.sort(reversed = True)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.sort(reversed = True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> a.sort(reverse = True)
>>> a
[45, 32, 22, 11, 9, 8, 7, 5, 4, 1]
>>> type(a)
<class 'list'>
>>> for i in a:
	print(i)

45
32
22
11
9
8
7
5
4
1
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/07-ForLoop.py 
1
2
3
4
5
6
7
8
9
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/07-ForLoop.py 
1
2
3
4
5
6
7
8
9
H
e
l
l
o
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/07-ForLoop.py 
Value is 1
Value is 2
Value is 3
Value is 4
Value is 5
Value is 6
Value is 7
Value is 8
Value is 9
H
e
l
l
o
>>> 
 RESTART: E:/Python/Python_Batches/PythonMorningReg_10-12/01-BasicPython/07-ForLoop.py 
1 is the value
2 is the value
3 is the value
4 is the value
5 is the value
6 is the value
7 is the value
8 is the value
9 is the value
H
e
l
l
o
>>> 
