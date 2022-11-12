
import json
import warcraftLogAPI
import readDamageDone
import normalize
import pca


encounterID_map = {
    "patchwork": 101118,
    'test': 0
}

full_boss_list_vars = {'bossID': 101118,
    'pageNumber': 1}
full_boss_list_query = """query full_boss_list($bossID: Int!, $pageNumber: Int!) {
    worldData {
        encounter(id: $bossID) {
            characterRankings (className: "Priest", specName: "Shadow", page: $pageNumber)
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

damage_summary_vars = {'reportCode': 'a', 'start': 0, 'end': 0, 'ID': 0}
damage_summary_query = """query damage_summary($reportCode: String!, $start: Float!, $end: Float!, $ID: Int!) {
    reportData {
        report (code: $reportCode) {
            table (dataType: DamageDone, startTime: $start, endTime: $end, sourceID: $ID) 
        }
    }
}"""

stat_info_query = """query statInfo ($reportCode: String!, $start: Float!, $end: Float!, $ID: Int!) {
	reportData {
		report (code: $reportCode) {
			table(startTime: $start, endTime: $end, sourceID: $ID)			
		}
	}
}
"""
downlaod_logs = True
normalize_logs = True
page_start = 1
page_count = 6
auth_token = warcraftLogAPI.get_new_token()

page_curr = page_start
if downlaod_logs:
    # Get list of all reports for patchwork 
    full_parse_data_list = []
    full_boss_list_vars['pageNumber'] = page_start
    for page_curr in range(page_start, page_count):
        print(page_curr)
        full_boss_list_vars['pageNumber'] = page_curr
        boss_log_list_api = warcraftLogAPI.apiCall(full_boss_list_query, full_boss_list_vars, auth_token)
        boss_log_list = boss_log_list_api['data']['worldData']['encounter']['characterRankings']

        

        oldParseRank = 100
        for log in boss_log_list['rankings']:
            parse_data = []
            #print(test_cur)

            valid_data = True
            #check if report is already in database

            report_code = log['report']['code']
            total_dps = log['amount']
        
            server_region = log['server']['region']
            server = log['server']['name']
            server = server.replace(" ", "")
            #print(server)
            player_name = log['name']
        
            #get source Id for future API calls
            source_id_vars['reportCode'] = report_code

            source_id, valid_data = warcraftLogAPI.getSourceID(source_id_query, source_id_vars, auth_token, player_name)

            if valid_data:
                #get parse Rank associated with current report code
                parse_rank_vars['charName'] = player_name
                parse_rank_vars['serRegion'] = server_region
                parse_rank_vars['serSlug'] = server
                parse_rank_vars['ID'] = encounterID_map['patchwork']
                parseRank = warcraftLogAPI.getParseRank(parse_rank_query, parse_rank_vars, auth_token, report_code)
                
                if parseRank == -1:
                    parseRank = oldParseRank
                parse_data.append(parseRank)
                parse_data.append(total_dps)
                parse_data.append(log['duration'])
                #figure out time
                start_time = log['startTime'] - log['report']['startTime']
                end_time = start_time + log['duration']

                # get stat info
                damage_summary_vars['reportCode'] = report_code
                damage_summary_vars['start'] = start_time
                damage_summary_vars['end'] = end_time
                damage_summary_vars['ID'] = source_id
            # stat_info = warcraftLogAPI.apiCall(stat_info_query, damage_summary_vars, auth_token)
                
                # get damage info
                damage_summary = warcraftLogAPI.apiCall(damage_summary_query, damage_summary_vars, auth_token)
                #print(damage_summary)
                damage_summary_data = readDamageDone.damageSummary(damage_summary, log['duration'])

                parse_data.extend(damage_summary_data)
                # store info 
            
                full_parse_data_list.append(parse_data)

            oldParseRank = parseRank

        #write to file
    print("writing dmg to file")
    readDamageDone.writeToFile('damageDone.csv', full_parse_data_list)
    print("done")
   
raw_data_file = 'damageDone.csv'
# normalize
normalize_file = "normTest.csv"
if normalize_logs:
    normalize.normalize(raw_data_file, normalize_file)
    print("done normalizing")
b =2
# PCA

pca.pca(normalize_file)
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
