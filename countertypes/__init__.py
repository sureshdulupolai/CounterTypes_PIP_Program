# Suresh Polai Cretead a CounterType
class counterTypes:
    def __init__(self, value):
        self.integer = 0
        self.floating = 0
        self.string = 0
        self.boolean = 0
        self.lst = 0
        self.tpl = 0
        self.dct = 0
        self.sets = 0

        self.lstOfInt = []
        self.lstOfFloat = []
        self.lstOfString = []
        self.lstOfBool = []
        self.lstOfLst = []
        self.lstOfTuple = []
        self.lstOfSet = []
        self.lstOfDict = []

        self.value = value

        for i in self.value:
            if isinstance(i, bool):
                self.boolean += 1
                self.lstOfBool.append(i)
            elif isinstance(i, int):
                self.integer += 1
                self.lstOfInt.append(i)
            elif isinstance(i, float):
                self.floating += 1
                self.lstOfFloat.append(i)
            elif isinstance(i, str):
                self.string += 1
                self.lstOfString.append(i)
            elif isinstance(i, list):
                self.lst += 1
                self.lstOfLst.append(i)
            elif isinstance(i, tuple):
                self.tpl += 1
                self.lstOfTuple.append(i)
            elif isinstance(i, set):
                self.sets += 1
                self.lstOfSet.append(i)
            elif isinstance(i, dict):
                self.dct += 1
                self.lstOfDict.append(i)

    def NonZeroTotal(self):
        NewSet = ''
        if self.integer:
            NewSet += f'Int : {self.integer}\n'
        if self.floating:
            NewSet += f'Float : {self.floating}\n'
        if self.string:
            NewSet += f'Str : {self.string}\n'
        if self.boolean:
            NewSet += f'Bool : {self.boolean}\n'
        if self.lst:
            NewSet += f'List : {self.lst}\n'
        if self.tpl:
            NewSet += f'Tuple : {self.tpl}\n'
        if self.sets:
            NewSet += f'Set : {self.sets}\n'
        if self.dct:
            NewSet += f'Dict : {self.dct}\n'
        return NewSet.strip()

    def Total(self):
        return f"Int : {self.integer}\nFloat : {self.floating}\nStr : {self.string}\nbool : {self.boolean}\nlist : {self.lst}\nTuple : {self.tpl}\nSet : {self.sets}\nDict : {self.dct}"
    
    @staticmethod
    def Author():
        return (
            "My name is Suresh Polai, and I am a Python developer with a strong interest "
            "in building helpful and simple Python tools. I created a package called counterTypes "
            "that allows users to input a list containing different data types such as int, float, str, "
            "bool, list, set, tuple, and dict. The class processes the list and counts how many elements "
            "belong to each type, while also storing them in separate sub-lists for easy access."
        )
    