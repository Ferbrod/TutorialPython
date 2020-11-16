#"Hello" = 'hello'
print("Hello")
print('hello')

a = "Hello" #assigning a string to a variable
print(a)

#Multiline string

b = """Sometimes you will need to use
a multline string and for that
you'll have to use three double quotes"""
print(b)

c = '''Sometimes you will need to use
a multline string and for that
you'll have to use three double quotes
or you can also use three single quotes'''

print(c)

#Strings are arrays

a = "Hello World"
print(a[1]) #get the character at position 1

print(a[2:5]) #this is to slice the world getting characters from position 2 to 5, not including this last one

print(a[-5:-2]) #also slicing but when you use negative numbers you count backwards, starting in the end of the string

print(len(a)) #this is to get the length of a string

#Methods fot strings built-in python

a = " Hello, World! "
print(a.strip()) #This returns "Hello, World!" without the spaces in the beggining and the end

print(a.lower()) #this returns the string in lower case

print(a.upper()) #this returns the string in upper case

print(a.replace("H", "I"))  #this replaces the string with another one

print(a.split("W")) #returns the string splitted if it founds the instance separator, in this case it returns ['Hello', 'World!']

#Check Strings

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) #in or not in ar booleans used to know if a certain prhase or character is present in a strings

y = "ain" not in txt
print(y)

#Concatenate

a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b #this to add a space
print(c)

age = 36
txt = "My name is jhon, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars" #this for merge numbers with strings without the need of converting them
print(myorder.format(quantity, itemno, price))

Myorder = "I want {2} pieces of item {1} for {0} dollars" #if you use numbers you'll make sure the values are putted in the correct order
print(Myorder.format(quantity, itemno, price))


txt = 'We are the so-called \'Vikings\' from the north'
print(txt) #this is used when you want to put double quotes or single quoutes inside of a string that uses them

txt = "\x48\x65\x6c\x6c\x6f" #transforms hex number into a strings
print(txt)

txt = "\110\145\154\154\157" #transforms octal values to string, it is a backslash followed ny 3 numbers
print(txt)

#Both last examples mean hello
