from initializeData import *
import battleEngine as be

Cnt = {}
GLV.Year = Year
for j in range(0, len(CNT)):
    Cnt[CNT[j].name] = CNT[j]
    CNT[j].Spending = 0

def cur_year():
    return GLV.Year

def initialize_stats():
    for ui in range(0, len(UNI)):
        define_universal_variables(UNI[ui])
    for mi in range(0, len(MOD)):
        if not MOD[mi].check_assigned():
            assign_modifier(MOD[mi])
    for ci in range(0, len(CNT)):
        calculate_stats(CNT[ci])
    calc_all_regions()
    get_globals_1()
    for ci in range(0, len(CNT)):
        calculate_stats_2(CNT[ci])
    get_globals_2()
    for ci in range(0, len(CNT)):
        apply_modifiers(CNT[ci])
        calculate_stats_final(CNT[ci])
        canonize_country(CNT[ci])
    for r in REG:
        canonize_region(r)
    print('Stats successfully initialized into engine.\n')

def simulate_year(update_file='update.txt'):
    if not update_file == '':
        assert isinstance(update_file, str), 'Update file input must be string.'
        process_update_file(update_file)
        for m in MOD:
            if not m.check_assigned():
                assign_modifier(m)
    for ci in range(0, len(CNT)):
        if CNT[ci].EPREIN == 0 or CNT[ci].EPREIN > CNT[ci].EP:
            CNT[ci].EPREIN = CNT[ci].EP - CNT[ci].Spending
            CNT[ci].IGR = (CNT[ci].EPREIN / CNT[ci].TEP * GLV.GovernmentGrowth * CNT[ci].EPREff +
                 (CNT[ci].TEP - CNT[ci].EP) / CNT[ci].TEP * GLV.PrivateGrowth * (100 - CNT[ci].MrkSens)) * CNT[ci].IGRmod / 100
            #if CNT[ci].IGR < 0: CNT[ci].IGR = 0
        for ri in range(0, len(REG)):
            if isOwnedBy(CNT[ci], REG[ri]):
                REG[ri].Population *= 1 + CNT[ci].PGR
                if REG[ri].Population < 0: REG[ri].Population = 0
                REG[ri].Development *= 1 + CNT[ci].IGR
                if REG[ri].Development < 0: REG[ri].Development = 0
        CNT[ci].Inertia += CNT[ci].ID
        if CNT[ci].Inertia < 0: CNT[ci].Inertia = 0
    update_stats()
    GLV.Year += 1
    print('Year successfully simulated.\n')

