# You will implement this class
# At the minimum, you need to implement the selectNodes function
# If you override __init__ from the agent superclass, make sure that the interface remains identical as in agent; 
# otherwise your agent will fail

from agent import Agent

from collections import deque
import copy
from sets import Set

class Frontier:
    
    def __init__(self):
        self.nodes = deque()

    def pop(self):
        return self.nodes.popleft()

    def pushback(self, x):
        self.nodes.append(x)

    def pushbacklist(self, xlist):
        for x in xlist:
            self.pushback(x)

    def pushfront(self, x):
        self.nodes.appendleft(x)

    def pushfrontlist(self, xlist):
        for x in xlist:
            self.pushfront(x)

    def empty(self):
        return not self.nodes

class MyAgent(Agent):

    def selectNodes(self, network):
        """ 
        select a subset of nodes (up to budget) to seed
        nodes in the network are selected *** BY THEIR INDEX ***
        """
        
        numNodes = network.size()
        
        selected = []

        # store the set of neighbors for each node
        nodeNeighbors = []
        for i in range(numNodes):
            nbrs = Set(network.getNeighbors(i))
            nbrs.add(i)
            nodeNeighbors.append(nbrs)

        # initialize the "Frontier" 
        frontier = Frontier()

        # initialize selected nodes
        x = []

        for i in range(numNodes):
            x.append(0)

        best = tuple(x)
        bestVal = 0
            
        ### your code goes here ###
        # [ NOTE: fill in where necessary ]
                
        while not frontier.empty():

            # take the front element from the frontier
            x = frontier.pop()

            # manage frontier and branch-and-bound search
            # prune nodes (and subtrees) as needed

                    while not frontier.empty():

            # take the front element from the frontier
            x = frontier.pop()

            # manage frontier and branch-and-bound search
            # prune nodes (and subtrees) as needed


        #using A* search--Christina
        frontier = util.PriorityQueue()
        frontier.push([problem.getStartState()], 0)
        came_from = {}
        cost_so_far = {}
        #came_from[problem.getStartState()] = None
        cost_so_far[problem.getStartState()] = 0
        solution = []

        while not frontier.isEmpty():
            current = frontier.pop()
            print 'current: ', current
            if problem.isGoalState(current[0]):
                # return solution
                here = current
                solution.append(here[1])
                # print 'CAME_FROM: ', came_from
                print here, ' came from ', came_from[here[0]]
                while came_from[here[0]][0] != problem.getStartState():
                    here = came_from[here[0]]
                    solution.append(here[1])
                # print 'solution: ', solution
                return list(reversed(solution))
            for child in problem.getSuccessors(current[0]):
                new_cost = cost_so_far[current[0]] + child[2]
                if child[0] not in cost_so_far or new_cost < cost_so_far[child[0]]:
                    cost_so_far[child[0]] = new_cost
                    priority = new_cost + heuristic(child[0], problem)
                    frontier.push(child, priority)
                    came_from[child[0]] = current

        ### end your code ###

        for i in range(numNodes):
            if (best[i] == 1):
                selected.append(i)
                
        return selected

    def expand(self, x):
        """
        expand a node in the tree
        
        returns children of this node in the search tree
        """
        
        nodes = []

        ### your code goes here  ####
        
        nodes=self.Network.getNeighbors(); #Christina
        
        
            ### end your code  ###

            return nodes

    def eval(self, nodeNeighbors, x):
        """
        evaluate the value of node x
        nodeNeighbors is an auxiliary data structure
        keeping track of sets of neighbors for each node
        """
        
        nbrs = Set()
        for i in range(len(x)):
            if x[i] == 1:
                for j in nodeNeighbors[i]:
                    nbrs.add(j)

        return len(nbrs)
    
    def display():
        print "Agent ID ", self.id

