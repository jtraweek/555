"""
File addresses all outputs for Sprint 4
"""
import  GedcomClass
from Sprint4 import US_31
from Sprint4 import US_41

file1 = open('./test_ged/user_story_31_test.ged', 'r')
file2 = open('./test_ged/user_story_31_test_2.ged', 'r')
individuals = GedcomClass.read_individuals(file1)
individuals = GedcomClass.read_individuals(file2)
families = GedcomClass.read_families(file)


print('\n Test user story 31 No Living Singles:')
GedcomClass.main(file2)
if len(US_31.living_singles(families, individuals)) == 0:
    print('Error: US31: No Living Singles')
else:
    print('INDIVIDUAL: US31: {}'.format(US_31.living_singles(families, individuals)))



print('\n Test user story 31 Living Singles:')
GedcomClass.main(file1)
if len(US_31.living_singles(families, individuals)) == 0:
    print('Error: US31: No Living Singles')
else:
    print('INDIVIDUAL: US31: {}'.format(US_31.living_singles(families, individuals)))


'''
file = open('./test_ged/user_story_30_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 30:')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US30: The list of living married individuals is {}'
      .format(US_30.living_married(families, individuals)))
'''