import math
import random
import sys

import pandas as pd
import scipy.stats as stat

random.seed(0)


def perform_t_test(alg1, alg2):
    data = pd.read_csv("results_Combination_layouts.csv")

    algorithm = data[data.columns[1]].tolist()
    nodes = data[data.columns[2]].tolist()

    unique_algo = set(algorithm)
    uniquelist = list(unique_algo)

    nodes_expanded = dict(zip(uniquelist, ([] for _ in uniquelist)))

    for algo, no_nodes in zip(algorithm, nodes):
        if math.isnan(no_nodes):
            nodes_expanded[algo].append(0)
        else:
            nodes_expanded[algo].append(no_nodes)

    for keys, val in nodes_expanded.items():
        nodes_list = nodes_expanded[keys]
        zeroes_index = [i for i, e in enumerate(nodes_list) if e == 0]

        for algos, _ in nodes_expanded.items():
            nodes_expanded_list = nodes_expanded[algos]
            indicesList = sorted(zeroes_index, reverse=True)
            for indx in indicesList:
                if indx < len(nodes_expanded_list):
                    nodes_expanded_list.pop(indx)

    index_list = random.sample(range(0, len(nodes_expanded[alg1])), 50)

    first_algo = list(map(nodes_expanded[alg1].__getitem__, index_list))

    second_algo = list(map(nodes_expanded[alg2].__getitem__, index_list))

    t_val, p_val = stat.ttest_rel(first_algo, second_algo, nan_policy='omit')
    print("P value for {0} and {1} is {2}".format(alg1, alg2, str(p_val)))


if __name__ == '__main__':
    alg1, alg2 = sys.argv[1], sys.argv[2]
    perform_t_test(alg1, alg2)
