x =  "awesome"
print("Python is " + x)

y = "Python is "

z = y + x
print(z)

d = "3"
e = "2"

print(d + e)
h = "great"

def myFunc():
    global h
    h = "fantastic"
    print("two is lower than " + h)

myFunc()

print("Python is " + h)
#Solo se pueden concatenar (unir) dos variables del mismo tipo, ya sea str o int
