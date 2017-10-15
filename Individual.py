class Individual(object):
    """
    Init all the attributes except list ones with None
    Init list attributes with blank list
    """
    def __init__(self):
        self._name = None
        self._sex = None
        self._birt = None
        self._deat = None
        self._spouse = []
        self._child = None

    """
    Getter
    :return 'NA' on missing records
    """
    @property
    def name(self):
        if not self._name:
            return 'NA'
        return self._name

    """
    Setter
    Replace the attribute with given object
    """
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
        self._birt = birt

    @property
    def deat(self):
        if not self._deat:
            return 'NA'
        return self._deat

    @deat.setter
    def deat(self, deat):
        self._deat = deat

    """
    Default getter for list attributes
    :return the list object
    """
    @property
    def spouse(self):
        if not self._spouse:
            return 'NA'
        return self._spouse

    """
    Setter for list attributes
    Append the given object to the list
    """
    @spouse.setter
    def spouse(self, spouse):
        self._spouse.append(spouse)

    """
    Deleter for list attributes
    """
    @spouse.deleter
    def spouse(self):
        self._spouse = []

    """
    String getter for list attributes
    :return the string version of the list object
            append commas for multiple values
    """
    @property
    def spouse_str(self):
        if not self._spouse:
            return 'NA'
        string = ''
        for s in self._spouse:
            string += s + ', '
        string = string[:-2]
        return string

    @property
    def child(self):
        if not self._child:
            return 'NA'
        return self._child

    @child.setter
    def child(self, child):
        self._child = child
