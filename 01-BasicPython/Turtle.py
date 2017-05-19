Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> john = turtle.shape()
>>> john.forward(100)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    john.forward(100)
AttributeError: 'str' object has no attribute 'forward'
>>> john = turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.right(45)
>>> turtle.forward(200)
>>> turtle.right(45)
>>> turtle.right(45)
>>> turtle.right(90)
>>> turtle.right(-45)
>>> turtle.forward(500)
>>> turtle.reset()
>>> for i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10):
	print(i)

0
1
2
3
4
5
6
7
8
9
>>> for i in range(4):
	turtle.forward(200)
	turtle.left(90)

>>> for i in range(11):
	print(i*2)

0
2
4
6
8
10
12
14
16
18
20
>>> for i in range(1,11):
	print(i*2)

2
4
6
8
10
12
14
16
18
20
>>> for i in range(11,21):
	print(i*2)

22
24
26
28
30
32
34
36
38
40
>>> turtle.reset()
>>> for i in range(10):
	turtle.forward(i*10)
	turtle.left(90)

>>> for i in range(50):
	turtle.forward(i*10)
	turtle.left(90)

>>> turtle.color('red')
>>> turtle.reset()
>>> turtle.width(10)
>>> turtle.width(100)
>>> turtle.width('10')
>>> turtle.circle(100)
>>> turtle.width('1')
>>> turtle.circle(100)
>>> turtle.reset()
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.circle(100)
>>> turtle.left(-90)
>>> turtle.circle(100)
>>> turtle.left(90)
>>> turtle.left(180)
>>> turtle.circle(100)
>>> turtle.left(90)
>>> turtle.left(90)
>>> turtle.left(90)
>>> turtle.circle(100)
>>> turtle.reset()
>>> for i in range(30):
	turtle.circle(i*10)
	turtle.left(90)

Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    turtle.circle(i*10)
  File "<string>", line 8, in circle
  File "C:\Python36-32\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Python36-32\lib\turtle.py", line 3179, in _goto
    self._update()
  File "C:\Python36-32\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python36-32\lib\turtle.py", line 562, in _update
    self.cv.update()
  File "C:\Python36-32\lib\tkinter\__init__.py", line 1171, in update
    self.tk.call('update')
KeyboardInterrupt
>>> turtle.reset()
>>> 
