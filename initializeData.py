__author__ = 'Owen'
# Hey there, data! Pull up a seat. Here's where you'll be brought together and standardized for use
# in the engine. The engine parameters can still be tuned, but that's a story for another day. For
#now, it's all about putting you in the right OUTFIT!

from loadWorld import *
from loadUniversals import *
from statistics import *
from random import *
import copy

#First thing's first is to import the WORLD and UNIVERSALS from the requisite directory! Remember to
#ensure world.txt and universals.txt are in the same place.
#REFERENCE - 

CNT = AllCountries
REG = AllRegions
UNI = Universals
MOD = AllModifiers
GLV = globalVariables(Year)

def isOwnedBy(C, R):
    try:
        return (C.name == R.Attributes['Owner'])
    except KeyError:
        print('Invalid Owner key for '+R.name)
        raise

def hasQuality(C, U):
    ORONE = (C.Attributes['Legitimacy'] == U.name) or (C.Attributes['Apparatus'] == U.name)
    ORTWO = (C.Attributes['Centralization'] == U.name)
    return ORONE or ORTWO

def define_universal_variables(U):
    attribs = U.Attributes[U.name]
    attribs = list(filter(None, values.findall(attribs)))
    if UNWTMap[U.name] == 'FACTIONS.':
        U.MIL = float(attribs[0])
        U.MIN = float(attribs[1])
        U.isFaction = True
    else:
        U.BS = float(attribs[0])
        U.ID = float(attribs[1])
        U.BT = float(attribs[2])
        U.BAP = float(attribs[3])
        U.UC = float(attribs[4])
        U.BMP = float(attribs[5])
        U.BSci = float(attribs[6])
        U.isFaction = False
    return U

def assign_modifier(M):
    CNT[CIDMap[M.Attributes['Target']]].Modifiers.append(M)
    M.mark_assigned()

