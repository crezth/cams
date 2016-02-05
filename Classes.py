__author__ = 'Owen'
from regulars import *

class Object:
    name = 'Default'
    def __init__(self,name):
        self.name = name
        self.Attributes = {}
        self.isAssigned = False
        self.AttList = []
    def apply_attribute(self,attribute,value):
        if not not numbers.search(value).group():
            self.Attributes[attribute] = float(value)
        else:
            self.Attributes[attribute] = value
    def modify_attribute(self,attribute,mod):
        self.Attributes[attribute] = float(self.Attributes[attribute]) + float(mod)
    def mark_assigned(self):
        self.isAssigned = True
    def check_assigned(self):
        return self.isAssigned
    def hello(self):
        print('My name is', self.name)

class Country(Object):
    def __init__(self,name):
        self.name = name
        self.Attributes = {}
        self.Modifiers = []
        self.MIDFASList = []
        self.MA = 0
        self.MS = 0
        self.IA = 0
        self.IS = 0
        self.DA = 0
        self.DS = 0
        self.FA = 0
        self.FS = 0
        self.AA = 0
        self.AS = 0
        self.SA = 0
        self.SS = 0
    def setMidfas(self,MIDFAS):
        self.MIDFASList = MIDFAS
    def assignMidfasToVars(self):
        i = 0
        [self.MA,self.MS] = self.splitMidfas(i+0)
        [self.IA,self.IS] = self.splitMidfas(i+1)
        [self.DA,self.DS] = self.splitMidfas(i+2)
        [self.FA,self.FS] = self.splitMidfas(i+3)
        [self.AA,self.AS] = self.splitMidfas(i+4)
        [self.SA,self.SS] = self.splitMidfas(i+5)
    def splitMidfas(self,i):
        s1g = name.search(self.MIDFASList[i])
        s1 = s1g.group()
        s2 = simnum.search(firstnum.search(s1).group()).group()
        s3 = simnum.search(secnum.search(s1).group()).group()
        s2 = int(s2)
        s3 = int(s3)
        return s2, s3

class globalVariables(Object):
    def __init__(self,Year):
        self.AvgEPC = 0
        self.StdEPC = 0
        self.AvgUnity = 0
        self.StdUnity = 0
        self.AvgSupport = 0
        self.StdSupport = 0
        self.Year = Year

class ptr:
    def __init__(self, obj): self.obj = obj
    def __call__(self): return self.obj
    def get(self):    return self.obj
    def set(self, obj):      self.obj = obj
    def add(self, chg):      self.obj += chg
    def set_index(self, index, value):    self.obj[index] = value