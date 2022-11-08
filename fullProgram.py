
import json
import warcraftLogAPI


encounterID_map = {
    "patchwork": 101118,
    'test': 0
}

full_boss_list_vars = {'bossID': 101118}
full_boss_list_query = """query full_boss_list($bossID: Int!) {
	worldData {
		encounter(id: $bossID) {
			characterRankings (className: "Priest", specName: "Shadow")
		}
	}
}"""

source_id_vars = {'reportCode': 'a'}
source_id_query = """query report($reportCode: String!) {
	reportData {
		report (code: $reportCode) {
			playerDetails (endTime: 1000000000000)
        }
    }
}"""

parse_rank_vars = {'charName': 'a', 'serSlug': 'a', 'serRegion': 'a', 'ID': -1}
parse_rank_query = """query characterRank($charName: String!, $serSlug: String!, $serRegion: String!, $ID: Int!) {
	characterData  {
		character (name: $charName, serverSlug: $serSlug, serverRegion: $serRegion) {
			encounterRankings (compare: Rankings, metric: dps, encounterID: $ID) 		
		}
	}
}"""



auth_token = warcraftLogAPI.get_new_token()

# Get list of all reports for patchwork 
log_count = 100

test_int = 1
 
boss_log_list_api = warcraftLogAPI.apiCall(full_boss_list_query, full_boss_list_vars, auth_token)
boss_log_list = boss_log_list_api['data']['worldData']['encounter']['characterRankings']
for log in boss_log_list['rankings']:
    report_code = log['report']['code']
    total_dps = log['amount']
    duration = log['duration']
    start_time = log['startTime']
    server_region = log['server']['region']
    server = log['server']['name']
    server = server.replace(" ", "")
    print(server)
    player_name = log['name']
 
    #get source Id for future API calls
    source_id_vars['reportCode'] = report_code
    source_id = warcraftLogAPI.getSourceID(source_id_query, source_id_vars, auth_token, player_name)

    #get parse Rank associated with current report code
    parse_rank_vars['charName'] = player_name
    parse_rank_vars['serRegion'] = server_region
    parse_rank_vars['serSlug'] = server
    parse_rank_vars['ID'] = encounterID_map['patchwork']
    parseRank = warcraftLogAPI.getParseRank(parse_rank_query, parse_rank_vars, auth_token, report_code)

    # get stat info

    # get damage info

    # store info


# normalize

# PCA

# plot

# profit



    
   
   


"""

query patchwork_log {
	worldData {
		encounter(id: 101118) {
			characterRankings (className: "Priest", specName: "Shadow")
		}
	}
}

"""
query = """query test2 {
	characterData {
		character(name: "jabes", serverSlug: "whitemane", serverRegion: "us")
		{
			id
			classID
		}
	}
}"""
