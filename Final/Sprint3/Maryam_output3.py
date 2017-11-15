import GedcomClass
from Sprint3 import US_29
from Sprint3 import US_30

# THIS FILE IS ADDRESSING WHAT EACH FEATURE SHOULD RETURN!
file = open('./test_ged/user_story_29_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
print('INFORMATION: FAMILY: US29: The list of deceased individuals is {}'
      .format(US_29.deceased_people(individuals)))

file = open('./test_ged/user_story_30_test.ged', 'r')
families = GedcomClass.read_families(file)
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
print('INFORMATION: FAMILY: US30: The list of living married individuals is {}'
      .format(US_30.living_married(families, individuals)))
