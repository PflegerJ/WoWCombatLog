import json
import numpy as np
import math 
import csv


    
def DoT(spell, totalTime, empty = False):

    dot_data = {'dps': 0,
                'uptime': 0,
                'uses': 0,
                'tick_ratio': 0,
                'miss_ratio': 0,
                'Resisted Tick': 0,
                'Resisted Tick Min': 0,
                'Resisted Tick Max': 0,
                'Tick': 0,
                'Tick Min': 0,
                'Tick Max': 0,
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


def direct_damage(spell, totalTime, empty = False):
    dd_data = {'dps': 0,
                'uses': 0,
                'hit_ratio': 0,
                'crit': 0,
                'Resisted Hit': 0,
                'Resisted Hit Min': 0,
                'Resisted Hit Max': 0,
                'Hit': 0,
                'Hit Min': 0,
                'Hit Max': 0,
                'Resisted Critical Hit': 0,
                'Resisted Critical Hit Min': 0,
                'Resisted Critical Hit Max': 0,
                'Critical Hit': 0,
                'Critical Hit Min': 0,
                'Critical Hit Max': 0
    }

    if empty:
        return list(dd_data.values())

    dps = spell['total'] / totalTime
    dd_data['dps'] = dps

    uses = spell['uses']
    dd_data['uses'] = uses

    hit_ratio = spell['hitCount'] / uses
    dd_data['hit_ratio'] = hit_ratio

    crit_ratio = spell['critHitCount'] / uses
    dd_data['crit_ratio'] = crit_ratio

    hit_details = spell['hitdetails']

    for hit in hit_details:
        hit_type = hit['type']
        ratio = hit['count'] / uses
        dd_data[hit_type] = ratio
        dd_data[hit_type + ' Min'] = hit['min']
        dd_data[hit_type + ' Max'] = hit['max']


    return list(dd_data.values())

def MF(spell, totalTime, empty = False):
    mf_data = {'dps': 0,
                'uptime': 0,
                'uses': 0,
                'tick_ratio': 0,
                'miss_ratio': 0,
                'Tick': 0,
                'Tick Min': 0,
                'Tick Max': 0
    }

    if empty:
        return list(mf_data.values())

    dps = spell['total'] / totalTime
    mf_data['dps'] = dps

    uptime = spell['uptime'] / totalTime
    mf_data['uptime'] = uptime

    uses = spell['uses']
    mf_data['uses'] = uses

    tick_count = spell['tickCount']
    tick_ratio = spell['tickCount'] / uses
    mf_data['tick_ratio'] = tick_ratio

    miss_ratio = spell['missCount'] / uses
    mf_data['miss_ratio'] = miss_ratio

    hit_details = spell['hitdetails'][0]
    hit_type = hit_details['type']
    ratio = hit_details['count'] / tick_count
    mf_data[hit_type] = ratio
    mf_data[hit_type + ' Min'] = hit_details['min']
    mf_data[hit_type + ' Max'] = hit_details['max']

    return list(mf_data.values())


def SF(spell, totalTime, empty = False):
    sf_data = {'dps': 0,
                'uses': 0,
                'hit_count': 0,
                'miss_count': 0,
                'Resisted Hit': 0,
                'Resisted Hit Min': 0,
                'Resisted Hit Max': 0,
                'Hit': 0,
                'Hit Min': 0,
                'Hit Max': 0,
                'Critical Hit': 0,
                'Critical Hit Min': 0,
                'Critical Hit Max': 0,
                'Glancing Blow': 0,
                'Glancing Blow Min': 0,
                'Glancing Blow Max': 0
    }

    if empty:
        return list(sf_data.values())

    dps = spell['total'] / totalTime
    sf_data['dps'] = dps

    uses = spell['uses']
    sf_data['uses'] = uses

    hit_count = spell['hitCount']
    sf_data['hit_count'] = hit_count

    miss_ratio = spell['missCount']
    sf_data['miss_count'] = miss_ratio

    hit_details = spell['hitdetails']

    for hit in hit_details:
        hit_type = hit['type']
        ratio = hit['count']
        sf_data[hit_type] = ratio
        sf_data[hit_type + ' Min'] = hit['min']
        sf_data[hit_type + ' Max'] = hit['max']

    return list(sf_data.values())


def readFile(fileName):
    data = []
    file = open(fileName, 'r')

    fileLine = file.readline()
    while fileLine:
        
        jsonLine = json.loads(fileLine)
        spells = jsonLine['entries']
        totalTime = jsonLine['totalTime']
        line_data = [totalTime]
        swp = []
        vt = []
        swd = []
        mb = []
        sf = []
        mf = []

        for spell in spells:
            spell_name = spell['name']

            if spell_name == 'Shadow Word: Pain' and spell['guid'] == 25368:
                swp = DoT(spell, totalTime)
            elif spell_name == 'Vampiric Touch' and spell['guid'] == 34917:
                vt = DoT(spell, totalTime)
            elif spell_name == 'Shadow Word: Death' and spell['guid'] == 32996:
                swd = direct_damage(spell, totalTime)
            elif spell_name == 'Mind Blast' and spell['guid'] == 25375:
                mb = direct_damage(spell, totalTime)
            elif spell_name == 'Shadowfiend' and spell['guid'] == 34433:
                sf = SF(spell, totalTime)
            elif spell_name == 'Mind Flay' and spell['guid'] == 25387:
                mf = MF(spell, totalTime)


        if len(swp) == 0:
            swp = DoT(-1, -1, True)
        if len(vt) == 0:
            vt = DoT(-1, -1, True)
        if len(swd) == 0:
            swd = direct_damage(-1, -1, True)
        if len(mb) == 0:
            mb = direct_damage(-1, -1, True)
        if len(sf) == 0:
            sf = SF(-1, -1, True)
        if len(mf) == 0:
            mf = MF(-1, -1, True)

        total_dps = swp[0] + vt[0] + swd[0] + mb[0] + sf[0] + mf[0]
        line_data.append(total_dps)
        line_data.extend(swp)
        line_data.extend(vt)
        line_data.extend(swd)
        line_data.extend(mb)
        line_data.extend(sf)
        line_data.extend(mf)

        sum = 0
        for i in range(len(line_data)):
            if i != 0:
                sum = sum + line_data[i]
        

        fileLine = file.readline()
        if sum != 0:
            if data != []:
                if data[-1] != line_data:
                    data.append(line_data)
            else:
                data.append(line_data)
    
    file.close()
    return data

def writeToFile(fileName, data):
    file = open(fileName, 'w')
    wr = csv.writer(file)
    wr.writerows(data)

    file.close()
    return


guild_info = open('guild_info.txt', 'r')
guild_info_line = guild_info.readline()

while guild_info_line:
    guild_name = guild_info_line.split(' ')[0]
    data = readFile(guild_name + '.txt')
    writeToFile(guild_name + '_raw_data.csv', data)
    guild_info_line = guild_info.readline()

#data = readFile('ssb.txt')
#writeToFile('ssb_raw_data.cvs', data)

