import os
import csv
import sys
import time
from subprocess import Popen, PIPE, STDOUT
import generateLayout as multiple_layouts

def getAllLayouts(comb):
    if comb:
        obj = os.scandir('1.search/layouts/Combination')
    else:
        obj = os.scandir('1.search/layouts')
    layouts = []
    for entry in obj:
        if entry.is_file():
            layouts.append(entry.name.split('.')[0])
    return layouts


def writeToCsvFile(comb,object={}):
    if comb:
        filename = 'results_Combination_layouts.csv'
    else:
        filename = 'results_given_layouts.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["Layout Name", "Algorithm",
                   "Nodes Expanded", "Path Cost"])
        for layoutName in object.keys():
            for algorithm in object[layoutName].keys():
                w.writerow([layoutName, algorithm, object[layoutName][algorithm]
                           ['nodes_expanded'], object[layoutName][algorithm]['path_cost']])


def getExtractedInfo(outputStr=''):
    outputArray = outputStr.split('\n')
    nodes_expanded = 'N/A'
    path_cost = 'N/A'
    for eachLine in outputArray:
        if 'Search nodes expanded:' in eachLine:
            nodes_expanded = eachLine.split(': ')[1].lstrip()
        elif 'Path found ' in eachLine:
            path_cost = eachLine.split(' ')[6].lstrip()
    return {
        "nodes_expanded": nodes_expanded,
        "path_cost": path_cost
    }


def runFunction(comb):
    finalResult = {}
    algorithms = ['dfs', 'bfs', 'astar', 'ucs', 'mm', 'mm0']
    layouts = getAllLayouts(comb)
    for layout in layouts:
        for algorithm in algorithms:
            if comb:
                cmd = "python pacman.py -l /Combination/" + layout + " -p SearchAgent -a fn=" + \
                      algorithm + ",prob=PositionSearchProblem,heuristic=manhattanHeuristic -q"
                if algorithm == 'mm0':
                    cmd = "python pacman.py -l /Combination/" + layout + \
                          " -p SearchAgent -a fn=mm,prob=PositionSearchProblem -q"
            else:
                cmd = "python pacman.py -l " + layout + " -p SearchAgent -a fn=" + \
                    algorithm + ",prob=PositionSearchProblem,heuristic=manhattanHeuristic -q"
                if algorithm == 'mm0':
                    cmd = "python pacman.py -l " + layout + \
                        " -p SearchAgent -a fn=mm,prob=PositionSearchProblem -q"
            proc = Popen(cmd.split(' '), stdout=PIPE,
                         stderr=PIPE, cwd='1.search')

            (output, error) = proc.communicate()

            extractedInfo = getExtractedInfo(output.decode("utf-8"))
            if not layout in finalResult:
                finalResult[layout] = {}
            finalResult[layout][algorithm] = extractedInfo

            print(layout, 'and', algorithm, 'execution completed!')
            if error:
                pass
    writeToCsvFile(comb,finalResult)


if __name__ == '__main__':
    start = time.time()
    comb = True
    args = sys.argv[1]
    if args == "-y":
        multiple_layouts.main_fn()
        runFunction(comb)
    elif args == "-n":
        comb = False
        runFunction(comb)
    end = time.time()

print("Time in minutes : {0}".format((end-start)/60))
print("\n\n\n  ************** Script execution completed! ************** \n\n\n")
