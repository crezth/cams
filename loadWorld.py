__author__ = 'Galileo'
from Classes import *

AllCountries = []
AllRegions = []
AllModifiers = []
AllIDs = {}
CIDMap = {}
RIDMap = {}
MIDMap = {}
CID = 0
RID = 0
MID = 0
IDD = {
    "C": CID,
    "R": RID,
    "M": MID
}

def get_object(name):
    type = AllIDs[name]
    if type == 'Country':
        oID = CIDMap[name]
        object = AllCountries[oID]
    elif type == 'Region':
        oID = RIDMap[name]
        object = AllRegions[oID]
    elif type == 'Modifier':
        oID = MIDMap[name]
        object = AllModifiers[oID]
    else:
        print('Error! Item type is invalid.')
    return object

def add_country(country_name):
    AllCountries.append(Country(country_name))
    CIDMap[country_name] = IDD['C']
    #print(AllCountries[ID].name)
    IDD['C'] += 1
    AllIDs[country_name] = 'Country'

def add_region(region_name):
    AllRegions.append(Object(region_name))
    RIDMap[region_name] = IDD['R']
    #print(AllRegions[ID].name)
    IDD['R'] += 1
    AllIDs[region_name] = 'Region'

def add_modifier(modifier_name):
    AllModifiers.append(Object(modifier_name))
    MIDMap[modifier_name] = IDD['M']
    IDD['M'] += 1
    AllIDs[modifier_name] = 'Modifier'

def remove_object(object_name,type_list,type_map):
    type_list.remove(type_map(object_name))
    AllIDs[object_name] = ''

f = open('world.txt')
for line in f:
    get_end = end.match(line)
    if get_end is True:
        break
    get_comment = comment.search(line)
    get_year = YEAR.search(line)
    if not not get_year:
        Year = int(year_form.search(line).group())
    if not get_comment:
        get_action = action.search(line)
        if not not get_action:
            get_action = get_action.group()
            if (action_previous.match(get_action)) and (not not prev_action):
                get_action = prev_action
            #print(get_action)
            if action_create.match(get_action):
                get_target = target.search(line).group()
                country_name = name.search(get_target).group()
                if not not type_country.search(line):
                    add_country(country_name)
                elif not not type_region.search(line):
                    add_region(country_name)
                elif not not type_modifier.search(line):
                    add_modifier(country_name)
            elif action_define.match(get_action):
                get_target_m = target.search(line)
                if not not get_target_m:
                    get_target = get_target_m.group()
                    target_name = name.search(get_target).group()
                else:
                    if not not country_name:
                        target_name = country_name
                    else:
                        print('Error! DEFINE statement unclear.')
                        break
                try:
                    if (not not name.search(attribute.search(line).group())) and (name.search(value.search(line).group())):
                        get_attribute = name.search(attribute.search(line).group()).group()
                        get_value = name.search(value.search(line).group()).group()
                        if AllIDs[target_name] == 'Country':
                            tID = CIDMap[target_name]
                            AllCountries[tID].apply_attribute(get_attribute,get_value)
                        elif AllIDs[target_name] == 'Region':
                            tID = RIDMap[target_name]
                            AllRegions[tID].apply_attribute(get_attribute,get_value)
                        elif AllIDs[target_name] == 'Modifier':
                            tID = MIDMap[target_name]
                            AllModifiers[tID].apply_attribute(get_attribute,get_value)
                except AttributeError:
                    print("Error: Couldn't read attribute at \n"+line)
                    raise
                #print(get_attribute,AllCountries[tID].Attributes[get_attribute])
            elif action_adjust.match(get_action):
                print('ADJUST statements not permitted in world file.\n'+'line:\n'+line)
            elif action_midfas.match(get_action):
                get_target_m = target.search(line)
                if not not get_target_m:
                    get_target = get_target_m.group()
                    target_name = name.search(get_target).group()
                else:
                    if not not country_name:
                        target_name = country_name
                    else:
                        print('Error! MIDFAS statement unclear.')
                        break
                get_midfas = midfas.findall(line)
                for r in range(0,len(get_midfas)):
                    tID = CIDMap[target_name]
                    AllCountries[tID].setMidfas(get_midfas)
                    AllCountries[tID].assignMidfasToVars()
        prev_action = get_action
