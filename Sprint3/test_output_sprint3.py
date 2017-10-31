import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_18
from Sprint3 import user_story_21
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_28
from Sprint3 import US_29
from Sprint3 import US_30

file = open('./test_ged/user_story_13_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
        
file = open('./test_ged/user_story_18_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
        
file = open('./test_ged/user_story_21_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
        
file = open('./test_ged/user_story_23_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
        
file = open('./test_ged/user_story_24_test.ged', 'r')
families = GedcomClass.read_families(file)
individuals = GedcomClass.read_individuals(file)
        
file = open('./test_ged/user_story_28_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
        
file = open('./test_ged/user_story_29_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
        
file = open('./test_ged/user_story_30_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
        
