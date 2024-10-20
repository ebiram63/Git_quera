"""
def f(a, L=[]):
     L.append(a)
     return L
 
 f(1)
[1]
 f(2)
[1, 2]
 f(3)
[1, 2, 3]
"""
"""
>>> def f(a, L=None):
...     if L == None:
...         L = []
...     L.append(a)
...     return L
... 
>>> f(1)
[1]
>>> f(2)
[2]
>>> f(2,f(1))
[1, 2]
"""
"""
for adding diverse inputs to a definatiuon 
>>> def f(a, *args):
...     return args
... 
>>> f(2)
()
>>> f(2, 1)
(1,)
>>> f(1, 2, 3)
(2, 3)
"""
"""
>>> def f(*args, **kwargs):
...     print(args)
...     print(kwargs)
... 
>>> f(a=2)
()
{'a': 2}
>>> f(1, a=2)
(1,)
{'a': 2}
>>> f(1, a=2, 2)
  File "<stdin>", line 1
    f(1, a=2, 2)
               ^
SyntaxError: positional argument follows keyword argument
"""
"""
>>> def print_users(**users):
...     for name, age in users.items():
...         print(f"{name} is {age} years old.")
...
>>> print_users(Ali=21, Mamadreza=18, Mahdi=22)
'Ali is 21 years old.'
'Mamadreza is 18 years old.'
'Mahdi is 22 years old.'
"""
"""
>>> print(*[1, 2, 3])
1 2 3
>>> print(*(1, 2, 3))
1 2 3
>>> print(*{'a': 1, 'b': 2, 'c': 3})
a b c
"""
"""
>>> def mean(*numbers):
...     return sum(numbers)/len(numbers)
...
>>> data = [1, 2, 3, 4, 5]
>>> mean(*data)
3.0
"""
"""
>>> def print_people(**people):
...     for name, job in people.items():
...         print(f'{name} is a {job}.')
...
>>> data = {'Mohammad': 'teacher', 'Samad': 'worker'}
>>> print_people(**data)
'Mohammad is a teacher.'
'Samad is a worker.'
"""
"""
lambda argumets : expression
"""
"""
>>> (lambda x: x * x)(2)
4
>>> power_two = lambda x: x * x
>>> power_two(2)
4
>>> average = lambda a, b: (a + b) / 2
>>> average(20, 18)
19.0
>>> statistic = lambda a, b: [(a + b) / 2, max(a, b)]
>>> statistic(20, 18)
[19.0, 20]
"""
"""
>>> mylist = [(1,3),(4,5),(2,10),(9,6)]

>>> mylist.sort()
>>> mylist
[(1, 3), (2, 10), (4, 5), (9, 6)]

>>> mylist.sort(key = lambda x: x[-1])
>>> mylist
[(1, 3), (4, 5), (9, 6), (2, 10)]
"""
"""
>>> def myfunc(n):
          return lambda a : a * n

>>> mydoubler = myfunc(2)
>>> mytripler = myfunc(3)
>>> 
>>> mydoubler(11)
22
>>> mytripler(11)
33
"""