def calculate_stats(C):
    #Get base values from universals.
    C.Size = 0
    C.Population = 1
    C.IC = 0
    C.TEP = 0
    C.BS = 0
    C.ID = 0
    C.BT = 0
    C.BAP = 0
    C.UC = 0
    C.BMP = 0
    C.BSci = 0
    C.EPPOP = 0
    C.MP_total = 0
    C.Infantry = list(range(0, 9))
    C.Armor = list(range(0, 9))
    C.Destroyers = list(range(0, 5))
    C.Cruisers = list(range(0, 5))
    C.Battleships = list(range(0, 3))
    C.Fighters = list(range(0, 2))
    C.Bombers = list(range(0, 2))
    for INF in range(0, 9):
        try:
            C.Infantry[INF] = C.Attributes['Infantry'+str(INF+1)]
        except (KeyError, IndexError):
            C.Infantry[INF] = 0
    for CAV in range(0, 9):
        try:
            C.Armor[CAV] = C.Attributes['Armor'+str(CAV+1)]
        except (KeyError, IndexError):
            C.Armor[CAV] = 0
    for DES in range(0, 5):
        try:
            C.Destroyers[DES] = C.Attributes['Destroyers'+str(DES+1)]
        except (KeyError, IndexError):
            C.Destroyers[DES] = 0
    for CRU in range(0, 5):
        try:
            C.Cruisers[CRU] = C.Attributes['Cruisers'+str(CRU+1)]
        except (KeyError, IndexError):
            C.Cruisers[CRU] = 0
    for BAT in range(0, 3):
        try:
            C.Battleships[BAT] = C.Attributes['Battleships'+str(BAT+1)]
        except (KeyError, IndexError):
            C.Battleships[BAT] = 0
    for FIT in range(0, 2):
        try:
            C.Fighters[FIT] = C.Attributes['Fighters'+str(FIT+1)]
        except (KeyError, IndexError):
            C.Fighters[FIT] = 0
    for BOM in range(0, 2):
        try:
            C.Bombers[BOM] = C.Attributes['Bombers'+str(BOM+1)]
        except (KeyError, IndexError):
            C.Bombers[BOM] = 0
    try:
        C.Inertia = C.Attributes['Inertia']
    except KeyError:
        C.Inertia = 50
        print('Error: No Inertia entered, KEY: '+C.name)
        pass
    try:
        C.inStrain = C.Attributes['Strain']
    except KeyError:
        C.inStrain = 0
        pass
    try:
        C.Mobilized = C.Attributes['Mobilized']
    except KeyError:
        C.Mobilized = 0
        pass
    try:
        C.CurMP = C.Attributes['MP']
    except KeyError:
        C.CurMP = 0
        print('Error: No MP entered, KEY: '+C.name)
        pass
    try:
        C.Player = C.Attributes['Player']
    except KeyError:
        C.Player = 'NPC'
        pass
    try:
        C.Ruler = C.Attributes['Ruler']
    except KeyError:
        C.Ruler = 'None'
        pass
    try:
        C.MonGrief = C.Attributes['MonGrief']
    except KeyError:
        C.MonGrief = ''
        pass
    try:
        C.ImpGrief = C.Attributes['ImpGrief']
    except KeyError:
        C.ImpGrief = ''
        pass
    try:
        C.DemGrief = C.Attributes['DemGrief']
    except KeyError:
        C.DemGrief = ''
        pass
    try:
        C.FasGrief = C.Attributes['FasGrief']
    except KeyError:
        C.FasGrief = ''
        pass
    try:
        C.AnaGrief = C.Attributes['AnaGrief']
    except KeyError:
        C.AnaGrief = ''
        pass
    try:
        C.SocGrief = C.Attributes['SocGrief']
    except KeyError:
        C.SocGrief = ''
        pass
    try:
        C.Leadership = C.Attributes['Leadership']
    except KeyError:
        C.Leadership = 'Average'
        pass
    try:
        C.Training = C.Attributes['Training']
    except KeyError:
        C.Training = 'Average'
        pass
    try:
        C.Artillery = C.Attributes['Artillery']
    except KeyError:
        C.Artillery = 'Average'
        pass
    try:
        C.Tactics = C.Attributes['Tactics']
    except KeyError:
        C.Tactics = 'Mixed'
        pass
    try:
        C.NavalPower = C.Attributes['NavalPower']
    except KeyError:
        C.NavalPower = 'Average'
        pass
    try:
        C.AirPower = C.Attributes['AirPower']
    except KeyError:
        C.AirPower = 'Average'
        pass
    for u in range(0, len(UNI)):
        if (hasQuality(C, UNI[u])):
            C.BS += UNI[u].BS
            C.ID += UNI[u].ID
            C.BT += UNI[u].BT
            C.BAP += UNI[u].BAP
            C.UC += UNI[u].UC
            C.BMP += UNI[u].BMP
            C.BSci += UNI[u].BS
    #Calculate base stats
    C.Support = (C.MA * C.MS + C.IA * C.IS + C.DA * C.DS + C.FA * C.FS + C.AA * C.AS + C.SA * C.SS) / 100
    C.Unity = mean([C.MA * C.MS, C.IA * C.IS, C.DA * C.DS, C.FA * C.FS, C.AA * C.AS, C.SA * C.SS]) / 100
    C.Militarism = sum([C.MA * UNI[UNIDMap['Monarchist']].MIL * (C.MS > UNI[UNIDMap['Monarchist']].MIN) / 100,
                         C.IA * UNI[UNIDMap['Imperialist']].MIL * (C.IS > UNI[UNIDMap['Imperialist']].MIN) / 100,
                         C.FA * UNI[UNIDMap['Fascist']].MIL * (C.FS > UNI[UNIDMap['Fascist']].MIN) / 100,
                         C.DA * UNI[UNIDMap['Democrat']].MIL * (C.DS > UNI[UNIDMap['Democrat']].MIN) / 100,
                         C.AA * UNI[UNIDMap['Anarchist']].MIL * (C.AS > UNI[UNIDMap['Anarchist']].MIN) / 100,
                         C.SA * UNI[UNIDMap['Socialist']].MIL * (C.SS > UNI[UNIDMap['Socialist']].MIN) / 100]) ** 2
    C.BMP *= C.Militarism
    #Tally regions in countries.
    for reg in range(0, len(REG)):
        if (isOwnedBy(C, REG[reg])):
            try:
                REG[reg].Population = REG[reg].Attributes['Population']
                REG[reg].Development = REG[reg].Attributes['Development']
                REG[reg].Acceptance = REG[reg].Attributes['Acceptance']
                REG[reg].Occupation = REG[reg].Attributes['Occupied']
            except KeyError:
                print(['Essential variables missing for region ID', reg])
                raise
            REG[reg].IC = (REG[reg].Population * (REG[reg].Development / 100) ** 2 / 100000) * (
                1 - REG[reg].Occupation) * 10
            REG[reg].EP = (REG[reg].Population / 1000000 + REG[reg].IC * 0.15) * REG[reg].Acceptance * (
                1 - REG[reg].Occupation) * 10
            REG[reg].MP = REG[reg].Population * REG[reg].Acceptance * (1 - REG[reg].Occupation) * C.BMP
            REG[reg].EPPOP = REG[reg].EP / REG[reg].Population * 1000000 / REG[reg].Acceptance
            C.Size += 1
            C.Population += REG[reg].Population
            C.IC += REG[reg].IC
            C.TEP += REG[reg].EP
            #C.EPPOP = mean([C.EPPOP, REG[reg].EPPOP])
            C.MP_total += REG[reg].MP
    return C

