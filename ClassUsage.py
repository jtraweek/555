# import the class
from Individual import Individual

# create a new instance
ind = Individual()

# calling attributes before setting values
print('First test:')
print(ind.name)
print(ind.sex)
print(ind.birt)
print(ind.deat)
print(ind.spouse)
print(ind.spouse_str)
print(ind.child)

# set values
# the normal setter will replace the built-in attributes with the given object
print('Second test:')
ind.name = 'test'
ind.sex = 'test'
ind.birt = 'test'
ind.deat = 'test'
ind.child = 'test'
print(ind.name)
print(ind.sex)
print(ind.birt)
print(ind.deat)

print(ind.child)

# IMPORTANT
# note that the list attributes have different implementation of setter
# list setter will only append the given object to the list attributes
# call normal getter to get the list object
# and call _str getter to get the string version of the list
print('Third test:')
ind.spouse = 'test1'
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
