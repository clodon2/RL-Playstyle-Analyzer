from playstyle_calculations import calculate_playstyles
from replay_grabber import get_replay_data
from Information import sample_replay

def final_values(player):
    raw_values = calculate_playstyles(get_replay_data(sample_replay))
    print(raw_values)
    data_values = []
    data_names = []
    for i in raw_values[player]['Stats']:
        data_values.append(raw_values[player]['Stats'][i])
        data_names.append(i)

    return data_values, data_names