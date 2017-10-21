# import the class
from Individual import Individual

# create a new instance
ind = Individual()

# calling attributes before setting values
print('First test:')
print(ind.name)
print(ind.sex)
print(ind.child)
print(ind.birt)
print(ind.birt_str)
print(ind.deat)
print(ind.spouse)
print(ind.spouse_str)

# set values
# the normal setter will replace the built-in attributes with the given object
print('Second test:')
ind.name = 'test'
ind.sex = 'test'
ind.birt = '1 JAN 1820'
ind.deat = '1 JAN 1830'
ind.child = 'test'
print(ind.name)
print(ind.sex)
print(ind.child)
# note that the date attribute has two getters
# default getter will return a datetime object
# _str getter will return a format date string
print(ind.birt)
print(ind.birt_str)
print(ind.deat)
print(ind.deat_str)
# two built-in additional attribute that based on computation
print(ind.age)
print(ind.alive)

# IMPORTANT
# note that the list attributes have different implementation of setter
# list setter will only append the given object to the list attributes
print('Third test:')
ind.spouse = 'test1'
# the list attributes also have two getters
# normal getter will return list object
# _str getter will return a string version of the list
print(ind.spouse)
print(ind.spouse_str)
ind.spouse = 'test2'
print(ind.spouse)
print(ind.spouse_str)

# list attributes have a deleter
print('Fourth test:')
del ind.spouse
print(ind.spouse)
print(ind.spouse_str)
