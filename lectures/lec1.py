def getFNum(self):
    return self.fNum

def setFNum(self, fNum):
    if fNum <= 0:
        raise ValueError('Not a valid Faculty Number!')
    self.fNum = fNum

def getName(self):
    return self.name

def setName(self, name):
    if name == "" or len(name) < 2:
        raise ValueError('Not a real name!')
    self.name = name

def getAvgMark(self):
    return self.avgMark

def setAvgMark(set, avgMark):
    if avgMark < 2 or avgMark > 6:
        raise ValueError("Not a real average mark")
    