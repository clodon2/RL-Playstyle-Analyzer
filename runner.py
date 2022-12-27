from playstyle_calculations import calculate_playstyles
from replay_grabber import get_replay_data, get_replay_title
from Information import sample_replay, replays
from graph_display import generate_multi_chart

def graph_all(replay):
    data = get_replay_data(replay)
    all_data = data[1]
    calc_data = data[0]
    print(all_data)
    playstyle_vals = calculate_playstyles(all_data)
    print(playstyle_vals)
    generate_multi_chart(playstyle_vals, graphs_title=all_data["title"])

graph_all(replays[2])