def calc_all_regions():
    for reg in range(0, len(REG)):
        if REG[reg].Attributes['Owner'] == 0 or REG[reg].Attributes['Owner'] == 'NAN':
            try:
                REG[reg].Population = REG[reg].Attributes['Population']
                REG[reg].Development = REG[reg].Attributes['Development']
                REG[reg].Acceptance = REG[reg].Attributes['Acceptance']
                REG[reg].Occupation = REG[reg].Attributes['Occupied']
            except KeyError:
                print(['Essential variables missing for region ID', reg])
                raise
            REG[reg].Attributes['Owner'] = 'NAN'
            REG[reg].IC = (REG[reg].Population * (REG[reg].Development / 100) ** 2 / 100000) * (
                1 - REG[reg].Occupation) * 10
            REG[reg].EP = (REG[reg].Population / 1000000 + REG[reg].IC * 0.15) * REG[reg].Acceptance * (
                1 - REG[reg].Occupation) * 10
            REG[reg].EPPOP = REG[reg].EP / REG[reg].Population * 1000000 / REG[reg].Acceptance


def get_globals_1():
    count = len(CNT)
    allunities = []
    allsupports = []
    for ui in range(0,count):
        allunities.append(CNT[ui].Unity)
        allsupports.append(CNT[ui].Support)
    GLV.AvgUnity = mean(allunities)
    GLV.StdUnity = pstdev(allunities)
    GLV.AvgSupport = mean(allsupports)
    GLV.StdSupport = pstdev(allsupports)

def calculate_stats_2(C):
    C.Dissent = (C.UC * GLV.StdUnity + GLV.AvgUnity - C.Unity) / GLV.StdUnity**2
    if C.Dissent < 0:
        nodissentbonus = C.Dissent
    else:
        nodissentbonus = 0
    C.SupportBonus = (C.Support - GLV.AvgSupport) / GLV.StdSupport - nodissentbonus
    C.AP = max([C.BAP + C.SupportBonus, 1])
    C.Stability = C.BS * (C.Inertia / 100)**0.33 - C.Dissent
    C.TXP = C.BT + C.SupportBonus
    C.Sci = C.BSci * (1.5 - (C.Inertia/100)**2)
    C.GovtControl = (1 + (C.Mobilized**2 * (0.5 + 0.1 * C.AP)))
    C.MxMP = int(C.MP_total/10000 * C.GovtControl)
    C.EP = C.TEP * (((20 + C.TXP * 3) / 100)**2 + (C.Stability - 6) / 1000)
    C.EPPOP = C.TEP / C.Population * 1000000
    C.EPIC = C.EPPOP * ((1.5 - C.AP * 0.1) + (C.Inertia/100)**0.5)
    C.PGR = 0.03 * (C.Stability / 6)

