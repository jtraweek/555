from dateutil.relativedelta import relativedelta
import GedcomClass


def siblings_spacing(individual, family, individuals):
    birt = individual.birt
    if birt == 'NA':
        return True
    children = family.chil
    for child in children:
        sibling = GedcomClass.get_individual(child, individuals)
        sibling_birt = sibling.birt
        if sibling_birt != 'NA':
            sibling_birt_day_after = sibling_birt + relativedelta(days=1)
            sibling_birt_month_after = sibling_birt + relativedelta(months=8)
            if sibling_birt_day_after < birt < sibling_birt_month_after:
                return False
    return True
