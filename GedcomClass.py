from collections import OrderedDict
from prettytable import PrettyTable
from Individual import Individual
from Family import Family


def read_individuals(_file):
    """
    Creates a dictionary of individuals information within the GEDCOM file.
    Key value pairs are individual IDs and the dictionary containing their GEDCOM information.
    """
    # reset the cursor
    _file.seek(0)
    # init variables
    dic = OrderedDict({})
    is_individual = False
    ind = Individual()
    is_date = False
    date_tag = ''

    # loop through the file
    for line in _file:
        # trim
        line = line.strip()
        words = line.split(' ')
        level = words[0]
        args = ''

        if len(words) < 2 or (not level.isdigit()):
            continue

        level = int(level)
        # family or individual tag
        if level == 0:
            # individual tag
            # create a new entry
            # prepare to record
            if len(words) == 3 and words[2] == 'INDI':
                is_individual = True
                ind = Individual()
                ind.id = words[1].replace("@", "")
                if ind.id in dic:
                    ind.id_count = dic[ind.id].id_count + 1
            else:
                is_individual = False
            continue

        if is_individual:
            tag = words[1]
            # date tag
            # prepare to record
            if (tag == 'BIRT' or tag == 'DEAT') and level == 1:
                is_date = True
                date_tag = tag
                continue

            for i in range(2, len(words)):
                args += words[i] + ' '
            args = args[:-1]
            args = args.replace("@", "")

            if len(args) > 0:
                # validate the tag
                if level == 1:
                    if tag == 'NAME':
                        ind.name = args
                    elif tag == 'SEX':
                        ind.sex = args
                    elif tag == 'FAMC':
                        ind.child_of = args
                    elif tag == 'FAMS':
                        ind.spouse_of = args
                if level == 2 and tag == 'DATE' and is_date:
                    if date_tag == 'BIRT':
                        ind.birt = args
                    elif date_tag == 'DEAT':
                        ind.deat = args
                    is_date = False
                    date_tag = ''
        if ind.id != 'NA':
            dic[ind.id] = ind
    return dic


def read_families(_file):
    """
    Creates a dictionary of individuals information within the GEDCOM file.
    Key value pairs are individual IDs and the dictionary containing their GEDCOM information.
    """
    # reset the cursor
    _file.seek(0)
    # init variables
    dic = OrderedDict({})
    is_family = False
    fam = Family()
    is_date = False
    date_tag = ''

    # loop through the file
    for line in _file:
        # trim
        line = line.strip()
        words = line.split(' ')
        level = words[0]
        args = ''

        if len(words) < 2 or (not level.isdigit()):
            continue

        level = int(level)
        # family or individual tag
        if level == 0:
            # individual tag
            # create a new entry
            # prepare to record
            if len(words) == 3 and words[2] == 'FAM':
                is_family = True
                fam = Family()
                fam.id = words[1].replace("@", "")
                if fam.id in dic:
                    fam.id_count = dic[fam.id].id_count + 1
            else:
                is_family = False
            continue

        if is_family:
            tag = words[1]
            # date tag
            # prepare to record
            if (tag == 'MARR' or tag == 'DIV') and level == 1:
                is_date = True
                date_tag = tag
                continue

            for i in range(2, len(words)):
                args += words[i] + ' '
            args = args[:-1]
            args = args.replace("@", "")

            if len(args) > 0:
                # validate the tag
                if level == 1:
                    if tag == 'HUSB':
                        fam.husb = args
                    elif tag == 'WIFE':
                        fam.wife = args
                    elif tag == 'CHIL':
                        fam.chil = args
                if level == 2 and tag == 'DATE' and is_date:
                    if date_tag == 'MARR':
                        fam.marr = args
                    elif date_tag == 'DIV':
                        fam.div = args
                    is_date = False
                    date_tag = ''
        if fam.id != 'NA':
            dic[fam.id] = fam
    return dic


def create_pretty_tables(individuals, families):
    """
    Creates tables to display file information.
    """
    pt_indi = PrettyTable(
        ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
    for item in individuals.values():
        pt_indi.add_row([item.id, item.name, item.sex, item.birt_str, item.age,
                         item.alive, item.deat_str, item.child_of, item.spouse_str])

    pt_fam = PrettyTable(
        ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for item in families.values():
        pt_fam.add_row([item.id, item.marr_str, item.div_str,
                        item.husb, individuals.get(item.husb).name,
                        item.wife, individuals.get(item.wife).name, item.chil_str])

    print(pt_indi)
    print(pt_fam)


def main(_file):
    """
    Print a pretty table
    """
    individuals = read_individuals(_file)
    families = read_families(_file)
    create_pretty_tables(individuals, families)


def get_individual(_id, individuals):
    _object = individuals.get(_id)
    if not _object:
        _object = Individual()
        # print('Error: {} not found in individuals'.format(_id))
    return _object


def get_family(_id, families):
    _object = families.get(_id)
    if not _object:
        _object = Family()
        # print('Error: {} not found in families'.format(_id))
    return _object
