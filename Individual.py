from datetime import datetime


class Individual(object):
    def __init__(self):
        """
        Init all the attributes except list ones with None
        Init list attributes with blank list
        """
        self._id = None
        self._id_count = 1
        self._name = None
        self._sex = None
        self._birt = None
        self._deat = None
        self._spouse = []
        self._child = None

    @property
    def id(self):
        """
        Getter
        :return 'NA' on missing records
        """
        if not self._id:
            return 'NA'
        return self._id

    @id.setter
    def id(self, _id):
        """
        Setter
        Replace the attribute with given object
        """
        self._id = _id

    @property
    def name(self):
        if not self._name:
            return 'NA'
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def sex(self):
        if not self._sex:
            return 'NA'
        return self._sex

    @sex.setter
    def sex(self, sex):
        self._sex = sex

    @property
    def birt(self):
        if not self._birt:
            return 'NA'
        return self._birt

    @birt.setter
    def birt(self, birt):
        self._birt = datetime.strptime(birt, '%d %b %Y')

    @property
    def birt_str(self):
        if not self._birt:
            return 'NA'
        return self._birt.strftime('%d %b %Y')

    @property
    def deat(self):
        if not self._deat:
            return 'NA'
        return self._deat

    @deat.setter
    def deat(self, deat):
        self._deat = datetime.strptime(deat, '%d %b %Y')

    @property
    def deat_str(self):
        if not self._deat:
            return 'NA'
        return self._deat.strftime('%d %b %Y')

    @property
    def spouse_of(self):
        """
        Default getter for list attributes
        :return the list object
        """
        if not self._spouse:
            return 'NA'
        return self._spouse

    @spouse_of.setter
    def spouse_of(self, spouse):
        """
        Setter for list attributes
        Append the given object to the list
        """
        self._spouse.append(spouse)

    @spouse_of.deleter
    def spouse_of(self):
        """
        Deleter for list attributes
        """
        self._spouse = []

    @property
    def spouse_str(self):
        """
        String getter for list attributes
        :return the string version of the list object
                append commas for multiple values
        """
        if not self._spouse:
            return 'NA'
        string = ''
        for s in self._spouse:
            string += s + ', '
        string = string[:-2]
        return string

    @property
    def child_of(self):
        if not self._child:
            return 'NA'
        return self._child

    @child_of.setter
    def child_of(self, child):
        self._child = child

    @property
    def age(self):
        """
        Built-in age calculation
        :return: 'NA' on older than 150 or younger than 0
        """
        if not self._birt:
            return 'NA'

        birth = self.birt
        if not self._deat:
            death = datetime.today()
        else:
            death = self.deat
        age = death.year - birth.year
        if 0 <= age < 150:
            return age
        return 'NA'

    @property
    def alive(self):
        """
        Built-in alive validate
        :return: False on age 'NA' or death record exists
        """
        if not self._deat and self.age != 'NA':
            return True
        return False

    @property
    def id_count(self):
        return self._id_count

    @id_count.setter
    def id_count(self, count):
        self._id_count = count
