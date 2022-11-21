import json
import numpy as np
import math
import csv


"""_summary_
"""
def DoT(spell, totalTime, empty = False, tricks = False, swp = False):

    # data stucture for dot
    dot_data = {'dps': 0,       # total dmg / encounter duration
                'uptime': 0,    # time on boss / encounter duration
                'uses': 0,
                'tick_ratio': 0,    # amount of ticks / uses
                'miss_ratio': 0,    # misses / uses
                'crit_ratio': 0,    # crits / uses

                # tricks of the Trade only
                'Hit Ratio': 0,
                'Hit Min': 0,
                'Hit Max': 0,
                'Hit Total': 0,

                'Resisted Hit Ratio': 0,
                'Resisted Hit Min': 0,
                'Resisted Hit Max': 0,
                'Resisted Hit Total': 0,

                'Critical Hit Ratio': 0,
                'Critical Hit Min': 0,
                'Critical Hit Max': 0,
                'Critical Hit Total': 0,

                'Resisted Critical Hit Ratio': 0,
                'Resisted Critical Hit Min': 0,
                'Resisted Critical Hit Max': 0,
                'Resisted Critical Hit Total': 0,

                # normal dot dmg
                'Resisted Tick Ratio': 0,         # resisted ticks / total ticks
                'Resisted Tick Min': 0, 
                'Resisted Tick Max': 0,
                'Resisted Tick Total': 0,

                'Tick Ratio': 0,                  # normal ticks / total ticks
                'Tick Min': 0,
                'Tick Max': 0,        
                'Tick Total': 0,    

                'Resisted Critical Tick Ratio': 0,        # resisted crit ticks / total ticks
                'Resisted Critical Tick Min': 0,
                'Resisted Critical Tick Max': 0,
                'Resisted Critical Tick Total': 0,

                'Critical Tick Ratio': 0,                 # crit ticks / total ticks
                'Critical Tick Min': 0,
                'Critical Tick Max': 0,
                'Critical Tick Total': 0
    }

    if empty:
        return list(dot_data.values())

    # getting DPS
    dps = spell['total'] / totalTime
    dot_data['dps'] = dps

    # getting Dot uptime
    uptime = spell['uptime'] / totalTime
    dot_data['uptime'] = uptime

    # uses
    uses = spell['uses']
    dot_data['uses'] = uses

    # tick ratio: Ticks per Use
    if spell['tickCount'] != 0:
        tick_count = spell['tickCount']
    else:
        tick_count = spell['hitCount']
    
    tick_ratio = spell['tickCount'] / uses
    dot_data['tick_ratio'] = tick_ratio

    miss_ratio = spell['missCount'] / uses
    dot_data['miss_ratio'] = miss_ratio

    hit_details = spell['hitdetails'] 

    for hit in hit_details:
        hit_type = hit['type']
        ratio = hit['count'] / tick_count
        dot_data[hit_type + ' Ratio'] = ratio
        dot_data[hit_type + ' Min'] = hit['min']
        dot_data[hit_type + ' Max'] = hit['max']
        dot_data[hit_type + ' Total'] = hit['total']

    return list(dot_data.values())


def MF( spell, totalTime):
    mf_data = {
                'dps': 0,
                'uptime': 0,
                'uses': 0,
                'tick_ratio': 0,
                'miss_ratio': 0,
                'Tick': 0,
                'Tick Min': 0,
                'Tick Max': 0
    }
    return 0

"""
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


fileLine4 = file5.readline()
jsonLine4 = json.loads(fileLine4)
spells4 = jsonLine4['entries']
totalTime4 = jsonLine4['totalTime']

for spell4 in spells4:
    spell_id4 = spell4['guid']


fileLine5 = file5.readline()
#jsonLine5 = json.loads(fileLine5)
spells5 = jsonLine5['entries']
totalTime5 = jsonLine5['totalTime']

for spell5 in spells5:
    spell_id5 = spell5['guid']

"""


