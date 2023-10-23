import requests
import json

API_KEY = "RGAPI-ee96dbab-9b06-456a-ab15-9cd19fae58ac"

path_to_ids = "./lol-draft-predict_gg-c9\data_parsing\data\soloqueue_ids.txt"

# Initialize an empty dictionary
name_dict = {}
puuids = {}
soloq_data = {}
# Open and read the text file
with open(path_to_ids, 'r') as file:
    for line in file:
        # Split each line by the "-" character
        parts = line.strip().split('-')
        
        # Ensure there are two parts
        if len(parts) == 2:
            name = parts[0].strip()
            value = parts[1].strip()
            
            # Add the name and value to the dictionary
            name_dict[name] = value
            soloq_data[name] = {}

for key, value in name_dict.items():
    # Construct the API URL with the summoner name
    api_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{value}?api_key={API_KEY}'

    # Send a GET request to the API URL
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        summoner_info = response.json()

        # Access the desired information from the JSON response
        puu_id = summoner_info['puuid']
        puuids[key] = puu_id
        gamecount = 0;
        match_url = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puu_id}/ids?start={gamecount}&count=20&api_key={API_KEY}'
        match_response = requests.get(match_url)
        if match_response.json():
            #Parse MatchIDS and get information
            for element in match_response.json():
                game_url = f'https://asia.api.riotgames.com/lol/match/v5/matches/{element}?api_key={API_KEY}'
                data_response = requests.get(game_url)
                match_data = data_response.json()
                # Find the participant data for the specified puuid
                for participant in match_data['info']['participants']:
                    if participant['puuid'] == puu_id:
                        champion_id = participant['championName']
                        win_status = participant['win']
                        if champion_id not in soloq_data[key]:
                            soloq_data[key][champion_id] = [0,0]
                        if win_status:
                            soloq_data[key][champion_id][0] += 1
                        else: 
                            soloq_data[key][champion_id][1] += 1
            match_response = requests.get(match_url)
    else:
        # Handle the case when the request is not successful
        print(f"Failed to retrieve data for {value}. Status code: {response.status_code}")

print(soloq_data)

with open('soloq_data.txt','w') as file:
    file.write(json.dumps(soloq_data))