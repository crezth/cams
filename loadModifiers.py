__author__ = 'Owen'
from Classes import *

Mods = []
MODMap = {}
MODID = -1

TYPES = []

working_type = 'I WANT TO PERFORM SEXUAL ACTS ON KRAZNAYA NOT EVEN JOKING'
f = open('modifiers')
for line in f:
    get_comment = comment.search(line)
    if (not get_comment):
        get_action = action.search(line)
        if (not not get_action):
            get_action = get_action.group()
            get_adder = action_add.search(get_action)
            get_dots = action_previous.search(get_action)
            if (not not get_adder):
                MODID += 1
                get_target = name.search(target.search(line).group()).group()
                get_country = name.search(tag.search(line).group()).group()
                MODMap[get_target] = MODID
                Mods.append(Object(get_target))
                Mods[MODID].apply_attribute('Target',get_country)
            elif (not not get_dots):
                get_attribute = name.search(attribute.search(line).group()).group()
                get_value = name.search(value.search(line).group()).group()
                Mods[MODID].apply_attribute(get_attribute,get_value)
f.close()

print('Modifiers loaded\n')