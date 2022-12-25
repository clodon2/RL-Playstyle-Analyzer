import requests
import json

# gets the replay information (entire dictionary of values)
def get_replay(replay_id):
    # builds the URL
    trsltsite = "https://ballchasing.com/api/"
    call = "replays/"
    replay = f"{replay_id}"
    fullurl = trsltsite + call + replay
    try:
        response = requests.get(fullurl, headers={'Authorization': 'p2iP2Ds0Ek6kqVKgNN3Im1a6xTIdBx86XQjjdmQy'})
        responsestring = response.content.decode("utf-8")
        output = json.loads(responsestring)
    # prevents crashes from errors, gives user a notification
    except Exception as e:
        output = "API not able to be connected or max tries exceeded. Full error: " + f"{e}"
    return output

# returns only needed information from replay data
def clean_replay_data(replay_dict):
    cleaned_dict = {}
    cleaned_dict['blue'] = replay_dict['blue']
    cleaned_dict['orange'] = replay_dict['orange']
    return cleaned_dict

# get replay information for playstyle calculations
def get_replay_data(replay_id):
    return clean_replay_data(get_replay(replay_id))