def save_world(filename='world'+str(GLV.Year)+'.txt'):
    c0 = '/'
    c1 = ', '
    c2 = '}'
    f = open(filename, 'w')
    f.write('### Countries start here'+'\n')
    f.write('YEAR: '+str(GLV.Year)+'\n')
    for C in CNT:
        f.write('CREATE: (Country) '+'"'+C.name+'"\n')
        f.write('DEFINE: {FullName:'+C.Attributes['FullName']+'}\n')
        f.write('.: {Player:'+C.Player+'}\n')
        f.write('.: {Ruler:'+C.Ruler+'}\n')
        f.write('.: {Apparatus:'+C.Attributes['Apparatus']+'}\n')
        f.write('.: {Centralization:'+C.Attributes['Centralization']+'}\n')
        f.write('.: {Legitimacy:'+C.Attributes['Legitimacy']+'}\n')
        f.write('.: {Inertia:'+format(C.Inertia, '.2f')+'}\n')
        f.write('.: {MP:'+str(int(C.CurMP))+'}\n')
        f.write('.: {Mobilized:'+format(C.Mobilized, '.1f')+'}\n')
        f.write('.: {Strain:'+format(C.Strain, '.0f')+'}\n')
        if not not C.MonGrief:
            f.write('.: {MonGrief:'+C.MonGrief+'}\n')
        if not not C.ImpGrief:
            f.write('.: {ImpGrief:'+C.ImpGrief+'}\n')
        if not not C.DemGrief:
            f.write('.: {DemGrief:'+C.DemGrief+'}\n')
        if not not C.FasGrief:
            f.write('.: {FasGrief:'+C.FasGrief+'}\n')
        if not not C.AnaGrief:
            f.write('.: {AnaGrief:'+C.AnaGrief+'}\n')
        if not not C.SocGrief:
            f.write('.: {SocGrief:'+C.SocGrief+'}\n')
        f.write('.: {Leadership:'+C.Leadership+'}\n')
        f.write('.: {Training:'+C.Training+'}\n')
        f.write('.: {Artillery:'+C.Artillery+'}\n')
        f.write('.: {Tactics:'+C.Tactics+'}\n')
        f.write('.: {NavalPower:'+C.NavalPower+'}\n')
        f.write('.: {AirPower:'+C.AirPower+'}\n')
        for I in range(0, len(C.Infantry)):
            if C.Infantry[I] > 0:
                f.write('.: {Infantry'+str(I+1)+':'+format(C.Infantry[I], '.0f')+'}\n')
        for A in range(0, len(C.Armor)):
            if C.Armor[A] > 0:
                f.write('.: {Armor'+str(A+1)+':'+format(C.Armor[A], '.0f')+'}\n')
        for D in range(0, len(C.Destroyers)):
            if C.Destroyers[D] > 0:
                f.write('.: {Destroyers'+str(D+1)+':'+format(C.Destroyers[D], '.0f')+'}\n')
        for R in range(0, len(C.Cruisers)):
            if C.Cruisers[R] > 0:
                f.write('.: {Cruisers'+str(R+1)+':'+format(C.Cruisers[R], '.0f')+'}\n')
        for B in range(0, len(C.Battleships)):
            if C.Battleships[B] > 0:
                f.write('.: {Battleships'+str(B+1)+':'+format(C.Battleships[B], '.0f')+'}\n')
        for F in range(0, len(C.Fighters)):
            if C.Fighters[F] > 0:
                f.write('.: {Fighters'+str(F+1)+':'+format(C.Fighters[F], '.0f')+'}\n')
        for O in range(0, len(C.Bombers)):
            if C.Bombers[O] > 0:
                f.write('.: {Bombers'+str(O+1)+':'+format(C.Bombers[O], '.0f')+'}\n')
        f.write('MIDFAS: {'+str(C.MA)+c0+str(C.MS)+c1+str(C.IA)+c0+str(C.IS)+c1+str(C.DA)+c0+str(C.DS)+c1+str(C.FA)+
                c0+str(C.FS)+c1+str(C.AA)+c0+str(C.AS)+c1+str(C.SA)+c0+str(C.SS)+c2)
        f.write('\n')
    f.write('### Regions start here'+'\n')
    for R in REG:
        try:
            f.write('CREATE: (Region) '+'"'+R.name+'"'+'\n')
            f.write('DEFINE: {Population:'+str(int(R.Population))+'}\n')
            f.write('.: {Development:'+format(R.Development, '.1f')+'}\n')
            f.write('.: {Acceptance:'+format(R.Acceptance, '.2f')+'}\n')
            f.write('.: {Occupied:'+format(R.Occupation, '.1f')+'}\n')
            f.write('.: {Owner:'+str(R.Attributes['Owner'])+'}\n')
        except AttributeError:
            print('Region '+R.name+' has unacceptable Owner.\n')
            continue
    for M in MOD:
        f.write('CREATE: (Modifier) '+'"'+M.name+'"'+'\n')
        number_of_items = 0
        for item in M.AttList:
            if number_of_items == 0:
                write_action = 'DEFINE:'
            else:
                write_action = '.:'
            f.write(write_action+' {'+item+':'+str(M.Attributes[item])+'}\n')
            number_of_items += 1
    f.write('END')
    f.close()
    print(filename+' created.')