f.close()

print('World loaded\n')

def process_update_file(filename='update.txt'):
    f = open(filename)
    for line in f:
        get_end = end.match(line)
        if get_end is True:
            break
        get_comment = comment.search(line)
        if not get_comment:
            get_action = action.search(line)
            if not not get_action:
                get_action = get_action.group()
                if action_previous.match(get_action) and (not not prev_action):
                    get_action = prev_action
                if action_create.match(get_action):
                    get_target = target.search(line).group()
                    country_name = name.search(get_target).group()
                    if not not type_country.search(line):
                        add_country(country_name)
                    elif not not type_region.search(line):
                        add_region(country_name)
                    elif not not type_modifier.search(line):
                        add_modifier(country_name)
                elif action_define.match(get_action):
                    get_target_m = target.search(line)
                    if not not get_target_m:
                        get_target = get_target_m.group()
                        target_name = name.search(get_target).group()
                    else:
                        if not not country_name:
                            target_name = country_name
                        else:
                            print('Error! DEFINE statement unclear.'+line)
                            break
                    try:
                        if (not not name.search(attribute.search(line).group())) and (name.search(value.search(line).group())):
                            get_attribute = name.search(attribute.search(line).group()).group()
                            get_value = name.search(value.search(line).group()).group()
                            if AllIDs[target_name] == 'Country':
                                tID = CIDMap[target_name]
                                AllCountries[tID].apply_attribute(get_attribute,get_value)
                            elif AllIDs[target_name] == 'Region':
                                tID = RIDMap[target_name]
                                AllRegions[tID].apply_attribute(get_attribute,get_value)
                            elif AllIDs[target_name] == 'Modifier':
                                tID = MIDMap[target_name]
                                AllModifiers[tID].apply_attribute(get_attribute,get_value)
                                AllModifiers[tID].AttList.append(get_attribute)
                    except AttributeError:
                        print("Error: Couldn't read attribute at \n"+line)
                        raise
                elif action_adjust.match(get_action):
                    get_target = target.search(line)
                    if not not get_target:
                        get_target = get_target.group()
                        target_name = name.search(get_target).group()
                    else:
                        if not not country_name:
                            target_name = country_name
                        else:
                            print('Error! ADJUST statement unclear.\n'+line)
                            break
                    if (not not name.search(attribute.search(line).group())) and (name.search(value.search(line).group())):
                        get_attribute = name.search(attribute.search(line).group()).group()
                        get_value = name.search(value.search(line).group()).group()
                        if AllIDs[target_name] == 'Country':
                            tID = CIDMap[target_name]
                            if anyunitxp.match(get_attribute):
                                unit_type = int(digit.search(get_attribute).group()) - 1
                                get_attribute = anyunit_name.search(get_attribute).group()
                                AllCountries[tID].Canon[get_attribute].set_index(unit_type, int(get_value))
                            else:
                                if not isinstance(AllCountries[tID].Canon[get_attribute].get(), str):
                                    AllCountries[tID].Canon[get_attribute].add(float(get_value))
                                else:
                                    AllCountries[tID].Canon[get_attribute].set(get_value)
                        elif AllIDs[target_name] == 'Region':
                            rID = RIDMap[target_name]
                            if isinstance(AllRegions[rID].Canon[get_attribute].get(), int):
                                AllRegions[rID].Canon[get_attribute].add(get_value)
                            else:
                                AllRegions[rID].Canon[get_attribute].set(get_value)
                        elif AllIDs[target_name] == 'Modifier':
                            print('Cannot perform ADJUST on Modifier-type object.\n'+line)
                elif action_remove.match(get_action):
                    get_target = target.search(line)
                    if not not get_target:
                        get_target = get_target.group()
                        target_name = name.search(get_target).group()
                        if AllIDs[target_name] == 'Country':
                            remove_object(target_name,AllCountries,CIDMap)
                        elif AllIDs[target_name] == 'Region':
                            remove_object(target_name,AllRegions,RIDMap)
                        elif AllIDs[target_name] == 'Modifier':
                            remove_object(target_name,AllModifiers,MIDMap)
                    else:
                        print('Error! REMOVE statement MUST have clearly defined target.\n'+line)
            prev_action = get_action