def get_globals_2():
    count = len(CNT)
    alleps = []
    allics = []
    allmps = []
    allepics = []
    for ui in range(0,count):
        alleps.append(CNT[ui].Unity)
        allics.append(CNT[ui].Support)
        allmps.append(CNT[ui].MxMP)
        allepics.append(CNT[ui].EPIC)
    GLV.AvgEP = mean(alleps)
    GLV.TotalEP = sum(alleps)
    GLV.AvgIC = mean(allics)
    GLV.TotalIC = sum(allics)
    GLV.TotalMP = sum(allmps)
    GLV.TotalEPIC = sum(allepics)
    GLV.AvgEPIC = sum(allepics)/len(allepics)
    growth_chance = [-1,-0.5,0.0,0.25,0.5,0.75,1.0,1.3,1.6,1.9,2.2,2.6,3.0,3.4,3.8,4.2,4.6,5.0,5.5,6.0]
    GLV.PrivateGrowth = choice(growth_chance)/100
    GLV.GovernmentGrowth = median(growth_chance)/100

def apply_modifiers(C):
    C.EPREff = 1
    C.MrkSens = 0
    C.IGRmod = 1
    C.BaseCostModifier = 0
    for di in range(0, len(C.Modifiers)):
        Mod = C.Modifiers[di].Attributes
        quality = Mod['Quality']
        effort = Mod['Effort']
        try:
            power = effort / C.EPIC * quality
        except ZeroDivisionError:
            print('Error: '+C.name+'has zero EPIC and assigned modifiers. Cannot calculate modifier contributions.')
            power = 0
            pass
        Mod['Power'] = power
        try:
            C.Stability += Mod['Stab']
        except KeyError:
            pass
        try:
            C.AP = C.AP + (1 + Mod['AP']/100 * power)
        except KeyError:
            pass
        try:
            C.TXP = C.TXP * (1 + Mod['TXP']/100 * power)
        except KeyError:
            pass
        try:
            C.MxMP = int(C.MP_total/10000 + C.Mobilized * C.AP/100) * (1 + Mod['MP']/100 * power)
        except KeyError:
            pass
        try:
            C.EP = (C.TEP * (((20 + C.TXP * 3) / 100)**2 + (C.Stability - 6) / 1000)) * (1 + Mod['EP']/100 * power)
        except KeyError:
            pass
        try:
            C.IC *= (1 + Mod['IC']/100 * power)
        except KeyError:
            pass
        try:
            C.Sci = C.Sci * (1 + Mod['Sci']/100 * power)
        except KeyError:
            pass
        try:
            C.PGR = C.PGR * (1 + Mod['Growth']/100 * power)
        except KeyError:
            pass
        try:
            C.IGRmod = (1 + Mod['Industry']/100 * power)
        except KeyError:
            C.IGRmod = 1
            pass
        try:
            C.EPREff = (1 + Mod['EPREIN']/100 * power)
        except KeyError:
            C.EPREff = 1
            pass
        try:
            C.MrkSens = Mod['MrkSens'] * power
        except KeyError:
            C.MrkSens = 0
            pass
        try:
            C.BaseCostModifier = Mod['BC'] * power
        except KeyError:
            C.BaseCostModifier = 0
            pass
        try:
            C.StrainDecayModifier = Mod['StrainDecay'] * power
        except KeyError:
            C.StrainDecayModifier = 0
    return C

