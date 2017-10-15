import unittest
from Sprint2 import us14
import GedcomClass

if __name__ == '__main__':
    unittest.main()


class JL(unittest.TestCase):
    def test_us14(self):
        file = open('./us14_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = us14.has_more_than_five_birth('F1', families)
        self.assertEqual(condition1, True)
        condition2 = us14.has_more_than_five_birth('F2', families)
        self.assertEqual(condition2, False)

    def test_us15(self):
        file = open('./us15_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = us14.has_more_than_fifteen_siblings('F1', families)
        self.assertEqual(condition1, True)
        condition2 = us14.has_more_than_fifteen_siblings('F2', families)
        self.assertEqual(condition2, False)
