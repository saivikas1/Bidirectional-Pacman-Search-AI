# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack()  # open set
    explored = []  # closed set
    start_state = [problem.getStartState(), []]
    frontier.push(start_state)
    while True:
        if frontier.isEmpty():  # If everything is explored but no solution
            return "No Path"
        cur_node = frontier.pop()
        if problem.isGoalState(cur_node[0]):
            return cur_node[1]
        if cur_node[0] not in explored:  # Add newly visited nodes to closed set
            explored.append(cur_node[0])
            successors = problem.getSuccessors(cur_node[0])
            i = 0
            while (i < len(successors)):
                frontier.push([successors[i][0], cur_node[1] + [successors[i][1]]])
                i += 1
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()  # open set
    explored = []  # closed set
    start_state = [problem.getStartState(), []]
    frontier.push(start_state)
    while True:
        if frontier.isEmpty():
            return "No Path"
        cur_node = frontier.pop()
        if problem.isGoalState(cur_node[0]):
            return cur_node[1]
        if cur_node[0] not in explored:
            explored.append(cur_node[0])
            successors = problem.getSuccessors(cur_node[0])
            i = 0
            while (i < len(successors)):
                frontier.push([successors[i][0], cur_node[1] + [successors[i][1]]])
                i += 1
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    explored = []
    init_cst = 0
    start_state = [problem.getStartState(), [], init_cst]
    frontier.push(start_state, init_cst)
    while True:
        if frontier.isEmpty():
            return "No Path"
        cur_node = frontier.pop()
        if problem.isGoalState(cur_node[0]):
            return cur_node[1]
        if cur_node[0] not in explored:
            explored.append(cur_node[0])
            successors = problem.getSuccessors(cur_node[0])
            i = 0
            while (i < len(successors)):
                frontier.push([successors[i][0], cur_node[1] + [successors[i][1]], cur_node[2] + successors[i][2]],
                              cur_node[2] + successors[i][2])
                i += 1
    util.raiseNotDefined()


def nullHeuristic(state, problem=None, info={}):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    explored = []
    init_cst = 0
    start_state = [problem.getStartState(), [], init_cst]
    frontier.push(start_state, init_cst)
    while True:
        if frontier.isEmpty():
            return "No Path"
        cur_node = frontier.pop()
        if problem.isGoalState(cur_node[0]):
            return cur_node[1]
        if cur_node[0] not in explored:
            explored.append(cur_node[0])
            successors = problem.getSuccessors(cur_node[0])
            i = 0
            while (i < len(successors)):
                frontier.push([successors[i][0], cur_node[1] + [successors[i][1]], cur_node[2] + successors[i][2]],
                              cur_node[2] + successors[i][2] + heuristic(successors[i][0], problem))
                i += 1
    util.raiseNotDefined()



# Function to reset backward path before joining to forward
def reset(path):
    path_lst = []
    i=0
    while(i<len(path)):
        if path[i] == 'South':
            path_lst=['North']+path_lst
        elif path[i] == 'East':
            path_lst=['West']+path_lst
        elif path[i] == 'West':
            path_lst=['East']+path_lst
        elif path[i] == 'North':
            path_lst=['South']+path_lst
        i+=1
    return path_lst

# Function to get minimum value in open and closed
def dicminval(dic):
    return min(dic.values())