def calculate_stats_final(C):
    try:
        C.Productivity = C.IC / C.MxMP
        C.BaseCost = max([(GLV.TotalIC / GLV.TotalMP) / C.Productivity * C.EPPOP, 1])
    except ZeroDivisionError:
        C.Productivity = 0
        C.BaseCost = 1
    C.BaseCost *= (1 + C.BaseCostModifier)
    C.Strain = C.EP - C.Spending
    if C.Strain >= 0:
        C.EPREIN = C.Strain
        C.Strain = C.inStrain
    else:
        C.EPREIN = 0
        C.Strain += C.inStrain
    try:
        C.IGR = (C.EPREIN / C.TEP * GLV.GovernmentGrowth * C.EPREff +
                (C.TEP - C.EP) / C.TEP * GLV.PrivateGrowth * (100 + C.MrkSens)) * C.IGRmod / 100\
            + (C.GovtControl * C.Mobilized) / 100
    except ZeroDivisionError:
        C.IGR = 0
        pass
    C.MPTrickle = int((C.MxMP - C.CurMP) / 20 * C.GovtControl * C.Mobilized)
    calculate_upkeep(C)
    get_government_leader(C)
    C.EP -= C.Upkeep
    return C

def update_stats():
    for C in CNT:
        #Calculate base stats
        C.Support = (C.MA * C.MS + C.IA * C.IS + C.DA * C.DS + C.FA * C.FS + C.AA * C.AS + C.SA * C.SS) / 100
        C.Unity = mean([C.MA * C.MS, C.IA * C.IS, C.DA * C.DS, C.FA * C.FS, C.AA * C.AS, C.SA * C.SS]) / 100
        C.Militarism = sum([C.MA * UNI[UNIDMap['Monarchist']].MIL * (C.MS > UNI[UNIDMap['Monarchist']].MIN) / 100,
                             C.IA * UNI[UNIDMap['Imperialist']].MIL * (C.IS > UNI[UNIDMap['Imperialist']].MIN) / 100,
                             C.FA * UNI[UNIDMap['Fascist']].MIL * (C.FS > UNI[UNIDMap['Fascist']].MIN) / 100,
                             C.DA * UNI[UNIDMap['Democrat']].MIL * (C.DS > UNI[UNIDMap['Democrat']].MIN) / 100,
                             C.AA * UNI[UNIDMap['Anarchist']].MIL * (C.AS > UNI[UNIDMap['Anarchist']].MIN) / 100,
                             C.SA * UNI[UNIDMap['Socialist']].MIL * (C.SS > UNI[UNIDMap['Socialist']].MIN) / 100]) ** 2
        C.BMP *= C.Militarism
        #Tally regions in countries.
        C.Size = 0
        C.Population = 0
        C.IC = 0
        C.TEP = 0
        C.MP_total = 0
        for reg in range(0, len(REG)):
            if (isOwnedBy(C, REG[reg])):
                REG[reg].IC = (REG[reg].Population * (REG[reg].Development / 100) ** 2 / 100000) * (1 - REG[reg].Occupation) * 10
                REG[reg].EP = (REG[reg].Population / 1000000 + REG[reg].IC * 0.15) * REG[reg].Acceptance * (1 - REG[reg].Occupation) * 10
                REG[reg].MP = REG[reg].Population * REG[reg].Acceptance * (1 - REG[reg].Occupation) * C.BMP
                REG[reg].EPPOP = REG[reg].EP / REG[reg].Population * 1000000 / REG[reg].Acceptance
                C.Size += 1
                C.Population += REG[reg].Population
                C.IC += REG[reg].IC
                C.TEP += REG[reg].EP
                #C.EPPOP = mean([C.EPPOP, REG[reg].EPPOP])
                C.MP_total += REG[reg].MP
    get_globals_1()
    for C in CNT:
        calculate_stats_2(C)
    get_globals_2()
    for C in CNT:
        apply_modifiers(C)
        calculate_stats_final(C)
    return C

