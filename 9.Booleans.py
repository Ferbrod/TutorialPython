print(10 > 9)
print(10 == 9)
print(10 < 9) #When you compare two values python evaluates the expression and returns the boolean answer

a = 200
b = 33
#Printing a string depending on one condition
if b > a:
    print("B is greater than a")
else:
    print("B is not greater than a")

#the bool() function allows you to evaluate any given value and returns an answer

print(bool("hello"))
print(bool(15))

#You can also evaluate two variables
x = "Hello"
y = 14

print(bool(x))
print(bool(y))

#This values retrun false

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))

class myClass():
    def __len__(self):
     return 0

myobj = myClass()
print(bool(myobj))

#Print the answer of a function

def myFunction():
    return True

print(myFunction())

#Print something based on the answer from the function

if myFunction():
    print("Yes")
else:
    print("No")


#there are also built-in functions that returns a boolean value

x = 200
print(isinstance(x, int)) #isinstance comparates if the variable x is an interger or not, it can compare any data type
