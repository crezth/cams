__author__ = 'Owen'
from Classes import *

Universals = []
UNWTMap = {}
UNIDMap = {}
UNID = 0

TYPES = []

working_type = 'SONEREAL IS A SEXY QUEEN'
f = open('universals')
for line in f:
    get_comment = comment.search(line)
    if (not get_comment):
        get_type = title.search(line)
        if not not get_type:
            get_type = get_type.group()
            working_type = get_type
            if working_type not in TYPES:
                TYPES.append(working_type)
        elif (not not title.match(working_type)):
            get_aspect = aspects.search(line)
            get_values = values.findall(line)
            get_values = list(filter(None,get_values))
            if (not not get_aspect) and (not not get_values):
                get_aspect = get_aspect.group()
                get_aspect = name.search(get_aspect).group()
                UNWTMap[get_aspect] = working_type
                UNIDMap[get_aspect] = UNID
                Universals.append(Object(get_aspect))
                Universals[UNID].apply_attribute(get_aspect,str(get_values))
                UNID += 1
