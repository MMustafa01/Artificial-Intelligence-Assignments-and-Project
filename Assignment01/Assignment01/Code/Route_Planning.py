from time import process_time_ns
from util import PriorityQueue
import util
from search import SearchProblem
import pandas as pd





class RoutePlanning(SearchProblem):
    def __init__(self):
        self.cities, self.city_graph = self.get_graph()
        self.heuristic = self.heuristic()
        self.start =  self.getStartState()
        self.Goal = self.getGoalState()
        self.curr = self.start


    def get_graph(self):
        cities_df = pd.read_csv(r'CSV\cities.csv')
        df = pd.read_csv(r'CSV\Connections.csv')
        # 
        cities = ["Islamabad"] + (list(cities_df["Islamabad"]))
        # print(f"This is the cities {cities}" )
        graph = {}
        # print(cities, len(cities))
        # print(list(cities_df.loc()[0]))
        for i in range(len(cities)):
            conn_list = list(df.loc()[i])
            node = conn_list[0]
            if not node in cities:
                print(f"There seems to be a problem in the data")
            
            for j in range(1,len(conn_list)):
                try:
                    graph[node] += [(cities[j-1], conn_list[j])]
                except:
                    graph[node] = [(cities[j-1], conn_list[j])]
        return cities,graph


    def heuristic(self):
        cities_df = pd.read_csv(r'CSV\cities.csv')
        hn_df = pd.read_csv(r'CSV\heuristics.csv')
        cities = ["Islamabad"] + (list(cities_df["Islamabad"]))
        graph = {}
        # print(cities, len(cities))
        # print(list(cities_df.loc()[0]))
        for i in range(len(cities)):
            conn_list = list(hn_df.loc()[i])
            node = conn_list[0]
            if not node in cities:
                print(f"There seems to be a problem in the data")
            
            for j in range(1,len(conn_list)):
                try:
                    graph[node] += [(cities[j-1], conn_list[j])]
                except:
                    graph[node] = [(cities[j-1], conn_list[j])]
            # print(conn_list)                
        return graph    

    def getStartState(self):
        state = input('Please give the start state\n')
        while True:
            if state in self.cities:
                return state
            else:
                state = input("Please make sure that the state is correct\n")

    def getGoalState(self):
        state = input('Please give the Goal state\n')
        while True:
            if state in self.cities:
                return state
            else:
                state = input("Please make sure that the state is correct\n")
    
    def isGoalState(self, state):
        return state == self.Goal

    def getSuccessors(self, state): #return (state, action, per_step_cost)
        possible = []
        neighbor = self.city_graph[state]
        for successor,per_step_cost in neighbor:
            if successor == state or per_step_cost == -1:
                continue
            action = (state, successor)
            possible.append((successor, action, per_step_cost))
        return tuple(possible)

    def getHeuristic(self, state):
        estimation = self.heuristic[self.curr] 
        for node, hn in estimation:
            if node == state:
                return hn 
        print("There seems to be an error in the given data")

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



# def aStarSearch(problem:RoutePlanning):
    
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

# problem = RoutePlanning()

# print(aStarSearch(problem))






