from replay_grabber import get_replay_data
from Information import cluster_template, cluster_max_values, sample_replay

print(get_replay_data(sample_replay))

def get_team_average(category, value, team, replay_data):
    average = 0
    teammates = 0
    for i in replay_data[team]['players']:
        average += i['stats'][category][value]
        teammates += 1
    return average / teammates

def get_team_total(category, value, team, replay_data):
    total = 0
    for i in replay_data[team]['players']:
        total += i['stats'][category][value]
    return total

def calc_num_position(replay_data):
    results = {}

    factor_amount = 2
    p_stats = replay_data['stats']['positioning']

    in_off = p_stats['percent_offensive_third']
    in_mid = p_stats['percent_neutral_third']
    in_def = p_stats['percent_defensive_third']

    attacker = p_stats["percent_most_forward"]
    waiting = 100 - (p_stats["percent_most_forward"] + p_stats["percent_most_back"])
    defender = p_stats["percent_most_back"]

    results['1st Man'] = (attacker)/100
    results["2nd Man"] = (waiting)/100
    results["3rd Man"] = (defender)/100
    return results

def calc_stiker_value(replay_data, team, full_data):
    factor_amount = 2
    c_stats = replay_data['stats']['core']

    goals = c_stats['goals']
    goal_percent = goals / get_team_total('core', 'goals', team, full_data)

    shots = c_stats['shots']
    shot_percent = shots / get_team_total('core', 'shots', team, full_data)

    total = goal_percent + shot_percent

    return total / factor_amount

def calc_anchor_value(replay_data, team, full_data):
    factor_amount = 2
    c_stats = replay_data['stats']['core']

    saves = c_stats['saves']
    save_percent = saves / get_team_total('core', 'saves', team, full_data)

    shots_denied = c_stats['shots_against']
    shot_denied_percent = shots_denied / get_team_total('core', 'shots_against', team, full_data)

    total = save_percent + shot_denied_percent

    return total / factor_amount

def calculate_playstyles(replay_data):
    player_playstyles = {}

    # Blue team calulcations
    for i in replay_data['blue']['players']:
        # calculation
        man_results = calc_num_position(i)
        strike_results = calc_stiker_value(i, 'blue', replay_data)
        anchor_results = calc_anchor_value(i, 'blue', replay_data)

        # sets
        player_playstyles[i["name"]] = {
            "Team": "Blue",
            "Stats": {
                "Anchor": anchor_results,
                "Striker": strike_results,
                "1st Man": man_results["1st Man"],
                "2nd Man": man_results["2nd Man"],
                "3rd Man": man_results["3rd Man"]
            }
        }

    # Orange team calulcations
        for i in replay_data['orange']['players']:
            man_results = calc_num_position(i)
            strike_results = calc_stiker_value(i, 'orange', replay_data)
            anchor_results = calc_anchor_value(i, 'orange', replay_data)

            # sets
            player_playstyles[i["name"]] = {
                "Team":"Orange",
                "Stats":{
                    "Anchor": anchor_results,
                    "Striker": strike_results,
                    "1st Man": man_results["1st Man"],
                    "2nd Man": man_results["2nd Man"],
                    "3rd Man": man_results["3rd Man"]
                }
            }

    return player_playstyles
