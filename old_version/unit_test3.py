import GedcomClass
import unittest
from Sprint1 import user_story_3

file = open('../Test GEDCOM Files/Liu ged.ged', 'r')
individuals = GedcomClass.read_individuals(file)
person_istance = individuals.get()

class TestMethods(unittest.TestCase):
    def test_birth_b4_death(self):  # YOU ARE TESTING THE FUNCTION, NOT THE VALUES!
        self.assertTrue(user_story_3.bir_deth('I1',person_istance.birt,person_istance.deat))
        self.assertGreater(user_story_3.bir_deth('I2','4 SEP 1889','19 OCT 1971'))
        self.assertTrue(user_story_3.bir_deth('I5','29 NOV 1944' ,'NA'))
        self.assertless(user_story_3.bir_deth('I11','7 JAN 1940','1 JAN 1938'))
        self.assertFalse(user_story_3.bir_deth('I12', 'NA','NA' ))
        self.assertFalse(user_story_3.bir_deth('I1', '',''))
        self.assertFalse(user_story_3.bir_deth('I12','22.34','JAN 12'))

if __name__ == '__main__':
    unittest.main()
