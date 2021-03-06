__author__ = 'Owen'
import re
YEAR = re.compile('YEAR:')
year_form = re.compile('\d\d\d\d')
end = re.compile('END')
comment = re.compile('###')
action = re.compile('[\w.]*[\s]?:')
type_country = re.compile('(Country)')
type_region = re.compile('(Region)')
type_modifier = re.compile('(Modifier)')
action_create = re.compile('CREATE')
action_define = re.compile('DEFINE')
action_adjust = re.compile('ADJUST')
action_midfas = re.compile('MIDFAS')
action_remove = re.compile('REMOVE')
action_add = re.compile('ADD')
action_previous = re.compile('[.]')
target = re.compile('"\w.*"')
attribute = re.compile('{[\w\s][^:]*:')
value = re.compile(':[+-]?[\w\s\'][^:]*}')
midfas = re.compile('[{,\s]\d*/\d*[},\s]')
firstnum = re.compile('\d*[/]')
secnum = re.compile('[/]\d*')
name = re.compile('[+-]?\w.*\w|[+-]?\d')
simnum = re.compile('\d*\d')
numbers = re.compile('[+-]?[\d]*')

govt_title = re.compile('GOVERNMENT.')
legt_title = re.compile('LEGITIMACY.')
fact_title = re.compile('FACTIONS.')
appa_title = re.compile('APPARATUS.')
lega_title = re.compile('LEGALISM.')

title = re.compile('[A-Z][A-Z]*[.]')
aspects = re.compile('[A-Z]\w*\s*')
whitespace = re.compile('\s\s')
values = re.compile('[+-]?[\d.]*')

tag = re.compile('[A-Z][A-Z][A-Z][^:]')

entity = re.compile('[\w\s\'.]*[,\n]')
elements = re.compile('[\w\s\'.]*[^,\n]')

infantryxp = re.compile('Infantry\d')
armorxp = re.compile('Armor\d')
destroyersxp = re.compile('Destroyers\d')
cruisersxp = re.compile('Cruisers\d')
battleshipsxp = re.compile('Battleships\d')
fightersxp = re.compile('Fighters\d')
bombersxp = re.compile('Bombers\d')
anyunitxp = re.compile('((Infantry)|(Bombers)|(Destroyers)|(Armor)|(Cruisers)|(Battleships)|(Fighters))\d')
anyunit_name = re.compile('[\D]*')
digit = re.compile('\d')
