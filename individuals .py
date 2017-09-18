VALID_TAGS = {'NAME': 1, 'SEX': 1, 'FAMC': 1, 'FAMS': 1, 'DATE': 2}
DATE_TAGS = {'BIRT': 1, 'DEAT': 1}


def create_person_dict():
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


def read_individuals(file):
    dic = {}
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
                current_id = words[1]
                dic[current_id] = create_person_dict()
            else:
                is_individual = False
                current_id = ''
            continue

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
                    dic[current_id][last_tag].append(args)
                    is_date = False
                    last_tag = ''
                else:
                    dic[current_id][tag].append(args)
    return dic


def get_name(person_id, individuals):
    return individuals.get(person_id).get('NAME')


def get_gender(person_id, individuals):
    return individuals.get(person_id).get('SEX')


def get_birthday(person_id, individuals):
    return individuals.get(person_id).get('BIRT')


def get_death(person_id, individuals):
    return individuals.get(person_id).get('DEAT')


def get_child(person_id, individuals):
    return individuals.get(person_id).get('FAMC')


def get_spouse(person_id, individuals):
    return individuals.get(person_id).get('FAMS')


file = open('./Test GEDCOM Files/JULIE GEDCOM.ged.ged', 'r')
individuals = read_individuals(file)
print(individuals)
print(get_name('@I1@', individuals))
print(get_gender('@I1@', individuals))
print(get_birthday('@I1@', individuals))
print(get_death('@I1@', individuals))
print(get_child('@I1@', individuals))
print(get_spouse('@I1@', individuals))

