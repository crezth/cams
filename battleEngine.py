__author__ = 'Owen'
# This is the battle engine
# import this file and use method battleEngine.do_battle(attack,defense)

from WW2BattleData import *
import Classes

class Army(Classes.Object):
    def __init__(self, disposition):
        self.disposition = disposition
        self.Units = []
    def add_unit(self, amount, kind, grade):
        self.Units.append(Unit(amount, kind, grade))

class Battle(Classes.Object):
    def __init__(self):
        self.initialized = True

class Unit(Classes.Object):
    def __init__(self, size, kind, grade):
        self.size = size
        self.kind = kind
        self.grade = grade
    def define_stats(self, cntry):
        self.TLI = get_TLI(self.kind, self.grade)
        self.morale = get_morale(cntry)
        self.strength = self.TLI * self.size * self.morale

def do_battle(A, D, Ac, Dc):
    [RedArmy, BlueArmy, BattleObject] = quantify_forces(A, D)
    assign_stats(RedArmy, Ac)
    assign_stats(BlueArmy, Dc)
    generate_environment(BattleObject)
    run_engagement(RedArmy, BlueArmy, BattleObject)

    print('Battle')

def quantify_forces(A, D):
    RedArmy = Army('attack')
    BlueArmy = Army('defense')
    BattleObject = Battle()
    for k in range(0, kind_num):
        for g in range(0, grade_num):
            RedArmy.add_unit(A[kind_dic[k]+str(g)], k, g)
            BlueArmy.add_unit(D[kind_dic[k]+str(g)], k, g)
    return RedArmy, BlueArmy, BattleObject

def assign_stats(ArmyObj, CountryObj):
    for u in ArmyObj.Units:
        ArmyObj.Units.define_stats(CountryObj)

def generate_environment(BattleObj):
    print('Generate environment')

def run_engagement(Attackers, Defenders, Environment):
    print('Run engagement')

def get_morale(CountryObj):
    morale = sum(morale_factors)/len(morale_factors)
    return morale

def get_TLI(kind, grade):
    TLItotal = TLI_dic[kind][grade]
    return TLItotal