# Suresh Polai Cretead a CounterType
import time
import ast

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
    
    def ListSumReturn(listForm):
        dataTypesCheck = [int, float, bool]; NoRun = 0
        loopNo = 0; listOfTotal = []
        for FirstStep in listForm:
            if NoRun == 0:
                countErrorLine = 0; totalOfBigDataType = 0
                for step1 in FirstStep:
                    if type(step1) in dataTypesCheck: 
                        totalOfBigDataType += step1; countErrorLine += 1
                    else: 
                        listOfTotal = f"{type(step1)} Character Is Present. Start From Place '{countErrorLine + 1}', List No {loopNo}"; NoRun += 1
                listOfTotal.append(totalOfBigDataType)
            else:
                break
        return listOfTotal
    
    def ListSumDictReturn(place, listForm):
        sumValue = 0;  countEnter = 0
        if place in listForm[0].keys():
            for DataIn in listForm:
                if (type(DataIn[place]) == int) or (type(DataIn[place]) == float) or (type(DataIn[place]) == bool): 
                    sumValue += DataIn[place]; countEnter += 1
                else: 
                    sumValue = f"On the place '{place}', {type(DataIn[place])} Character Is Present. Start From Place '{countEnter + 1}'"; break
            return sumValue
        else:
            sumValue = 'No Place Holder Found in Dict'
            return sumValue

    def listSum(self, datatype='int', place = ''):
        if datatype.lower() == 'int':
            return sum(self.lstOfInt)
        elif datatype.lower() == 'float':
            return sum(self.lstOfFloat)
        elif datatype.lower() == 'bool':
            return sum(self.lstOfBool)
        elif datatype.lower() == 'list':
            return counterTypes.ListSumReturn(self.lstOfLst)
        elif datatype.lower() == 'tuple':
            return counterTypes.ListSumReturn(self.lstOfTuple)
        elif datatype.lower() == 'set':
            return counterTypes.ListSumReturn(self.lstOfSet)
        elif datatype.lower() == 'dict':
            return counterTypes.ListSumDictReturn(place=place, listForm=self.lstOfDict)
        else:
            return f"Sum for type '{datatype}' not supported."
        
    def getMaxDataType(self):
        counts = {
            'int': self.integer,
            'float': self.floating,
            'str': self.string,
            'bool': self.boolean,
            'list': self.lst,
            'tuple': self.tpl,
            'set': self.sets,
            'dict': self.dct,
        }
        return max(counts, key=counts.get)
    
    def getMinDataType(self):
        counts = {
            'int': self.integer,
            'float': self.floating,
            'str': self.string,
            'bool': self.boolean,
            'list': self.lst,
            'tuple': self.tpl,
            'set': self.sets,
            'dict': self.dct,
        }
        return min(counts, key=counts.get)
    
    def getCount(self):
        counts = {
            'int': self.integer,
            'float': self.floating,
            'str': self.string,
            'bool': self.boolean,
            'list': self.lst,
            'tuple': self.tpl,
            'set': self.sets,
            'dict': self.dct,
        }
        return counts
    
    def get(self):
        counts = {
            'int': self.lstOfLst,
            'float': self.lstOfFloat,
            'str': self.lstOfString,
            'bool': self.lstOfBool,
            'list': self.lstOfLst,
            'tuple': self.lstOfTuple,
            'set': self.lstOfSet,
            'dict': self.lstOfDict,
        }
        return counts
    
    def sumOfNumeric(self):
        return sum(self.lstOfInt) + sum(self.lstOfFloat) + sum(map(int, self.lstOfBool))
    
    def stringifyAll(self):
        context = {
            "ints": [str(i) for i in self.lstOfInt],
            "floats": [str(f) for f in self.lstOfFloat],
            "bools": [str(b) for b in self.lstOfBool],
            "strings": self.lstOfString,
        }
        return context
    
    def stringFy(self):
        context = [str(i) for i in self.value]
        return context
    
    def start():
        current_Time = time.time()
        return current_Time
    
    def end(lastTime):
        ActualTimeTaken = time.time() - lastTime
        return ActualTimeTaken
    
    def JSON(self):
        return f'`{self.value}`'
    
    @staticmethod
    def UnJSON(valueJSON):
        newData = None
        if isinstance(valueJSON, str) and valueJSON.startswith("`") and valueJSON.endswith("`"):
            clean_data = valueJSON[1:-1]  # remove backticks
            try:
                # Try to parse as Python literal
                newData = ast.literal_eval(clean_data)
            except Exception:
                # If it fails, treat as normal string
                newData = clean_data
        else:
            newData = valueJSON  # already clean or not wrapped
        return newData
    
    # create a stringFy() for one particular

    # create a find function
    # element count function
    # replace function
    # delete function
    # str to int, float
    # multiple nested list covert into one list
    # single list ko chunks mai kar sake chunks([1,2,3,4],2) -> [[1,2], [3,4]]
    


data = [1, 2.2, 'hello', [1, 2], {'a': 1},  9, 18, {'a': 4}, {'a': 1}, [1, 15, 0, 8], (1, 8), 9, (89, 9), False, True, {10, 20}, True]
counter = counterTypes(data)
# print(counter.NonZeroTotal())
# print(counter.listSum('bool'))
# print(counter.lstOfBool)
# print(counter.getMaxDataType())
# print(counter.getMinDataType())
# print(counter.getCount())
# print()
# print(counter.get())
# print(counter.sumOfNumeric())
# print(counter.stringifyAll())
# a1 = counterTypes.start()
# print(counterTypes.end(a1))
# print(counter)
print(counter.stringFy())
JSON_Text = counter.JSON()
print(JSON_Text)
print(counterTypes.UnJSON(JSON_Text))

# statusOne = "`('Hi',  'I', 'am',  'Suresh')`"
# print(type(counterTypes.UnJSON(statusOne)))