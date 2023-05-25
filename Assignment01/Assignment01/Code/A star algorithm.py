import JumpingFrogs
from Route_Planning import RoutePlanning
from JumpingFrogs import Jumping_Frogs
from util import PriorityQueue

def get_action_path(path_dict, state):
    i = 0
    current_state = state
    traversal = list()

    while current_state != None:
        traversal.append(current_state)
        current_state = (path_dict[tuple(current_state)]) #This step is performing back_track
        i +=1
    traversal.reverse()
    print(f"The length of path {i}")
    return traversal



def aStarSearch(problem:RoutePlanning):
    
    start = problem.start


    goal = problem.Goal
    front_tier = PriorityQueue() # will contain the front teir nodes 
    front_tier.push(start, 0) #pushing the start state with priority = 0

    path = []
    CLOSED = [] #Nodes that have already been visited
    actions_so_far = [] 
    path = dict()
    gn_map = dict()

    path[tuple(start)] = None
    gn_map[tuple(start)] = 0 

    while not front_tier.isEmpty():
        _ ,current = (front_tier.pop()) #priority, current state
        CLOSED.append(current) 
      
        
        
        successors = problem.getSuccessors(current)

        for neighbor, action,per_step_cost in successors:
            
            if not tuple(neighbor) in path.keys():
                path[tuple(neighbor)] = current

            problem.curr = current
            gn = gn_map[tuple(current)] +  per_step_cost
            fn  = gn + problem.getHeuristic(neighbor)
            
            try:
                if neighbor in CLOSED and  gn_map[neighbor] < gn:
                    CLOSED.remove(neighbor)
                if  tuple(neighbor) not in gn_map.keys() :
                    gn_map[tuple(neighbor)] = gn
                    path[tuple(neighbor)] = current
                    front_tier.push(neighbor, fn)
                elif gn < gn_map[tuple(neighbor)]:
                    gn_map[tuple(neighbor)] = gn
                    path[tuple(neighbor)] = current
                    front_tier.push(neighbor, fn)   
                


            except:
                continue
        if problem.isGoalState(current):
            print("This")
            break

    return get_action_path(path, goal)

RPproblem = RoutePlanning()
# JF = Jumping_Frogs()


print(aStarSearch(RPproblem))
# print(aStarSearch(JF))