def biDirectional(problem, heuristic=nullHeuristic):
    
    direction_check = {'dir': 'forward'} #directionary to check direction of search

    g_forinit = 0 # g forward initial value
    g_bacinit = 0 # g backward initial value

    open_for = util.PriorityQueue() #open set forward search
    open_bac = util.PriorityQueue() #open set backward search

    h_forinit = heuristic(problem.getStartState(), problem, direction_check) #forward search initial heuristic
    prfinit = max((g_forinit + h_forinit), 2 * g_forinit) # start state priority value
    start_node = (problem.getStartState(), [], g_forinit, g_forinit + h_forinit, prfinit) #start node desc
    open_for.push(start_node, prfinit)

    direction_check = {'dir': 'backward'}
    h_bacinit = heuristic(problem.goal, problem, direction_check) #backward search initial heuristic
    prbinit = max((g_bacinit + h_bacinit), 2 * g_bacinit) # goal state priority value
    goal_node = (problem.goal, [], g_bacinit, g_bacinit + h_bacinit, prbinit) #goal node desc
    open_bac.push(goal_node, prbinit)

    U = float('Inf') # cost of the cheapest solution found so far
    eps = 1 #cost of the cheapest edge in the state-space

    closed_for = {} #closed set forward search
    closed_bac = {} #closed set backward search

    g_for = {} #g values for nodes on forward open set
    g_bac = {} #g values for nodes on backward open set
    f_for = {} #f values for nodes on forward open set
    f_bac = {} #f values for nodes on backward open set

    f_for[start_node[0]] = start_node[3]
    g_for[start_node[0]] = start_node[2]

    f_bac[goal_node[0]] = goal_node[3]
    g_bac[goal_node[0]] = goal_node[2]

    while not open_for.isEmpty() and not open_bac.isEmpty():
        prfnode = open_for.lookMin() #search min priority node in open forward set without popping
        prbnode = open_bac.lookMin() #search min priority node in open backward set without popping

        path_for = prfnode[1] #forward open set min priority node path
        path_bac = prbnode[1] #backward open set min priority node path

        C = min(prfnode[-1], prbnode[-1]) #node with min priority explored
        if U <= max(C, dicminval(f_for), dicminval(f_bac), dicminval(g_for) + dicminval(g_bac) + eps): #stopping criteria - whenever better solution is observed
            # Just for the display purpose -- DO NOT REMOVE OR EDIT
            problem.isGoalState(problem.goal)

            return finalPath

        if C == prfnode[-1]: #forward direction expansion
            direction_check = {'dir': 'forward'}
            pres_node = open_for.pop()

            curf_for = f_for[pres_node[0]]
            curg_for = g_for[pres_node[0]]

            # moving node from open to closed list
            del f_for[pres_node[0]]
            del g_for[pres_node[0]]
            closed_for[pres_node[0]] = (pres_node[1], pres_node[2])

            for i in problem.getSuccessors(pres_node[0]):
                if open_for.contains(i[0]): #if node in forward open set
                    if g_for[i[0]] <= curg_for + i[2]: #prev child cost less than current cost
                        continue

                if i[0] in closed_for: #if node in forward closed set
                    if closed_for[i[0]][1] <= curg_for + i[2]: #prev child cost less than current cost
                        continue

                if open_for.contains(i[0]): #if node in forward open set and prev child cost greater than current cost then remove child from open
                    open_for.valremove(i[0])
                    del f_for[i[0]]
                    del g_for[i[0]]

                if i[0] in closed_for: #if node in forward closed set and prev child cost greater than current cost then remove child from closed
                    del closed_for[i[0]]

                g_for[i[0]] = curg_for + i[2] #update g value

                h_forchild = heuristic(i[0], problem, direction_check) #child node heuristic
                prfchild = max((g_for[i[0]] + h_forchild), 2 * g_for[i[0]]) #child node priority
                fchild_node = (i[0], path_for + [i[1]], g_for[i[0]], g_for[i[0]] + h_forchild, prfchild) #child node

                open_for.push(fchild_node, prfchild) #add child node to forward open set

                f_for[i[0]] = g_for[i[0]] + h_forchild

                if open_bac.contains(i[0]): #if node already explored by backward search
                    U = min(U, g_for[i[0]] + g_bac[i[0]])
                    finalPath = fchild_node[1] + reset(open_bac.pathreturn(i[0]))

        else: #backward direction expansion
            direction_check = {'dir': 'backward'}
            pres_node = open_bac.pop()

            curf_bac = f_bac[pres_node[0]]
            curg_bac = g_bac[pres_node[0]]

            # moving node from open to closed list
            del f_bac[pres_node[0]]
            del g_bac[pres_node[0]]
            closed_bac[pres_node[0]] = (pres_node[1], pres_node[2])

            for i in problem.getSuccessors(pres_node[0]):
                if open_bac.contains(i[0]): #if node in backward open set
                    if g_bac[i[0]] <= curg_bac + i[2]: #prev child cost less than current cost
                        continue

                if i[0] in closed_bac: #if node in backward closed set
                    if closed_bac[i[0]][1] <= curg_bac + i[2]: #prev child cost less than current cost
                        continue

                if open_bac.contains(i[0]): #if node in backward open set and prev child cost greater than current cost then remove child from open
                    open_bac.valremove(i[0])
                    del f_bac[i[0]]
                    del g_bac[i[0]]

                if i[0] in closed_bac: #if node in backward closed set and prev child cost greater than current cost then remove child from closed
                    del closed_bac[i[0]]

                g_bac[i[0]] = curg_bac + i[2] #update g value

                h_bacchild = heuristic(i[0], problem, direction_check) #child node heuristic
                prbchild = max((g_bac[i[0]] + h_bacchild), 2 * g_bac[i[0]]) #child node priority
                bchild_node = (i[0], path_bac + [i[1]], g_bac[i[0]], g_bac[i[0]] + h_bacchild, prbchild) #child node

                open_bac.push(bchild_node, prbchild) #add child node to backward open set

                f_bac[i[0]] = g_bac[i[0]] + h_bacchild

                if open_for.contains(i[0]): #if node already explored by forward search
                    U = min(U, g_bac[i[0]] + g_for[i[0]])
                    finalPath = open_for.pathreturn(i[0]) + reset(bchild_node[1])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
mm = biDirectional
