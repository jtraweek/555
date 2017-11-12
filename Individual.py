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
        self._spouse_of = []
        self._child_of = None

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
        if (not self._birt) or self._birt == 'E':
            return 'NA'
        return self._birt

    @birt.setter
    def birt(self, birt):
        try:
            self._birt = datetime.strptime(birt, '%d %b %Y')
        except ValueError:
            self._birt = 'E'

    @property
    def birt_str(self):
        if (not self._birt) or self._birt == 'E':
            return 'NA'
        return self._birt.strftime('%d %b %Y')

    @property
    def deat(self):
        if (not self._deat) or self._deat == 'E':
            return 'NA'
        return self._deat

    @deat.setter
    def deat(self, deat):
        try:
            self._deat = datetime.strptime(deat, '%d %b %Y')
        except ValueError:
            self._deat = 'E'

    @property
    def deat_str(self):
        if (not self._deat) or self._deat == 'E':
            return 'NA'
        return self._deat.strftime('%d %b %Y')

    @property
    def spouse_of(self):
        """
        Default getter for list attributes
        :return the list object
        """
        if not self._spouse_of:
            return 'NA'
        return self._spouse_of

    @spouse_of.setter
    def spouse_of(self, spouse):
        """
        Setter for list attributes
        Append the given object to the list
        """
        self._spouse_of.append(spouse)

    @spouse_of.deleter
    def spouse_of(self):
        """
        Deleter for list attributes
        """
        self._spouse_of = []

    @property
    def spouse_str(self):
        """
        String getter for list attributes
        :return the string version of the list object
                append commas for multiple values
        """
        if not self._spouse_of:
            return 'NA'
        string = ''
        for s in self._spouse_of:
            string += s + ', '
        string = string[:-2]
        return string

    @property
    def child_of(self):
        if not self._child_of:
            return 'NA'
        return self._child_of

    @child_of.setter
    def child_of(self, child):
        self._child_of = child

    @property
    def age(self):
        """
        Built-in age calculation
        :return: 'NA' on older than 150 or younger than 0
        """
        if self.birt == 'NA':
            return 'NA'

        birth = self.birt
        if self.deat == 'NA':
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
        if self.deat_str == 'NA' and self.age != 'NA':
            return True
        return False

    @property
    def id_count(self):
        return self._id_count

    @id_count.setter
    def id_count(self, count):
        self._id_count = count

    def is_date_valid(self):
        return self._deat != 'E' and self._birt != 'E'
