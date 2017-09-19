import sys
from prettytable import PrettyTable
from collections import OrderedDict

"""
Valid GEDCOM file tags:
"""
VALID_TAGS = {'NAME': 1, 'SEX': 1, 'FAMC': 1, 'FAMS': 1, 'DATE': 2}
DATE_TAGS = {'BIRT': 1, 'DEAT': 1}


def create_person_dict():
    """
    Creates an empty dictionary of personal information within the GEDCOM file.
    Key value pairs are tags and their arguments.
    """
    name = 'NA'
    sex = 'NA'
    birth_date = 'NA'
    death_date = 'NA'
    spouse = 'NA'
    child = 'NA'
    dic = {'NAME': name, 'SEX': sex, 'BIRT': birth_date,
           'DEAT': death_date, 'FAMS': spouse,
           'FAMC': child}
    return dic

def create_family_dict():

    FAMID = ''
    HUSBID = ''
    WIFEID = ''
    dic = {'FAM': FAMID, 'HUSB': HUSBID, 'WIFE': WIFEID}
    return dic

def read_individuals(file):
    """
    Creates a dictionary called individuals.
    Key value pairs are individual IDs and the dictionary containing their GEDCOM information.
    """
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
                current_id = words[1].replace("@","")
                dic[current_id] = create_person_dict()
            else:
                is_individual = False
                current_id = ''


        if is_individual:
            tag = words[1]

            if tag in DATE_TAGS.keys() and level == DATE_TAGS.get(tag):
                is_date = True
                last_tag = tag
                continue

            if level == VALID_TAGS.get(tag):
                for i in range(2, len(words)):
                    args += words[i] + ' '
                args = args[:-1]

            if len(args) > 0:
                if is_date:
                    dic[current_id][last_tag] = args
                    is_date = False
                    last_tag = ''
                else:
                    dic[current_id][tag] = args

    return dic

def read_families(file):
    """
    Creates a dictionary called families.
    Key value pairs are family,husband,and wife IDs and the dictionary containing their GEDCOM information.
    """
    dic = OrderedDict({})
    is_family = False
    is_husband = False
    is_wife = False
    current_id = ''

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
                current_id = words[1].replace("@","")
                dic[current_id] = create_family_dict()
            else:
                is_family = False
                current_id = ''

            if len(words) == 3 and words[1] == "HUSB" and level == 1:
                is_husband = True
                tag = words[1]
                HUSBID = words[2].replace("@", "")
                dic[current_id] = create_family_dict()
            else:
                is_husband = False
                current_id = ''

            if len(words) == 3 and words[1] == "WIFE" and level == 1:
                is_wife = True
                tag = words[1]
                WIFEID = words[2].replace("@", "")
                dic[current_id] = create_family_dict()
            else:
                is_wife = False
                current_id = ''

        if is_individual:
            tag = words[1]

            if level == VALID_TAGS.get(tag):
                for i in range(2, len(words)):
                    args += words[i] + ' '
                args = args[:-1]

    return dic

def create_pretty_tables(individuals):
    """
    Creates tables to display file information.
    """
    pt_indi = PrettyTable(['ID', 'Name'[0]])

    for item in individuals:
        pt_indi.add_row([item, str(individuals[item]['NAME'])])

    pt_fam = PrettyTable(['ID', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name'])
    print(pt_indi)
    print(pt_fam)


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


def test_suite(individuals):
    """
    Tests that values match GEDCOM file
    """
    test(individuals['@I1@']['NAME'] == 'Rickard /Stark/')
    test(individuals['@I1@']['SEX'] == 'M')
    test(individuals['@I1@']['BIRT'] == '18 DEC 0230')
    test(individuals['@I1@']['DEAT'] == '9 MAY 0280')
    test(individuals['@I1@']['FAMC'] == 'NA')
    test(individuals['@I1@']['FAMS'] == '@F1@')


###############################################################################

def main(file):
    individuals = read_individuals(file)
    create_pretty_tables(individuals)
    test_suite(individuals)


###############################################################################

file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
main(file)