thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist)) #this allows you to know the length of the thislist

#lists can have any data type inside them

list1 = ["apple", "Banana", "Cherry"]
lsit2 = [1, 5, 7, 9, 3]
lsit3 = [True, False, False]

#lists can also contain different data type

list4 = ["abc", 34, True, 40, "male"]

print(type(thislist))

#you can also use the list constructor

newlist = list(("apple", "banana", "cherry")) #Note the double round brackets
print(newlist)

"""

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

"""

print(thislist[1]) #accesing to the second item of the list

print(thislist[-1]) #in negative values -1 refers to the last itme, -2 to the second last itme and so on

fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruitlist[2:5]) #the result will be a new list conformed by the range of values, being 2 the beggining and 5 the last one but notice that is not included

print(fruitlist[:4]) #if you leave out the first value, the range will go to the beggining of the list

print(fruitlist[2:]) #exactly like the last example but this time will go to the end instead of the beggining

#you can also use negative values, if you want to search from end of the list

#check if something is in a list or not

if "apple" in fruitlist:
    print("Yes, 'apple' is in the fruit list")

#another example

if "tomato" not in fruitlist:
    print("No, 'tomato' is not on the fruit list")
