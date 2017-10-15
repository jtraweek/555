from collections import OrderedDict
from prettytable import PrettyTable
from Individual import Individual


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
            ind = Individual()
            if len(words) == 3 and words[2] == 'INDI':
                is_individual = True
                ind.id = words[1].replace("@", "")
            else:
                is_individual = False
            continue

        if is_individual:
            tag = words[1]
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
                        ind.child = args
                    elif tag == 'FAMS':
                        ind.spouse = args
                    # date tag
                    # prepare to record
                    elif tag == 'BIRT' or tag == 'DEAT':
                        is_date = True
                        date_tag = tag
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


def create_pretty_tables(individuals):
    """
    Creates tables to display file information.
    """
    pt_indi = PrettyTable(
        ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
    for item in individuals.values():
        pt_indi.add_row([item.id, item.name, item.sex, item.birt_str, item.age,
                         item.alive, item.deat_str, item.child, item.spouse_str])
    print(pt_indi)


def main(_file):
    """
    Print a pretty table
    """
    individuals = read_individuals(_file)
    create_pretty_tables(individuals)


# file = open('./Test GEDCOM Files/Liu ged.ged', 'r')
# main(file)