def print_stats(FILE='output.txt'):
    romans = {0: 'I', 1: 'II', 2: 'III',  3: 'IV', 4: 'V'}
    f = open(FILE, 'w')
    f.write('### STATS FOR '+str(GLV.Year)+' A.D. ###\n')
    for C in CNT:
        f.write('Nation: '+C.Attributes['FullName']+' ('+C.Player+')\n')
        #f.write('Ruler: '+C.Ruler+'\n')
        #f.write('Government...\n')
        f.write('Population: '+format(int(C.Population), ',d')+'\n')
        f.write('Stability: '+format(C.Stability, '.1f')+'\n')
        f.write('Apparatus: '+C.Attributes['Apparatus']+'\n')
        f.write('Centralization: '+C.Attributes['Centralization']+'\n')
        f.write('Legitimacy: '+C.Attributes['Legitimacy']+'\n')
        #f.write('Economy...\n')
        f.write('Action Potential: '+format(C.AP, '.0f')+' ('+format(C.Inertia, '.2f')+'% Inertia)\n')
        f.write('Government: '+C.Majority+' ('+format(C.Support, '.2f')+'% Support)\n')
        f.write('MON: '+format(C.MA, '.0f')+' ('+format(C.MS, '.0f')+'%) '+C.MonGrief+'\n')
        f.write('IMP: '+format(C.IA, '.0f')+' ('+format(C.IS, '.0f')+'%) '+C.ImpGrief+'\n')
        f.write('DEM: '+format(C.DA, '.0f')+' ('+format(C.DS, '.0f')+'%) '+C.DemGrief+'\n')
        f.write('FAS: '+format(C.FA, '.0f')+' ('+format(C.FS, '.0f')+'%) '+C.FasGrief+'\n')
        f.write('ANA: '+format(C.AA, '.0f')+' ('+format(C.AS, '.0f')+'%) '+C.AnaGrief+'\n')
        f.write('SOC: '+format(C.SA, '.0f')+' ('+format(C.SS, '.0f')+'%) '+C.SocGrief+'\n')
        f.write('EP: '+format(C.EP, '.0f')+' ('+format(C.TXP, '.0f')+' TxP)\n')
        f.write('IC: '+format(C.IC, '.0f')+' ('+format(C.IGR*100, '+.1f')+'%)\n')
        #f.write('EPIC: '+format(C.EPIC, '.2f')+' ('+format(C.Inertia, '.2f')+')\n')
        f.write('Base Cost: '+format(C.BaseCost, '.0f')+' EP\n')
        inf = []
        arm = []
        infnames = be.infnames
        armnames = be.armnames
        first = True
        for i in range(0, len(C.Infantry)):
            if C.Infantry[i] < 1:
                inf.append('')
            else:
                if first:
                    inf.append(format(C.Infantry[i], '.0f')+' '+infnames[i])
                else:
                    inf.append(', '+format(C.Infantry[i], '.0f')+' '+infnames[i])
                first = False
        for i in range(0, len(C.Armor)):
            if C.Armor[i] < 1:
                arm.append('')
            else:
                if first:
                    arm.append(format(C.Armor[i], '.0f')+' '+armnames[i])
                else:
                    arm.append(', '+format(C.Armor[i], '.0f')+' '+armnames[i])
                first = False
        f.write('Army: ')
        if first:
            f.write('None')
        else:
            for wriob in inf:
                f.write(wriob)
            for wriob in arm:
                f.write(wriob)
        f.write('\n')
        des = []
        cru = []
        bat = []
        desnames = be.desnames
        crunames = be.crunames
        batnames = be.batnames
        first = True
        for i in range(0, len(C.Destroyers)):
            if C.Destroyers[i] < 1:
                des.append('')
            else:
                if first:
                    des.append(format(C.Destroyers[i], '.0f')+' '+desnames[i])
                else:
                    des.append(', '+format(C.Destroyers[i], '.0f')+' '+desnames[i])
                first = False
        for i in range(0, len(C.Cruisers)):
            if C.Cruisers[i] < 1:
                cru.append('')
            else:
                if first:
                    cru.append(format(C.Cruisers[i], '.0f')+' '+crunames[i])
                else:
                    cru.append(', '+format(C.Cruisers[i], '.0f')+' '+crunames[i])
                first = False
        for i in range(0, len(C.Battleships)):
            if C.Battleships[i] < 1:
                bat.append('')
            else:
                if first:
                    bat.append(format(C.Battleships[i], '.0f')+' '+batnames[i])
                else:
                    bat.append(', '+format(C.Battleships[i], '.0f')+' '+batnames[i])
                first = False
        f.write('Navy: ')
        if first:
            f.write('None')
        else:
            for wriob in des:
                f.write(wriob)
            for wriob in cru:
                f.write(wriob)
            for wriob in bat:
                f.write(wriob)
        f.write('\n')
        fit = []
        bom = []
        fitnames = be.fitnames
        bomnames = be.bomnames
        first = True
        for i in range(0, len(C.Fighters)):
            if C.Fighters[i] < 1:
                fit.append('')
            else:
                if first:
                    fit.append(format(C.Fighters[i], '.0f')+' '+fitnames[i])
                else:
                    fit.append(', '+format(C.Fighters[i], '.0f')+' '+fitnames[i])
                first = False
        for i in range(0, len(C.Bombers)):
            if C.Bombers[i] < 1:
                bom.append('')
            else:
                if first:
                    bom.append(format(C.Bombers[i], '.0f')+' '+bomnames[i])
                else:
                    bom.append(', '+format(C.Bombers[i], '.0f')+' '+bomnames[i])
                first = False
        f.write('Air: ')
        if first:
            f.write('None')
        else:
            for wriob in fit:
                f.write(wriob)
            for wriob in bom:
                f.write(wriob)
        f.write('\n')
        f.write('Reserves: '+format(C.CurMP, '.0f')+' Divisions (+'+format(C.MPTrickle,'.0f')+'/turn)\n')
        f.write('Army Quality: '+C.Leadership+' Leadership/'+C.Training+' Training/'+C.Artillery+' Equipment/'+C.Tactics+' Tactics\n')
        f.write('Power Projection: '+C.NavalPower+' Naval/'+C.AirPower+' Air\n')
        f.write('Mobilization: '+format(C.Mobilized*100, '.0f')+'% '+get_alert(C.Mobilized*100)+' (Cost: '+format(-C.Upkeep, '.0f')+' EP/turn)'+'\n')
        f.write('')
        f.write('\n')
    print('File written to '+FILE)

