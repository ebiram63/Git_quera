"""
def f(n):
    yield n//1
    yield n//2
    yield n//3

div = f(6)
print(type(div))
print(div)
print(list(div))

answers is 

<class 'generator'>
<generator object f at 0x7f6254849a40>
[6, 3, 2]
"""
import sys


def myRange(n):
    for i in range(n):
        yield i


print(sys.getsizeof(myRange(1000)))
print(sys.getsizeof(myRange(1000_000)))
print(sys.getsizeof(myRange(1000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000_000_000_000_000_000)))
print(sys.getsizeof(myRange(1000_000_000_000_000_000_000_000_000_000_000_000)))