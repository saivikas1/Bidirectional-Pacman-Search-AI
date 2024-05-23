import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')

layout_list = sys.argv[1:]
data = pd.read_csv("results_given_layouts.csv")
layoutName = data[data.columns[0]].tolist()
algorithm = data[data.columns[1]].tolist()
nodes = data[data.columns[2]].tolist()
path_cost = data[data.columns[3]].tolist()

unique_algo = set(layoutName)
uniquelist = list(unique_algo)

given_list = list(layout_list)

nodes_expanded = dict(zip(given_list, ([] for _ in given_list)))

path_cost_dict = dict(zip(given_list, ([] for _ in given_list)))

for layout, algo, nodes_exp, score_obt in zip(layoutName, algorithm, nodes, path_cost):
    if layout in given_list:
        nodes_expanded[layout].append((algo, nodes_exp))
        path_cost_dict[layout].append((algo, score_obt))

df = pd.DataFrame({'Layouts': given_list, 'DFS': [nodes_expanded[i][0][1] for i in given_list],
                   'BFS': [nodes_expanded[i][1][1] for i in given_list]
                      , 'astar': [nodes_expanded[i][2][1] for i in given_list],
                   'ucs': [nodes_expanded[i][3][1] for i in given_list]
                      , 'mm': [nodes_expanded[i][4][1] for i in given_list],
                   'mm0': [nodes_expanded[i][5][1] for i in given_list]})

X_axis = np.arange(len(given_list))
width = 0.15

fig, ax = plt.subplots(figsize=(15, 10))

bar1 = ax.bar(X_axis - 2 * width, df['DFS'], width=width, label='DFS', color='#FF0C29')
bar2 = ax.bar(X_axis - width, df['BFS'], width=width, label='BFS', color='#FF9004')
bar3 = ax.bar(X_axis, df['ucs'], width=width, label='ucs', color='#6290FF')
bar4 = ax.bar(X_axis + width, df['astar'], width=width, label='astar', color='#FF08D7')
bar5 = ax.bar(X_axis + 2 * width, df['mm'], width=width, label='mm', color='#0FE300')
bar6 = ax.bar(X_axis + 3 * width, df['mm0'], width=width, label='mm0', color='#A825FF')

ax.set_xticks(X_axis + width)
ax.set_xticklabels(given_list)
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{bar_value:,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=12)

ax.set_ylabel('Nodes', labelpad=15)
ax.set_xlabel('Layouts', labelpad=15)
ax.set_title('Number of nodes expanded', pad=15)

fig.tight_layout()


df = pd.DataFrame({'Layouts': given_list, 'DFS': [path_cost_dict[i][0][1] for i in given_list],
                   'BFS': [path_cost_dict[i][1][1] for i in given_list]
                      , 'astar': [path_cost_dict[i][2][1] for i in given_list],
                   'ucs': [path_cost_dict[i][3][1] for i in given_list]
                      , 'mm': [path_cost_dict[i][4][1] for i in given_list],
                   'mm0': [path_cost_dict[i][5][1] for i in given_list]})

X_axis = np.arange(len(given_list))
width = 0.15

fig, ax = plt.subplots(figsize=(15, 10))

bar1 = ax.bar(X_axis - 2 * width, df['DFS'], width=width, label='DFS', color='#FF0C29')
bar2 = ax.bar(X_axis - width, df['BFS'], width=width, label='BFS', color='#FF9004')
bar3 = ax.bar(X_axis, df['ucs'], width=width, label='ucs', color='#6290FF')
bar4 = ax.bar(X_axis + width, df['astar'], width=width, label='astar', color='#FF08D7')
bar5 = ax.bar(X_axis + 2 * width, df['mm'], width=width, label='mm', color='#0FE300')
bar6 = ax.bar(X_axis + 3 * width, df['mm0'], width=width, label='mm0', color='#A825FF')

ax.set_xticks(X_axis + width)
ax.set_xticklabels(given_list)
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

for bar in ax.patches:
    bar_value = bar.get_height()
    text = f'{bar_value:,}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + bar_value
    bar_color = bar.get_facecolor()
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=bar_color,
            size=12)

ax.set_ylabel('Path Cost', labelpad=15)
ax.set_xlabel('Layouts', labelpad=15)
ax.set_title('Path Cost', pad=15)

fig.tight_layout()
plt.show()