def print_pricing_tables(FILE='pricing_tables_'+str(GLV.Year)):
    f = open(FILE, 'w')
    f.write('### Pricing Tables ('+str(GLV.Year)+') ###\n')
    for C in CNT:
        if not C.Player == 'NPC': #i.e. if the country has a player, then we print the table
            f.write('NATION: '+C.Attributes['FullName']+' (Tag: '+C.name+')\n')
            f.write('Base Cost: '+str(C.BaseCost)+'\n')
            f.write('Effort Value: '+str(C.BaseCost*10)+'\n')

def get_alert(mob):
    if 0 <= mob <= 10:
        alert = '(PEACE)'
    elif mob <= 30:
        alert = '(ALERT)'
    elif mob <= 60:
        alert = '(READY)'
    elif mob <= 90:
        alert = '(WAR)'
    else:
        alert = '(TOTAL WAR)'
    return alert

def global_quick_conscription():
    for C in CNT:
        power_dictionary = {'Nonexistent': 0, 'Weak': 0.5, 'Average': 1, 'Strong': 1.5, 'Global': 2, 'Overwhelming': 3}
        IC_power = 1 + (C.IC - GLV.AvgIC)/C.IC
        C.CurMP *= 0.5
        pool = int(0.5 * C.CurMP) * (1 + C.Mobilized**2)
        inr = C.Inertia
        if inr < 33:
            ic = 'HI'
        elif inr < 66:
            ic = 'MD'
        else:
            ic = 'LO'

        DesFrac = 20
        CruFrac = 35
        BatFrac = 50
        FitFrac = 30
        BomFrac = 40

        InfCoef = {}
        InfCoef['HI'] = [0.2, 0.5, 0.3]
        InfCoef['MD'] = [0.25, 0.5, 0.25]
        InfCoef['LO'] = [0.3, 0.5, 0.2]

        CavCoef = {}
        CavCoef['HI'] = [0.125, 0.115, 0.09]
        CavCoef['MD'] = [0.115, 0.1, 0.05]
        CavCoef['LO'] = [0.1, 0.085, 0.01]

        DesCoef = {}
        DesCoef['HI'] = [2.5/DesFrac, 4.5/DesFrac, 1.5/DesFrac]
        DesCoef['MD'] = [3/DesFrac, 4/DesFrac, 1/DesFrac]
        DesCoef['LO'] = [3/DesFrac, 3/DesFrac, 0.5/DesFrac]

        CruCoef = {}
        CruCoef['HI'] = [2/CruFrac, 4/CruFrac, 1.5/CruFrac]
        CruCoef['MD'] = [4/CruFrac, 3/CruFrac, 1.0/CruFrac]
        CruCoef['LO'] = [5/CruFrac, 3/CruFrac, 0.5/CruFrac]

        BatCoef = {}
        BatCoef['HI'] = [1.5/BatFrac, 3.5/BatFrac, 0/BatFrac]
        BatCoef['MD'] = [2/BatFrac, 3/BatFrac, 0/BatFrac]
        BatCoef['LO'] = [2.5/BatFrac, 2.5/BatFrac, 0/BatFrac]

        FitCoef = {}
        FitCoef['HI'] = [3/FitFrac, 2/FitFrac]
        FitCoef['MD'] = [2/FitFrac, 1/FitFrac]
        FitCoef['LO'] = [1/FitFrac, 0/FitFrac]

        BomCoef = {}
        BomCoef['HI'] = [2/BomFrac, 1/BomFrac]
        BomCoef['MD'] = [1/BomFrac, 0.5/BomFrac]
        BomCoef['LO'] = [0.5/BomFrac, 0/BomFrac]

        for i in [0, 1, 2]:
            C.Infantry[i] = int(InfCoef[ic][i] * pool)
            C.Armor[i] = int(CavCoef[ic][i] * pool * IC_power)
            C.Destroyers[i] = int(DesCoef[ic][i] * pool * IC_power) * power_dictionary[C.NavalPower]
            C.Cruisers[i] = int(CruCoef[ic][i] * pool * IC_power) * power_dictionary[C.NavalPower]
            C.Battleships[i] = int(BatCoef[ic][i] * pool * IC_power) * power_dictionary[C.NavalPower]
        for i in [0, 1]:
            C.Fighters[i] = int(FitCoef[ic][i] * pool * IC_power) * power_dictionary[C.AirPower]
            C.Bombers[i] = int(BomCoef[ic][i] * pool * IC_power) * power_dictionary[C.AirPower]

    print('Global quick conscription finished.\n')

def undo_conscription():
    for C in CNT:
        C.CurMP *= 2.0

        for i in [0, 1, 2]:
            C.Infantry[i] = 0
            C.Armor[i] = 0
            C.Destroyers[i] = 0
            C.Cruisers[i] = 0
            C.Battleships[i] = 0
        for i in [0, 1]:
            C.Fighters[i] = 0
            C.Bombers[i] = 0

    print('All military units descripted.\n')