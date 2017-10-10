import sys
import datetime
import unittest

"""from prettytable import PrettyTable"""
from collections import OrderedDict

"""
Valid GEDCOM file tags:
"""
VALID_FAM_TAGS = {'MARR': 1, 'HUSB': 1, 'WIFE': 1, 'CHIL': 1, 'DIV': 2, 'DATE': 2}
FAM_DATE_TAGS = {'DIV': 1, 'MARR': 1}
VALID_IND_TAGS = {'NAME': 1, 'SEX': 1, 'FAMC': 1, 'FAMS': 1, 'DATE': 2}
IND_DATE_TAGS = {'BIRT': 1, 'DEAT': 1}


def create_person_dict():
    """
    Creates an empty dictionary of personal information within the GEDCOM file.
    Key value pairs are tags and their arguments.
    """
    name = []
    sex = []
    birth_date = []
    death_date = []
    spouse = []
    child = []
    dic = {'NAME': name, 'SEX': sex, 'BIRT': birth_date,
           'DEAT': death_date, 'FAMS': spouse,
           'FAMC': child}
    return dic


def create_family_dict():
    husband = []
    wife = []
    child = []
    marriage_date = []
    divorce_date = []

    dic = {'HUSB': husband, 'WIFE': wife, 'CHIL': child, 'MARR': marriage_date, 'DIV': divorce_date}
    return dic


def read_individuals(file):
    """
    Creates a dictionary called individuals.
    Key value pairs are individual IDs and the dictionary containing their GEDCOM information.
    """
    file.seek(0)
    dic = OrderedDict({})
    is_individual = False
    current_id = ''
    is_date = False
    last_tag = ''

    for line in file:
        line = line.strip()
        words = line.split(' ')
        level = words[0]
        tag = ''
        args = ''

        if len(words) < 2 or (not level.isdigit()):
            continue

        level = int(level)
        if level == 0:
            if len(words) == 3 and words[2] == 'INDI':
                is_individual = True
                current_id = words[1].replace("@", "")
                dic[current_id] = create_person_dict()
            else:
                is_individual = False
                current_id = ''

        if is_individual:
            tag = words[1]

            if tag in IND_DATE_TAGS.keys() and level == IND_DATE_TAGS.get(tag):
                is_date = True
                last_tag = tag
                continue

            if level == VALID_IND_TAGS.get(tag):
                for i in range(2, len(words)):
                    args += words[i] + ' '
                args = args[:-1]

            if len(args) > 0:
                if is_date:
                    dic[current_id][last_tag].append(args)
                    is_date = False
                    last_tag = ''
                else:
                    if tag in dic[current_id]:
                        dic[current_id][tag].append(args)

    return dic


def read_families(file):
    """
    Creates a dictionary called families.
    Key value pairs are family,husband,and wife IDs and the dictionary containing their GEDCOM information.
    """
    file.seek(0)
    dic = OrderedDict({})
    is_family = False
    current_id = ''
    is_date = False
    last_tag = ''

    for line in file:
        line = line.strip()
        words = line.split(' ')
        level = words[0]
        tag = ''
        args = ''

        if len(words) < 2 or (not level.isdigit()):
            continue

        level = int(level)
        if level == 0:
            if len(words) == 3 and words[2] == 'FAM':
                is_family = True
                current_id = words[1].replace("@", "")
                dic[current_id] = create_family_dict()
            else:
                is_family = False
                current_id = ''
            continue

        if is_family:
            tag = words[1]

            if tag in FAM_DATE_TAGS.keys() and level == FAM_DATE_TAGS.get(tag):
                is_date = True
                last_tag = tag
                continue

            if level == VALID_FAM_TAGS.get(tag):
                for i in range(2, len(words)):
                    args += words[i] + ' '
                args = args[:-1].replace("@", "")

            if len(args) > 0:
                if is_date:
                    dic[current_id][last_tag].append(args)
                    is_date = False
                    last_tag = ''
                else:
                    if tag in dic[current_id]:
                        dic[current_id][tag].append(args)

    return dic


'''
Getters
'''


def get_args(item_id, tag, dic):
    string = ''
    for name in dic.get(item_id).get(tag):
        string += name + ', '
    string = string[:-2]
    if string != '':
        return string
    else:
        return 'NA'


