class Individual(object):
    def __init__(self):
        self._name = None
        self._sex = None
        self._birt = None
        self._deat = None
        self._spouse = []
        self._child = None

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
        self._birt = birt

    @property
    def deat(self):
        if not self._deat:
            return 'NA'
        return self._deat

    @deat.setter
    def deat(self, deat):
        self._deat = deat

    @property
    def spouse(self):
        if not self._spouse:
            return 'NA'
        return self._spouse

    @spouse.setter
    def spouse(self, spouse):
        self._spouse.append(spouse)

    @spouse.deleter
    def spouse(self):
        self._spouse = None

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
