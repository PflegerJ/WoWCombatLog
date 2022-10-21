import json
import requests

key = 'api_key=71267aa6ad93af7d16ae16e5d8d3431f'


guild_logs = requests.get('https://www.warcraftlogs.com:443/v1/reports/user/Jabes?api_key=71267aa6ad93af7d16ae16e5d8d3431f')
guild_logs_json = guild_logs.json()

session = requests.Session()

print(guild_logs_json)
#guild_logs = requests.get('https://classic.warcraftlogs.com:443/v1/reports/guild/' + guild_name + '/' + guild_server + '/' + 'us' + '?' + key)
#    guild_logs_json = guild_logs.json()

print(2)