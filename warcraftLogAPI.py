import json
import requests
import sys



def get_new_token():
    auth_server_url = 'https://www.warcraftlogs.com/oauth/token' 
    client_id = '976a4a41-33ff-4e8e-a760-e1c39ec8daa6'
    client_secret = '6BmWiYjqMeDRZ9vtvVucXx2rvxaelMCQM4rvvM1D'

    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post( auth_server_url,
    data = token_req_payload, verify = False, allow_redirects = False,
    auth = ( client_id, client_secret ) )
    if ( token_response.status_code !=200 ):
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)
        
    print("Successfuly obtained a new token")
    tokens = json.loads(token_response.text)
    return tokens['access_token']

def apiCall(query, vars, auth_token):
    api_url = 'https://classic.warcraftlogs.com/api/v2/client'
    api_call_headers = {'Authorization': 'Bearer ' + auth_token}


    api_call_response = requests.post(api_url, json = {"query": query, 'variables': vars}, headers=api_call_headers, verify = True)
    return api_call_response.json()

def getSourceID(query, vars, auth_token, name):
    logz = apiCall(query, vars, auth_token)
    characters = logz['data']['reportData']['report']['playerDetails']['data']['playerDetails']['dps']
    for toon in characters:
        if (toon['name'] == name):
            return toon['id']
    
    return "NA"

def getParseRank(query, vars, auth_token, report_code):
    log = apiCall(query, vars, auth_token)
    reports = log['data']['characterData']['character']['encounterRankings']['ranks'] 
    for report in reports:
        if report['report']['code'] == report_code:
            return report['historicalPercent']
    
    return -1

