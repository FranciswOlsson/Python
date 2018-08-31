import random
import sys
import os

print("Hello World")

name = "Frank"
print(name)

#Arithmatic operators
print("5+2=",5+2)
print("5-2",5-2)
print("5*2=",5*2)
print("5/2=",5/2)
print("5%2=",5%2)
print("5**2=",5**2)
print("5//2=",5//2)

#Strings
quote = "\"Backslash includes quote"

multi_line_quote = '''this is a multi
line quote"'''

print("%s %s %s" %('quote like this', quote, multi_line_quote))

print('\n'*3)

print("I don't like ", end="")
print("newlines")

#Lists
grocery_list = ['Juice', 'Tomatoes', 'Milk']
print('First Item', grocery_list[0])
grocery_list[0]="Green Juice"
print("First Item",grocery_list[0])
print(grocery_list[1:3])
other_events=['Wash Car', 'Pick Up Kids',
              'Cash Check']
to_do_list = [other_events,grocery_list]
print(to_do_list)
print(to_do_list[1][1])

grocery_list.append("Onions")
print(to_do_list)

grocery_list.insert(1, "Pickle")

grocery_list.remove("Pickle")

grocery_list.sort()
grocery_list.reverse()

del grocery_list[3]
print(to_do_list)

to_do_list_2=other_events+grocery_list

print(len(to_do_list_2))
print(max(to_do_list_2))
print(min(to_do_list_2))

#Tuples
pi_tuple=(3,1,4,1,5,9)
new_tuple=list(pi_tuple)
new_list=tuple(new_tuple)

len(tuple)
min(tuple)
max(tuple)

#Dictionaries
super_villains={'Fiddler':'Isaac Brown',
                'Captain Cold': 'Leonard Snart',
                'Weather Wizard': 'Mark Mardon',
                'Mirror Wizard': 'Sam Scudder',
                'Pied Piper': 'Thomas Peterson'}

print(super_villains['Captain Cold'])
del super_villains['Fiddler']
super_villains['Pied Piper']= 'Hartley Rathaway'
print(len(super_villains))
print(super_villains)


