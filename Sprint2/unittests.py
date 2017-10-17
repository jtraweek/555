import unittest
from Sprint2 import us14
from Sprint2 import us15
from Sprint2 import us22
import GedcomClass


class JL(unittest.TestCase):
    def test_us14(self):
        file = open('./us14_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = us14.has_more_than_five_birth('F1', individuals, families)
        self.assertEqual(condition1, True)
        condition2 = us14.has_more_than_five_birth('F2', individuals, families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us15(self):
        file = open('./us15_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = us15.has_more_than_fifteen_siblings('F1', families)
        self.assertEqual(condition1, True)
        condition2 = us15.has_more_than_fifteen_siblings('F2', families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us22(self):
        file = open('./us22_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = us22.is_id_unique('I1', individuals)
        self.assertEqual(condition1, True)
        condition2 = us22.is_id_unique('I3', individuals)
        self.assertEqual(condition2, False)
        condition3 = us22.is_id_unique('F2', families)
        self.assertEqual(condition3, True)
        condition4 = us22.is_id_unique('F1', families)
        self.assertEqual(condition4, False)
        file.close()


if __name__ == "__main__":
    unittest.main()
