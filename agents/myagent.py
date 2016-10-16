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

        #testing Christina
        print "testing"
        for p in nodeNeighbors: print p
        print "End of 50 nodes"

        # initialize the "Frontier" 
        frontier = Frontier()

        # initialize selected nodes
        x = []

        for i in range(numNodes):
            x.append(0)

        best = tuple(x)
        bestVal = 0
        
        #testing Christina
        print "This is what x starts as"
        for p in x: print p
            
        ### your code goes here ###
        # [ NOTE: fill in where necessary ]

        #testing what expanding node 1 does
        print "testing result of expanding node 1" 
        nodes=self.expand(1);
        for p in nodes: print p
            
            
        while not frontier.empty():
            for i in range(numNodes):
            
        

           

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

        #I am not sure why this expand method is necessary when we can just use the getNeighbors from the networks.py file
        #I can't do that here since networks is not a param, but I can do it in the above section
        #network.getNeighbors(x); 
        
    
        
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

