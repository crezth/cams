__author__ = 'Galileo'
import re

List = []
Map = {}
ID = 0

comment = re.compile('###')
action = re.compile('[\w.]*:')
action_create = re.compile('CREATE')
action_define = re.compile('DEFINE')
action_adjust = re.compile('ADJUST')
action_previous = re.compile('[.]')
target = re.compile('"\w*"')
attribute = re.compile('{\w.*\w:')
value = re.compile(':[+-]?\w.*}')
name = re.compile('[+-]?\w.*\w')
numbers = re.compile('[+-]?\d*')

class Country:
    name = 'Default'
    def __init__(self,name):
        self.name = name
        self.Attributes = {}
    def apply_attribute(self,attribute,value):
        if not not numbers.search(value).group():
            self.Attributes[attribute] = float(value)
        else:
            self.Attributes[attribute] = value
    def modify_attribute(self,attribute,mod):
        self.Attributes[attribute] = float(self.Attributes[attribute]) + float(mod)
    def f(self):
        print('My name is',self.name)

f = open('region.txt')
for line in f:
    get_comment = comment.search(line)
    if not get_comment:
        get_action = action.search(line)
        if not not get_action:
            get_action = get_action.group()
            if (action_previous.match(get_action)) and (not not prev_action):
                get_action = prev_action
            print(get_action)
            if action_create.match(get_action):
                get_target = target.search(line).group()
                region_name = name.search(get_target).group()
                List.append(Country(region_name))
                Map[region_name] = ID
                print(List[ID].name)
                ID += 1
            elif action_define.match(get_action):
                get_target_m = target.search(line)
                if not not get_target_m:
                    get_target = get_target_m.group()
                    target_name = name.search(get_target).group()
                else:
                    if not not region_name:
                        target_name = region_name
                    else:
                        print('Error! DEFINE statement unclear.')
                        break
                get_attribute = name.search(attribute.search(line).group()).group()
                get_value = name.search(value.search(line).group()).group()
                tID = Map[target_name]
                List[tID].apply_attribute(get_attribute,get_value)
                print(get_attribute,List[tID].Attributes[get_attribute])
            elif action_adjust.match(get_action):
                get_target_m = target.search(line)
                if not not get_target_m:
                    get_target = get_target_m.group()
                    target_name = name.search(get_target).group()
                else:
                    if not not region_name:
                        target_name = region_name
                    else:
                        print('Error! ADJUST statement unclear.')
                        break
                get_attribute = name.search(attribute.search(line).group()).group()
                get_value = name.search(value.search(line).group()).group()
                tID = Map[target_name]
                List[tID].modify_attribute(get_attribute,get_value)
                print(get_attribute,List[tID].Attributes[get_attribute])
        prev_action = get_action

for i in range(0,len(List)):
    List[i].f()
    print(List[i].Attributes)