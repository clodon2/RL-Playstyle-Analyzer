import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

player_attributes = ["1st Man", "2nd Man", "3rd Man", "Anchor", "Striker"]
p_colors = ['red', 'blue', 'gray']
testing_data = [
    ("Player 1", [.1, .5, .1, .8, .3]),
    ("Player 5", [.5, .5, .5, .5, .5])
]

multi_test = [
    [
        ("Player 1", [.1, .5, .1, .8, .3]),
        ("Player 5", [.5, .5, .5, .5, .5]),
        ("Player 4", [.3, .1, .4, .2, .4])
    ],
    [
        ("Player 3", [.1, .5, .9, .8, .3]),
        ("Player 2", [.5, .5, .5, .9, .5]),
        ("Player 6", [.3, .1, .4, .2, .4])
    ]
]

def generate_single_chart(title, data, areas=player_attributes, data_colors=p_colors,
                          r_values=[0.2, 0.4, 0.6, 0.8, 1]):
    angles=np.linspace(0,2*np.pi,len(areas), endpoint=False)

    angles=np.concatenate((angles,[angles[0]]))

    areas.append(areas[0])

    print(angles)

    # needed to create final line
    for p, s in data:
        print(p, s)
        s.append(s[0])

    fig=plt.figure(figsize=(6,6))
    ax=fig.add_subplot(111, polar=True)
    #Alice Plot
    for player, color in zip(data, data_colors):
        p_name = player[0]
        stats = player[1]
        ax.plot(angles, stats, 'o-', color=color, linewidth=.8, label=p_name)
        ax.fill(angles, stats, alpha=0.2, color=color)

    # sets labels
    ax.set_thetagrids(angles * 180/np.pi, areas, horizontalalignment='center')
    # rotates so degree 0 is straight up
    ax.set_theta_zero_location("N")
    # sets max values and radial increments
    ax.set_rgrids(r_values)
    # sets area label margin from graph
    ax.set_rlabel_position(180)
    # sets title
    ax.set_title(title, weight='bold', size='large', position=(0.5, 0),
                     horizontalalignment='center')

    plt.grid(True)
    plt.legend(loc=(.9, .95))
    plt.show()

def generate_multi_chart(data, data_titles=["Blue Team", "Orange Team"],
                         areas=player_attributes, data_colors=p_colors,
                          r_values=[0.2, 0.4, 0.6, 0.8, 1], graphs_title="Unknown",
                         dif_data_colors=False, fill=True):

    angles=np.linspace(0,2*np.pi,len(areas), endpoint=False)

    angles=np.concatenate((angles,[angles[0]]))

    areas.append(areas[0])

    # needed to create final line
    for team in data:
        for p, s in team:
            s.append(s[0])

    fig=plt.figure(figsize=(10,5))
    fig.subplots_adjust(wspace=1, hspace=0, top=0.85, bottom=0.05)
    # plots
    plot_pos = 0
    for team in data:
        plot_pos += 1
        ax=fig.add_subplot(int(f"12{plot_pos}"), polar=True)
        # changes color set for next graph
        if dif_data_colors:
            data_colors = dif_data_colors[plot_pos - 1]
        for player, color in zip(team, data_colors):
            p_name = player[0]
            stats = player[1]
            ax.plot(angles, stats, 'o-', color=color, linewidth=.8, marker='.',
                    label=p_name)
            if fill:
                ax.fill(angles, stats, alpha=0.2, color=color)

            # sets labels
            ax.set_thetagrids(angles * 180/np.pi, areas, horizontalalignment='center')
            # rotates so degree 0 is straight up
            ax.set_theta_zero_location("N")
            # sets max values and radial increments
            ax.set_rgrids(r_values)
            # sets area label margin from graph
            ax.set_rlabel_position(180)
            # sets title
            ax.set_title(data_titles[plot_pos - 1], weight='bold', size='large', position=(0.5, 0),
                             horizontalalignment='center')
            # sets legend
            ax.legend(loc=(.9, .95))

    fig.text(0.5, 0.965, f'{graphs_title} Playstyles Graph',
             horizontalalignment='center', color='black', weight='bold',
             size='large')
    plt.grid(True)
    plt.show()