import requests

API_KEY = "RGAPI-ee96dbab-9b06-456a-ab15-9cd19fae58ac"

path_to_ids = "./lol-draft-predict_gg-c9\data_parsing\data\soloqueue_ids.txt"

# Initialize an empty dictionary
name_dict = {}
puuids = {}

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
        
    else:
        # Handle the case when the request is not successful
        print(f"Failed to retrieve data for {value}. Status code: {response.status_code}")