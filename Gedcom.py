import sys
import datetime
from prettytable import PrettyTable
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

def get_args(item_id, tag, dic):
    """
    Getters
    """
    string = ''
    for name in dic.get(item_id).get(tag):
        string += name + ', '
    string = string[:-2]
    if string != '':
        return string
    else:
        return 'NA'


def get_age(person_id, individuals):
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


def dates_b4_current_indi(birth, death):
    """
    Checks birth, death dates to ensure they occurred before the current date
    """
    birth_date = datetime.datetime.strptime(birth, '%d %b %Y')
    if death != 'NA':
        death_date = datetime.datetime.strptime(death, '%d %b %Y')
        if birth_date.date() < datetime.datetime.today().date() and death_date.date() < datetime.datetime.today().date():
            return True
        else:
            return False
    if birth_date.date() < datetime.datetime.today().date():
        return True
    else:
        return False
        
def dates_b4_current_fam(marriage, divorce):
    """
    Checks marriage, divorce dates to ensure they occurred before current date
    """
    if marriage == 'NA' and divorce == 'NA':
        return True
    marriage_date = datetime.datetime.strptime(marriage, '%d %b %Y')
    if divorce != 'NA':
        divorce_date = datetime.datetime.strptime(divorce, '%d %b %Y')
        if marriage_date.date() < datetime.datetime.today().date() and divorce_date.date() < datetime.datetime.today().date():
            return True
        else:
            return False
    if marriage_date.date() < datetime.datetime.today().date():
        return True
    else:
        return False

def div_b4_death(divorce_date, husb_death, wife_death):
    """
    Ensures divorce date occurred after death of husband & wife
    """
    if divorce_date == 'NA':
        div_b4_death = 'NO DIV'
        return div_b4_death
    elif husb_death == 'NA' and wife_death == 'NA':
        return True
    
    

def create_pretty_tables(individuals, families):
    """
    Creates tables to display file information.
    """
    pt_indi = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death','Dates Before Now', 'Child', 'Spouse'])

    for item in individuals:
        pt_indi.add_row([item,
                         get_args(item, 'NAME', individuals),
                         get_args(item, 'SEX', individuals),
                         get_args(item, 'BIRT', individuals),
                         get_age(item, individuals),
                         is_alive(item, individuals),
                         get_args(item, 'DEAT', individuals),
                         dates_b4_current_indi (get_args(item, 'BIRT', individuals), get_args(item, 'DEAT', individuals)),
                         get_args(item, 'FAMC', individuals),
                         get_args(item, 'FAMS', individuals)])

    pt_fam = PrettyTable(['ID', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Dates Before Now', 'DIV before DEAT'])

    for item in families:
        husband = get_args(item, 'HUSB', families)
        wife = get_args(item, 'WIFE', families)

        pt_fam.add_row([item, 
                        husband, 
                        get_args(husband, 'NAME', individuals), 
                        wife, 
                        get_args(wife, 'NAME', individuals),
                        dates_b4_current_fam(get_args(item, 'MARR', families), get_args(item, 'DIV', families)),
                        

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

def main(file):
    individuals = read_individuals(file)
    families = read_families(file)
    create_pretty_tables(individuals, families)
    test_suite(individuals)

    print('Done')


###############################################################################
file = open(r'C:\Users\Julie\Documents\GitHub\555\Test GEDCOM Files\JULIE GEDCOM.ged')
main(file)