def canonize_country(C):
    print('Canonizing country '+C.name+'...\n')
    C.Canon = {
        "FullName": ptr(C.Attributes['FullName']),
        "Player": ptr(C.Player),
        "Ruler": ptr(C.Ruler),
        "Apparatus": ptr(C.Attributes['Apparatus']),
        "Centralization": ptr(C.Attributes['Centralization']),
        "Legitimacy": ptr(C.Attributes['Legitimacy']),
        "Inertia": ptr(C.Inertia),
        "MP": ptr(C.CurMP),
        "Mobilized": ptr(C.Mobilized),
        "Strain": ptr(C.Strain),
        "MonGrief": ptr(C.MonGrief),
        "ImpGrief": ptr(C.ImpGrief),
        "DemGrief": ptr(C.DemGrief),
        "FasGrief": ptr(C.FasGrief),
        "AnaGrief": ptr(C.AnaGrief),
        "SocGrief": ptr(C.SocGrief),
        "Leadership": ptr(C.Leadership),
        "Training": ptr(C.Training),
        "Artillery": ptr(C.Artillery),
        "Tactics": ptr(C.Tactics),
        "NavalPower": ptr(C.NavalPower),
        "AirPower": ptr(C.AirPower),
        "Infantry": ptr(C.Infantry),
        "Armor": ptr(C.Armor),
        "Destroyers": ptr(C.Destroyers),
        "Cruisers": ptr(C.Cruisers),
        "Battleships": ptr(C.Battleships),
        "Fighters": ptr(C.Fighters),
        "Bombers": ptr(C.Bombers),
        "MonApp": ptr(C.MA),
        "MonSup": ptr(C.MS),
        "ImpApp": ptr(C.IA),
        "ImpSup": ptr(C.IS),
        "DemApp": ptr(C.DA),
        "DemSup": ptr(C.DS),
        "FasApp": ptr(C.FA),
        "FasSup": ptr(C.FS),
        "AnaApp": ptr(C.AA),
        "AnaSup": ptr(C.AS),
        "SocApp": ptr(C.SA),
        "SocSup": ptr(C.SS)
    }

def canonize_region(R):
    assert R.name, 'ERROR: Region has no name.\n'
    print('Canonizing region '+R.name+'...\n')
    assert R.Population, 'ERROR: Region '+R.name+' has no Population.\n'
    assert R.Development>-1, 'ERROR: Region '+R.name+' has no Development.\n'
    assert R.Acceptance>-1, 'ERROR: Region '+R.name+' has no Acceptance.\n'
    assert R.Occupation>-1, 'ERROR: Region '+R.name+' has no Occupation.\n'
    assert R.Attributes['Owner'], 'ERROR: Region '+R.name+' has no Owner.\n'
    R.Canon = {
        "Name": ptr(R.name),
        "Population": ptr(R.Population),
        "Development": ptr(R.Development),
        "Acceptance": ptr(R.Acceptance),
        "Occupied": ptr(R.Occupation),
        "Owner": ptr(R.Attributes['Owner'])
    }

def get_government_leader(C):
    midfas = {0: C.MA, 1: C.IA, 2: C.DA, 3: C.FA, 4: C.AA, 5: C.SA}
    midfass = {0: C.MS, 1: C.IS, 2: C.DS, 3: C.FS, 4: C.AS, 5: C.SS}
    midfas_dic = {0: 'Monarchist', 1: 'Imperialist', 2: 'Democrat', 3: 'Fascist', 4: 'Anarchist', 5: 'Socialist'}
    prevbest = 0
    windex = 0
    for m in range(0, 6):
        a_val = midfas[m] * midfass[m]
        if a_val > prevbest:
            prevbest = a_val
            windex = m
    C.Majority = midfas_dic[windex]

def calculate_upkeep(C):
    C.Upkeep = 0
    for I in C.Infantry:
        C.Upkeep += I * C.EPIC / 10
    for A in C.Armor:
        C.Upkeep += A * C.EPIC / 5
    for D in C.Destroyers:
        C.Upkeep += D * C.EPIC / 7.5
    for R in C.Cruisers:
        C.Upkeep += R * C.EPIC / 5
    for B in C.Battleships:
        C.Upkeep += B * C.EPIC / 2.5
    for F in C.Fighters:
        C.Upkeep += F * C.EPIC / 6.5
    for O in C.Bombers:
        C.Upkeep += O * C.EPIC / 4
    C.Upkeep *= C.Mobilized / 10