def get_age(person_id, individuals):
    """
    This function checks for the age of an individual.
    It either returns the age or 'NA' 
    """
    birth = individuals.get(person_id).get('BIRT')[0].split(' ')[-1]
    year = datetime.date.today().year
    if not is_alive(person_id, individuals):
        year = individuals.get(person_id).get('DEAT')[0].split(' ')[-1]
    age = int(year) - int(birth)
    if age < 150:
        return age
    return 'NA'


def is_alive(person_id, individuals):
    if individuals.get(person_id).get('DEAT'):
        return False
    return True


def birth_before_marriage(family, individual_id, individuals):
    """
    This function checks if a child is born before the marriage of their parents
    """
    for family_id in family:
        marr = family.get(family_id).get('MARR')[0].split(' ')[-1]
        children_list = family.get(family_id).get('CHIL')

        if len(children_list) != 0:

            for child in children_list:
                if child == individual_id:
                    birth = individuals.get(child).get('BIRT')[0].split(' ')[-1]
                    diff_birth_marr = int(birth) - int(marr)
                    if diff_birth_marr < 0:
                        return False
                    else:
                        return True

    return False


###############################################################################

def test(did_pass):
    """
    Print the result of a test
    """
    linenum = sys._getframe(1).f_lineno  # get the caller's line number
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)


def test_suite(dic):
    """
    Tests that values match GEDCOM file
    """
    test(get_args('I1', 'NAME', dic) == 'Rickard /Stark/')
    test(get_args('I1', 'SEX', dic) == 'M')
    test(get_args('I1', 'BIRT', dic) == '18 DEC 0230')
    test(get_args('I1', 'DEAT', dic) == '9 MAY 0280')
    test(get_args('I1', 'FAMC', dic) == 'NA')
    test(get_args('I1', 'FAMS', dic) == '@F1@')


###############################################################################

class TestAge(unittest.TestCase):
    """
    This class tests if the indiual is less than 150 years old
    The data we used in our main GEDCOM file is fictional. 
    And hence we have 'NA' if they are over 150 years old.
    """

    def testAge(self):
        file = open('/Users/celestesakhile/Desktop/555/Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
        individuals = read_individuals(file)

        condition_Satisfied_1 = get_age('I7', individuals)
        self.assertEqual(condition_Satisfied_1, 'NA')

        condition_Satisfied_2 = get_age('I6', individuals)
        self.assertEqual(condition_Satisfied_2, 24)

        condition_Satisfied_3 = get_age('I8', individuals)
        self.assertEqual(condition_Satisfied_3, 36)

        condition_Satisfied_4 = get_age('I11', individuals)
        self.assertEqual(condition_Satisfied_4, -2)

        condition_Satisfied_5 = get_age('I3', individuals)
        self.assertEqual(condition_Satisfied_5, 'NA')


if __name__ == '__main__':
    unittest.main()


###############################################################################

class TestBirthBeforeMarriage(unittest.TestCase):
    """
    This class tests if the child is born before the marriage of their parents.
    """

    def testBirthBeforeMarriage(self):
        file = open('/Users/celestesakhile/Desktop/555/Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
        individuals = read_individuals(file)
        family = read_families(file)

        condition_Satisfied_1 = birth_before_marriage(family, 'I3', individuals)
        self.assertEqual(condition_Satisfied_1, True)

        condition_Satisfied_2 = birth_before_marriage(family, 'I7', individuals)
        self.assertEqual(condition_Satisfied_2, True)

        condition_Satisfied_3 = birth_before_marriage(family, 'I13', individuals)
        self.assertEqual(condition_Satisfied_3, True)

        condition_Satisfied_4 = birth_before_marriage(family, 'I5', individuals)
        self.assertEqual(condition_Satisfied_4, True)

        condition_Satisfied_5 = birth_before_marriage(family, 'I10', individuals)
        self.assertEqual(condition_Satisfied_5, True)


if __name__ == '__main__':
    unittest.main()


###############################################################################


def main(file):
    individuals = read_individuals(file)
    family = read_families(file)

    test_suite(individuals)
    print('Done')


###############################################################################

file = open('/Users/celestesakhile/Desktop/555/Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
main(file)
