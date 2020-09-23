#c_animals.py

#here's another list
animals = ["kingfisher", "heron", "capuchin", "stork", "prairie dog", "hummingbird", "deer", "owl"]
print(animals)

#to remove an item from a list completely use del
del animals[4]
print(animals)

#To sort a list 
#sort alphabetical
animals.sort()
print (animals)

#sort reverse alphabetical
animals.sort(reverse=True)
print (animals)

#using sorted to display sorted, but it does not store the orginal list sorted
animals = ["kingfisher", "heron", "capuchin", "stork", "prairie dog", "hummingbird", "deer", "owl"]
print(animals)
print(sorted(animals))
print(animals)




#print reverse list (no sorting, permanent change-apply reverse
#again to get original order)
animals.reverse()
print(animals)

#length of list i.e. the number of items in a list
print(len(animals))


'''2-7. Seeing the World: Think of at least five places in the
world you’d like to visit.
•	Store the locations in a list.
Make sure the list is not in alphabetical order.
•	Print your list in its original order. Don’t worry
about printing the list neatly, just print it as a raw Python
list.
•	Use sorted() to print your list in alphabetical order
without modifying the actual list.
•	Show that your list is still in its original order by
printing it.
•	Use sorted() to print your list in reverse alphabetical
order without changing the order of the original list.
•	Show that your list is still in its original order by
printing it again.
•	Use reverse() to change the order of your list.
Print the list to show that its order has changed.
•	Use reverse() to change the order of your list again.
Print the list to show it’s back to its original order.
•	Use sort() to change your list so it’s stored in
alphabetical order. Print the list to show that its order
has been changed.
•	Use sort() to change your list so it’s stored in
reverse alphabetical order. Print the list to show that
its order has changed.
'''

