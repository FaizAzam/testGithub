#    Creating a list using Constructor

colors = list(("White", "Black", "Silver", "Green"))

#    Adding an element at the end of the list using append() method
colors.append("Blue")
print(colors)

#   Sorting list elements using sort() method
colors.sort()
print(colors)

#   Reverse list items using reverse() method
colors.reverse()
print(colors)

#    Reverse list items while sorting them
colors.append("Pink")
print(colors)
colors.sort(reverse=False)
print(colors)

#    remove() function removes a specific value from the list
colors.remove("Black")
print(colors)

#   pop() function removes an element at the specified position
#   the pop() method returns the removed value
#   if no index is mentioned pop() will remove last item from the list at index -1
print(colors.pop())
print(colors)
colors.pop(2)
print(colors)

#   inserting an element at specified position
colors.insert(1, "White")
print(colors)

#   the index() method returns the index/position of the element
#   it returns the first occurrence in case of duplicate values
print(colors.index("Silver"))

#   combining two lists using extend() method
#   extend() method accept any iterable (list, set, tuple, etc.) as a parameter
fruit = ["Apple", "Orange", "Grapes"]
colors.extend(fruit)
print(colors)

#   count() is used to count the number of times a value/element exists in a list
c = colors.count("White")
print("White exists ", c, " times")
c = colors.count("Black")
print("Black exists ", c, " times")

#   The copy() method returns a copy of the specified list
f = fruit.copy()
print(f)

#   clear() method removes all the elements from the list
f.clear()
print(f)