def writeToFile(fileName, data):
    file = open(fileName, 'w')
    wr = csv.writer(file)
    wr.writerows(data)

    file.close()
    return


def damageSummary(log, totalTime):
    data = []
    validLog = True

    spells = log['data']['reportData']['report']['table']['data']['entries']
    vt = []
    swp = []
    dp = []
    idp = []
    mb = []
    mf = []
    swd = []
    sf = []
    sb = [0, 0]
    sapper = 0
    for spell in spells:
        spell_guid = spell['guid']
        spell_name = spell['name']

        if spell['guid'] == 48160 or spell['guid'] == 48159:          # VT
            vt.append(spell.get('total', -1))
            vt.append(spell.get('uptime', -1) / totalTime)
            vt.append(spell.get('uses', -1))
            vt.append(spell.get('tickCount', -1))
            #vt = DoT(spell, totalTime)
        elif spell['guid'] == 48300 or spell['guid'] == 48299:        # DP
            dp.append(spell.get('total', -1))
            dp.append(spell.get('uptime', -1) / totalTime)
            dp.append(spell.get('uses', -1))
            dp.append(spell.get('tickCount', -1))
            #dp = DoT(spell, totalTime)
        elif spell['guid'] == 48125:        # SWP
            swp.append(spell.get('total', -1))
            swp.append(spell.get('uptime', -1) / totalTime)
            swp.append(spell.get('uses', -1))
            swp.append(spell.get('tickCount', -1))
            #swp = DoT(spell, totalTime, swp = True)
        elif spell['guid'] == 63675:        # improved DP
            idp.append(spell.get('total', -1))
            idp.append(spell.get('hitCount', -1))
        elif spell['guid'] == 48127:    #mb
            mb.append(spell.get('total', -1))
            mb.append(spell.get('uses', -1))
        elif spell['guid'] == 58381:    # mf
            mf.append(spell.get('total', -1))
            mf.append(spell.get('uses', -1))
            mf.append(spell.get('hitCount', -1))
        elif spell['guid'] == 34433:    # shadow fiend
            sf.append(spell.get('total', -1))
            sf.append(spell.get('hitCount', -1))
        elif spell['guid'] == 48158:    # swd
            swd.append(spell.get('total', -1))
            swd.append(spell.get('uses', -1))
        elif spell['guid'] == 56350:    # sar bomb
            sb[0] = spell['total']
            sb[1] = spell['uses']
        elif spell['guid'] == 56488:    #sapper
            sapper = spell['total']

   
  #  print('vt: ', vt)
  #  print('swp: ', swp)
    
   # print('dp: ', dp)
    data.extend(idp)
    #print('idp: ', idp)
    data.extend(mb)
    #print('mb: ', mb)
    data.extend(mf)
    #print('mf: ', mf)
    data.extend(swd)
    #print('swd: ', swd)
    data.extend(mf)
    #print('mf: ', mf)
    data.extend(sb)
    #print('sb: ', sb)
    data.append(sapper)
    #print('sapper: ', sapper)
    #print(data)
    data.extend(vt)
    data.extend(swp)
    data.extend(dp)
    if validLog:
        validLog = len(data) == 27
    for attribute in data:
        if attribute < 0:
            validLog = False

    return data, validLog

"""
data1 = readFile('testData1.txt')
data2 = readFile('testData2.txt')
data3 = readFile('testData3.txt')
data4 = readFile('testData4.txt')
data5 = readFile('testData5.txt')

print (len(data1))
print (len(data2))
print(len(data3))
print (len(data4))
print(len(data5))
data = [data1, data2, data3, data4, data5]
writeToFile('data1Write.csv', data)
"""

"""
guild_info = open('guild_info.txt', 'r')
guild_info_line = guild_info.readline()


while guild_info_line:
    guild_name = guild_info_line.split(' ')[0]
    data = readFile(guild_name + '.txt')
    writeToFile(guild_name + '_raw_data.csv', data)
    guild_info_line = guild_info.readline()
"""

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