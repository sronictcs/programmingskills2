#a_bicycles.py

##Using Lists to store data of the same type##

#a list is made up of a list name and an = then [ and the items in speech marks like below
bicycles = ["trek", "cannondale", "redline", "specialized"]

#to print a list use the print function and the name of the list
print (bicycles)


#To print 1 element of a list put the position of the item you want in [brackets]
#remember list indexes start at 0, 1, 2, etc
#returns 1 element
print (bicycles[0])

#You can use string methods like title case to list elements too
print(bicycles[0].title())


#To return the last element of a list print the item at position -1
print(bicycles[-1])

'''2-1. Names: Store the names of a few of your friends in a list
called names.
Print each person’s name by accessing each element in the list,
one at a time.'''
#write your code here


#use f-string to make a message variable and print
message = f"my first bicycle was a {bicycles[0].title()}."

print(message)

'''2-2. Greetings: Start with the list you used in Exercise 2-1,
but instead of
just printing each person’s name, print a message to them.
The text of each message should be the same, but each message
should
be personalized with the person’s name.
'''
#write your code here
