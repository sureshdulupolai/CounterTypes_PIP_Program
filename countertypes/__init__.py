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
            'int': self.lstOfInt,
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

    def compareEachElement(first, second):
        if (type(first) == list) and (type(second) == list):
            if all(isinstance(x, (int, float)) for x in first):
                if all(isinstance(x, (int, float)) for x in second):
                    if len(first) == len(second):
                        valueOne = 0
                        valueTwo = 0
                        for i in range(len(first)):
                            if first[i] > second[i]:
                                valueOne += 1
                            elif first[i] < second[i]:
                                valueTwo += 1

                        if valueOne > valueTwo:
                            return 'First list element is Greater, Then second list element.'
                        elif valueOne < valueTwo:
                            return 'Second list element is Greater, Then first list element.'
                        elif valueOne == valueTwo:
                            return 'Both List Element Has Same Number'
                        
                    else:
                        lenOfFirst, lenOfSecond = len(first), len(second)
                        if lenOfFirst > lenOfSecond:
                            return 'first list has more element, comparing with second.'
                        else:
                            return 'second list has more element, comparing with first.'
                else:
                    return 'Element type should be Integer or Float, In second list.'
            else:
                return 'Element type should be Integer or Float, In first list.'
        else:
            return 'only list type is supported'

    def reverse(self, reverse = True):
        if reverse:
            return [i for i in self.value[::-1]]
        elif reverse == False:
            return self.value
        else:
            return f'reverse={reverse} type error'

    def numeriFy(self):
        newList = []
        for DataInList in self.value:
            if DataInList.isalpha():
                newList.append(DataInList)
            elif '.' in DataInList:
                newList.append(float(DataInList))
            elif DataInList.isdigit():
                newList.append(int(DataInList))
        return newList

    def boolUnCondition(self):
        newList = []
        for DataIn in self.value:
            if DataIn == 'True':
                    newList.append(bool(True))
            elif DataIn == 'False':
                newList.append(bool(False))
            else:
                newList.append(DataIn)
        return newList
    
    def boolCondtion(self, Truekey, FalseKey):
        newList = []
        for DataIn in self.value:
            if DataIn == Truekey:
                    newList.append(bool(True))
            elif DataIn == FalseKey:
                newList.append(bool(False))
            else:
                newList.append(DataIn)
        return newList

    def booliFy(self, condition = False, Truekey = 'True', FalseKey = 'False'):
        if condition:
            return self.boolCondtion(Truekey = Truekey, FalseKey= FalseKey)
        else:
            return self.boolUnCondition()

    def formatic(self, key = False):
        newlist = []
        if key:
            newlist.append(self.get())
        else:
            newlist = [] + self.lstOfInt + self.lstOfFloat + self.lstOfBool + self.lstOfString + self.lstOfLst + self.lstOfTuple + self.lstOfSet + self.lstOfDict
        return newlist
    
    def fc(self, key, check):
        fd = 0; count = 0
        for findElement in self.value:
            if key == findElement:
                count += 1
                fd += 1

        if check == 'Find':
            if fd == 0:
                return f'No Key={key} Not Found Inside List.'
            else:
                return f'Yes!, Key={key} existing inside List.'
            
        elif check == 'Count':
            if fd == 0:
                return f'No Key={key} Not Found Inside List.'
            else:
                return f'Yes!, Key={key} existing inside List and count = {count}.'

    def find(self, key):
        return self.fc(key=key, check='Find')

    def count(self, key):
        return self.fc(key=key, check='Count')
        
    def replace(self, re, key):
        newList = []
        for listEle in self.value:
            if listEle == re:
                newList.append(key)
            else:
                newList.append(listEle)
        return newList

    def remove(self, key):
        newList = []
        for listElement in self.value:
            if listElement != key:
                newList.append(listElement)
        return newList

    def oneList(self):
        def flatten(data):
            result = []
            for item in data:
                if isinstance(item, list):
                    result.extend(flatten(item))
                else:
                    result.append(item)
            return result
        return flatten(self.value)

    def chunks(self, pair):
        chunked = []
        temp = self.value[:]  # original list ka copy

        # Agar length divisible nahi hai, to 0 pad karke complete karo
        while len(temp) % pair != 0:
            temp.append(0)

        # Chunk banate jao
        for i in range(0, len(temp), pair):
            chunked.append(temp[i:i + pair])

        if len(chunked) == 1:
            chunkeds = []
            for i in chunked:
                for j in i:
                    chunkeds.append(j)
            return chunkeds
        
        else:
            return chunked