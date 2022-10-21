import json
import numpy as np
import math
import csv


"""_summary_
"""
def DoT(spell, totalTime, empty = False):

    # data stucture for dot
    dot_data = {'dps': 0,       # total dmg / encounter duration
                'uptime': 0,    # time on boss / encounter duration
                'uses': 0,
                'tick_ratio': 0,    # amount of ticks / uses
                'miss_ratio': 0,    # misses / uses
                'crit_ratio': 0,    # crits / uses
                'Resisted Tick': 0,         # resisted ticks / total ticks
                'Resisted Tick Min': 0, 
                'Resisted Tick Max': 0,
                'Tick': 0,                  # normal ticks / total ticks
                'Tick Min': 0,
                'Tick Max': 0,          
                'Resisted Crit Tick': 0,        # resisted crit ticks / total ticks
                'Resisted Crit Tick Min': 0,
                'Resisted Crit Tick Max': 0,
                'Crit Tick': 0,                 # crit ticks / total ticks
                'Crit Tick Min': 0,
                'Crit Tick Max': 0
    }

    if empty:
        return list(dot_data.values())

    dps = spell['total'] / totalTime
    dot_data['dps'] = dps

    uptime = spell['uptime'] / totalTime
    dot_data['uptime'] = uptime

    uses = spell['uses']
    dot_data['uses'] = uses

    tick_count = spell['tickCount']
    tick_ratio = spell['tickCount'] / uses
    dot_data['tick_ratio'] = tick_ratio

    miss_ratio = spell['missCount'] / uses
    dot_data['miss_ratio'] = miss_ratio

    hit_details = spell['hitdetails']

    for hit in hit_details:
        hit_type = hit['type']
        ratio = hit['count'] / tick_count
        dot_data[hit_type] = ratio
        dot_data[hit_type + ' Min'] = hit['min']
        dot_data[hit_type + ' Max'] = hit['max']

    return list(dot_data.values())

file = open('testData1.txt', 'r')
file2 = open('testData2.txt', 'r')
file3 = open('testData3.txt', 'r')
file4 = open('testData4.txt', 'r') 
file5 = open('testData5.txt', 'r')

fileLine = file.readline()
jsonLine = json.loads(fileLine)
spells = jsonLine['entries']
totalTime = jsonLine['totalTime']

for spell in spells:
    spell_id = spell['guid']


fileLine4 = file4.readline()
jsonLine4 = json.loads(fileLine4)
spells4 = jsonLine4['entries']
totalTime4 = jsonLine4['totalTime']

for spell4 in spells4:
    spell_id4 = spell4['guid']


fileLine5 = file5.readline()
jsonLine5 = json.loads(fileLine5)
spells5 = jsonLine5['entries']
totalTime5 = jsonLine5['totalTime']

for spell5 in spells5:
    spell_id5 = spell5['guid']



"""
Mind Blast:     48127
Improved DP:    63675
shadowfiend:    34433
Saronite Bomb:  56350
D Plague:       48300
SWP:            48125
VT:             48160
MF:             58381
SWD:            48158
"""  