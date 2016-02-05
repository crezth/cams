__author__ = 'Owen'

infnames = {0: 'Rifle Infantry', 1: 'Trencher Infantry', 2: 'Assault Infantry'}
armnames = {0: 'Autocar Divisions', 1: 'Lt-Armor Divisions', 2: 'Md-Armor Divisions'}
desnames = {0: 'Gunboats', 1: 'Destroyers', 2: 'Submarines'}
crunames = {0: 'Lt-Cruisers', 1: 'Hv-Cruisers', 2: 'Battlecruisers'}
batnames = {0: 'Dreadnoughts', 1: 'Battleships', 2: 'Great Battleships'}
fitnames = {0: 'Biplane Squadrons', 1: 'Monoplane Squadrons'}
bomnames = {0: 'Triplane Bomber Squadrons', 1: 'Lt-Bomber Squadrons'}

allnames = [infnames, armnames, desnames, crunames, batnames, fitnames, bomnames]

kind_dic = {0: 'Infantry', 1: 'Armor', 2: 'Destroyers', 3: 'Cruisers', 4: 'Battleships', 5: 'Fighters', 6: 'Bombers'}

weapon_numbers = {0: 1000,
                  1: 100,
                  2: 1,
                  3: 1,
                  4: 1,
                  5: 15,
                  6: 15}

TLI_dic = {'Infantry': [1.0, 1.2, 1.4],
           'Armor': [10, 30, 75],
           'Destroyers': [450, 550, 400],
           'Cruisers': [475, 625, 700],
           'Battleships': [700, 950, 1200],
           'Fighters': [15, 25],
           'Bombers': [25, 35]}

leadership_tm = {'Terrible': 0.5,
                 'Poor': 0.8,
                 'Average': 1.0,
                 'Good': 1.2,
                 'Excellent': 1.5}

training_tm = {'Terrible': 0.70,
               'Poor': 0.85,
               'Average': 1.0,
               'Good': 1.15,
               'Excellent': 1.30}


kind_num = int(7)
grade_num = int(6)

def get_morale_factors(country):
    morale_factors = [leadership_tm[country.Leadership], training_tm[country.Training], tactics_tm]