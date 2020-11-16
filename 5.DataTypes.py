"""
Text type : str

numeric types: int, float, complex

sequence types: list, tuple, range

Mapping types: dict

set types: set, frozenset

Boolean type: bool

Binary types: bytes, bytearray, memoryview
"""

x = 5 #int int(20)
print(type(x))

y = "Hello world" #str str("Hello World")
print(type(y))

z = 220.5 #float float(20.5)
print(type(z))

a = 1j #complex complex(1j)
print(type(a))

b = ["apple", "banana", "cherry"]#list list(("apple, "banana", "cherry"))
print(type(b))

c = ("apple","banana", "tomato")#tuple tuple(("apple", "banana", "cherry"))
print(type(c))

d = range(6)#range
print(type(d))

e = {"name":"John", "age": 36}#dict dict(name = "john", age = 36)
print(type(e))

f = {"apple", "banana", "cherry"}#set set(("apple", "banana", "cherry"))
print(type(f))

g = frozenset({"apple","banana","cherry"})#frozenset frozenset(("apple", "banana", "cherry"))
print(type(g))

h = True #bool bool(5)
print(type(h))

i = b"hello" #bytes bytes(5) set(("apple", "banana", "cherry"))
print(type(i))

j = bytearray(5) #bytearray
print(type(j))

k = memoryview(bytes(5)) #memoryview
print(type(k))
