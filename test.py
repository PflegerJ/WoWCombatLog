import json
import requests
from requests.models import Response

# example of API call URL
# https://www.warcraftlogs.com:443/v1/rankings/encounter/626?metric=dps&class=7&spec=3&api_key=71267aa6ad93af7d16ae16e5d8d3431f

# API call parameters
#encounter_ID = { "hydross": 623, "lurker": 624, "Leo": 625, "fatham": 626, "morogrim": 627, "vashj":628 }
#view = "damage-done"
#priest_spec = { "disc": 1, "holy": 2, "shadow": 3 }

#guild_info = { "name": "Siberian%20Speed%20Bump", "realm": "bigglesworth", "region": "US"}

#server = ["bigglesworth"]
key = 'api_key=71267aa6ad93af7d16ae16e5d8d3431f'
#api_body = "https://classic.warcraftlogs.com:443/v1"

#@response2 = requests.get('https://www.classic.warcraftlogs.com:443/v1/report/tables/summary/hnxVk8MZPD1g9vbY?api_key=71267aa6ad93af7d16ae16e5d8d3431f')
#response = requests.get('https://classic.warcraftlogs.com:443/v1/reports/guild/Siberian%20Speed%20Bump/Bigglesworth/US?' + key)

#response3 = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/summary/hnxVk8MZPD1g9vbY?start=1637809151291&end=1637822636415&api_key=71267aa6ad93af7d16ae16e5d8d3431f')


#get guild name from file of guild names

#API call reports/guild to get list of logs
#guild_logs = requests.get('https://classic.warcraftlogs.com:443/v1/reports/guild/' + guild_name + '/' + guild_server + '/' + guild_region + '?' + key)
#guild_logs_json = guild_logs.json()

def get_guild_logs(guild_name, guild_server):
    guild_logs = requests.get('https://classic.warcraftlogs.com:443/v1/reports/guild/' + guild_name + '/' + guild_server + '/' + 'us' + '?' + key)
    guild_logs_json = guild_logs.json()
   # print (guild_logs_json)
    list_of_dmg_data = []
    past_tbc = False
    for log in guild_logs_json:
        time = log['end'] - log['start']
        b = log
        c = log['id']

        #fights = requests.get('https://www.warcraftlogs.com:443/v1/report/fights/AVxJCcyQgpdY9HzP?api_key=71267aa6ad93af7d16ae16e5d8d3431f')
        fights = requests.get('https://classic.warcraftlogs.com:443/v1/report/fights/' + log['id'] + '?' + key)
        fights_json = fights.json()
        print  (fights_json)
        alar_present = False
        
        for fight in fights_json['fights']:
            # checking if the log contains the desired fight
            if fight['name'] == 'Patchwerk':
                past_tbc = True
                break
            if fight['name'] == "Al'ar":
                summary = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/summary/' + log['id'] + '?end=' + str(time) + '&' + key)
                summary_json = summary.json()
                for player in summary_json['composition']:
                    if player['type'] == "Priest":
                        
                        spec = player['specs']
                        if spec != []:
                            if spec[0]['spec'] == 'Shadow':
                                player_id = player['id']
                                damage_data = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/damage-done/' + log['id'] + '?end=' + str(time) +'&sourceid=' + str(player_id) + '&encounter=730&wipes=2&' + key)
                                data_data_json = damage_data.json()
                                list_of_dmg_data.append(data_data_json)
        
        if past_tbc:
            break

    return list_of_dmg_data

"""
def write_json_to_file(guild_name, list_of_dmg_data):
    jsonFile = open(guild_name + ".txt", "w")
    for data in list_of_dmg_data:
        jsonString = json.dumps(data)
        jsonFile.write(jsonString)
        jsonFile.write('\n')

    jsonFile.close()
    """  

"""
#guild_file = open('guild_info.txt', 'r')
#guild_file_line = guild_file.readline()
while guild_file_line:
    name_and_server = guild_file_line.split(' ')
    guild_name = name_and_server[0]
    guild_server = name_and_server[1].strip()

    list_of_dmg_data = get_guild_logs(guild_name, guild_server)
    write_json_to_file(guild_name, list_of_dmg_data)


    guild_file_line = guild_file.readline()

#go through each log posted
    #get log ID and total time

"""



#Cleox
damage_data2 = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/damage-done/' + "f7rpMLBtN2ZJjHqg" + '?start=' + str(5673746) + '&end=' + str(5810604) +'&sourceid=' + str(29) + '&' + key)
damage_data_json2 = damage_data2.json()

jsonFile = open("testData1.txt", "w")
jsonString = json.dumps(damage_data_json2)
jsonFile.write(jsonString)  

#Stewzy
damage_data2 = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/damage-done/' + "7GFt1RpkA3HmPraX" + '?start=' + str(2273029) + '&end=' + str(2423669) +'&sourceid=' + str(18) + '&' + key)
damage_data_json2 = damage_data2.json()

jsonFile = open("testData2.txt", "w")
jsonString = json.dumps(damage_data_json2)
jsonFile.write(jsonString)  

#Hernekeitto
damage_data2 = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/damage-done/' + "K7W24PvY3hx6zm9j" + '?start=' + str(3322683) + '&end=' + str(3467589) +'&sourceid=' + str(42) + '&' + key)
damage_data_json2 = damage_data2.json()

jsonFile = open("testData3.txt", "w")
jsonString = json.dumps(damage_data_json2)
jsonFile.write(jsonString)  

#Telia
damage_data2 = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/damage-done/' + "HpZCAq9JRhmYW3Xv" + '?start=' + str(5720036) + '&end=' + str(5838622) +'&sourceid=' + str(11) + '&' + key)
damage_data_json2 = damage_data2.json()

jsonFile = open("testData4.txt", "w")
jsonString = json.dumps(damage_data_json2)
jsonFile.write(jsonString)  

#Paxman
damage_data2 = requests.get('https://www.warcraftlogs.com:443/v1/report/tables/damage-done/' + "vhjnw8mgcAqadCzf" + '?start=' + str(4941739) + '&end=' + str(5091340) +'&sourceid=' + str(8) + '&' + key)
damage_data_json2 = damage_data2.json()

jsonFile = open("testData5.txt", "w")
jsonString = json.dumps(damage_data_json2)
jsonFile.write(jsonString)  