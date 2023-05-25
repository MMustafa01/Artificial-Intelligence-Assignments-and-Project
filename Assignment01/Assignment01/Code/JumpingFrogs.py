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

from util import PriorityQueue
import util
from search import SearchProblem


class Jumping_Frogs(SearchProblem):
    '''
    This class needs an __init__() method. And the class needs the following attributes:
    1) self.goal_node
    2) Self.visited = []
    3) Self.front_tier = priorityqueue()
    4) self.closed = []
    
    '''
    def __init__(self):
        self.Goal =['B','B','B','','Y','Y','Y' ]
        self.curr = self.getStartState()
        self.start = self.getStartState()


    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return ['Y','Y','Y','','B','B','B']       
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        
        Returns True if and only if the state is a valid goal state.
        """

        if ['B','B','B','','Y','Y','Y' ] == state:   
            return True
        else:
            return False

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        

        possible = []
        # state = ['B','B','Y','Y','B','Y','']
        # print(f"The current state: \n \n{state} \n")
        ri = state.index('') #ri == Rock Index
        actions = [(ri, ri + 1),(ri, ri + 2),(ri, ri - 1),(ri, ri - 2)] 
        # Action is a tuple that specifies (index of rock in curr state, index of rock in new state)
        # [(Brown moves 1 left), (Brown moves 2 left), (Yellow moves 1 right), (Yellow moves 2 right)]
        # print(f"ri = {ri}")

        ############## Checking for all possible moves ###################
        for i in range(len(actions)):
            new_state = state.copy() 
            # new_state = state

            if i == 0 or i == 1:
                try: 
                    if state[ri + i + 1] == 'B':
                        new_state[ri + i + 1] = ''
                        new_state[ri] = 'B'
                        cost = i+1

                        possible.append((new_state, actions[i], cost))


                    
                except:
                    # print(f"The action = {actions[i]} is out of range")
                    continue
            elif i == 2 or i == 3:
                try: 
                    if state[ri - i + 1] == 'Y':
                        new_state[ri - i + 1] = ''
                        new_state[ri] = 'Y'
                        cost = i-1

                        possible.append((new_state, actions[i], cost))


                except:
                    # print(f"The action = {actions[i]} is out of range")
                    continue




        # print(f"\nThe possible states are: \n{possible}\n")
        if len(possible) == 0:
            # print("No more possible moves")
            return [(state,(ri,ri), 0)]
        return possible
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        # """
        #  actions: A list of actions to take

        # This method returns the total cost of a particular sequence of actions.
        # The sequence must be composed of legal moves.
        # Action List:  [( , )]
        # """
        # cost = 0
        # for action in actions:
        #     cost += abs(action[1] - action[0])
        # return cost
        # # This method will only return sum(g(n)) for all values of n in the path
        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        # For the jumpting frog h(n) = number of matching elements in the current state and the goal state
        hn = 0
        goal_state =  ['B','B','B','','Y','Y','Y' ]
        # print(f"The sate = \t {state} \n the goal state{goal_state}")


        for i in range(len(goal_state)):
            if goal_state[i] == state[i]:
                hn += 1
        return 7-hn    


        util.raiseNotDefined()





# def get_action_path(path_dict:dict, state):
#     i = 0
#     current_state = state
#     traversal = list()

#     while current_state != None:
#         traversal.append(current_state)
#         current_state = (path_dict[tuple(current_state)])
#         i +=1
#     traversal.reverse()
#     print(f"The length of path {i}")
#     return traversal


# def aStarSearch(problem:Jumping_Frogs):
    
#     start = problem.start


#     # print(start)

#     goal = problem.Goal
#     front_tier = PriorityQueue() # will contain the front teir nodes 
#     front_tier.push(start, 0) #pushing the start state with priority = 0
#     print(front_tier)



#     path = []
#     CLOSED = [] #Nodes that have already been visited
#     actions_so_far = [] 
#     path = dict()
#     cost_dict = dict()

#     path[tuple(start)] = None
#     cost_dict[tuple(start)] = 0 


#     i =0




#     while not front_tier.isEmpty():
#         _ ,current = (front_tier.pop()) #priority, current state
#         CLOSED.append(current) 




        
#         if problem.isGoalState(current):
#             break
        
#         successors = problem.getSuccessors(current)

#         for neighbor, action,per_step_cost in successors:
            
#             if not tuple(neighbor) in path.keys():
#                 path[tuple(neighbor)] = current

#             problem.curr = current
#             gn = cost_dict[tuple(current)] +  per_step_cost
#             fn  = gn + problem.getHeuristic(neighbor)
            
#             try:
#                 if  tuple(neighbor) not in cost_dict.keys() :
#                     cost_dict[tuple(neighbor)] = gn
#                     path[tuple(neighbor)] = current
#                     front_tier.push(neighbor, fn)
#                 elif gn < cost_dict[tuple(neighbor)]:
#                     cost_dict[tuple(neighbor)] = gn
#                     path[tuple(neighbor)] = current
#                     front_tier.push(neighbor, fn)   
#                 # elif neighbor in CLOSED and  cost_dict[neighbor] < gn: 


#             except:
#                 continue
#     return get_action_path(path, goal)

# problem = Jumping_Frogs()

# print(aStarSearch(problem))



