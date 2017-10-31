import GedcomClass

# This user story will check if name and birth are unique in a gedcom file

def uniqueNameAndBirth(indi, individuals):

    name = indi.name
    birth = indi.birt_str

    count =0
    for individual in individuals:
        check_individual = GedcomClass.get_individual(individual, individuals)
        if (check_individual.name == name and check_individual.birt_str == birth):
            count = count+1

    if (count <= 1):
        return True
    else:
        return False