import requests
import json
import sys

token_uri = 'https://www.warcraftlogs.com/oauth/token' 
client_id = '976a4a41-33ff-4e8e-a760-e1c39ec8daa6'
client_secret = '6BmWiYjqMeDRZ9vtvVucXx2rvxaelMCQM4rvvM1D'

grant_type = 'client_credentials'

a = { 'client_id': '976a4a41-33ff-4e8e-a760-e1c39ec8daa6',
    'client_secret': '6BmWiYjqMeDRZ9vtvVucXx2rvxaelMCQM4rvvM1D', 'grant_type': 'client_credentials' }

json_data = json.dumps(a)
#print(json_data)
r = requests.post(url=token_uri, data= json_data)
print(r)

#curl {client_id}:{client_secret} -d grant_type=client_credentials https://www.warcraftlogs.com/oauth/token

#curl -uri {976a4a41-33ff-4e8e-a760-e1c39ec8daa6}:{6BmWiYjqMeDRZ9vtvVucXx2rvxaelMCQM4rvvM1D} -d 
#grant_type=client_credentials https://www.warcraftlogs.com/oauth/token

#https://www.warcraftlogs.com/oauth/authorize?



api_url = 'https://classic.warcraftlogs.com/api/v2/client'

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

token = get_new_token()


query = """query test2 {
	characterData {
		character(name: "jabes", serverSlug: "whitemane", serverRegion: "us")
		{
			id
			classID
		}
	}
}"""
api_call_headers = {'Authorization': 'Bearer ' + token}
api_call_response = requests.post(api_url, json = {"query": query}, headers=api_call_headers, verify = False)
api_call_response_json = api_call_response.json()
print (api_call_response_json)

print (1665570356502 + 136858)  