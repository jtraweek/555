import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_18
from Sprint3 import user_story_21
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_28
from Sprint3 import US_29
from Sprint3 import US_30

file = open('../Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
GedcomClass.main(file)
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
