# network model
# node IDs start with 0 and go up to (# nodes - 1)

import ConfigParser
import sys
sys.path.append('..')
from util import ConfigSectionMap

import random
from node import Node

class Network:

    def __init__(self,Config,cascade,random):
        'initialize network nodes'

        self.numNodes = int(ConfigSectionMap(Config, "NetworkParameters")["numnodes"])
        edgeProb = float(ConfigSectionMap(Config, "NetworkParameters")["edgeprob"])
        self.nodes = []
        self.changed = []
        self.cascadeModel = cascade

        # initialize adjacency matrix
        self.adjacencyMatrix = [[0 for x in xrange(self.numNodes)] for x in xrange(self.numNodes)]
        for i in range(0,self.numNodes):
            self.nodes.append(Node(i))
            self.nodes[i].save()

        # generate network edges
        for i in range(0,self.numNodes):
            for j in range(i+1,self.numNodes):
                if (random.random() <= edgeProb):
                    self.adjacencyMatrix[i][j] = 1
                    self.adjacencyMatrix[j][i] = 1
                

    def update(self,nodeIndeces):
        # save current status of all nodes

        self.changed = []
        
        # change status of all specified nodes to adopt
        for i in nodeIndeces:
            if not self.nodes[i].adopted():
                self.nodes[i].save()
                self.nodes[i].adopt()
                self.changed.append(i)

        return self.cascadeModel.diffuse(self)

    def reverse(self):        
        # reverses network state to what it was before the last call to update
        for n in self.changed:
            self.nodes[n].reverse()

    def getNeighbors(self,nodeIndex):
        # return the set of neighbor (node ids)
        nbrs = []
        for i in range(0,self.numNodes):
            if self.adjacencyMatrix[i][nodeIndex] == 1:
                nbrs.append(i)

        return nbrs

    def reset(self):
        # reset the adoption process to
        # make all nodes "unadopt"
        for n in self.nodes:
            n.unadopt()

    def size(self):
        # returns the # of nodes
        return self.numNodes
                
    def display(self):
        for i in range(0,self.numNodes):
            print "[",i,": ",self.nodes[i].getStatus(),"]"

    def degree(self, node):
        # returns degree (# of neighbors) of the specified node (ID)
        deg = 0
        for i in range(0,len(self.nodes)):
            deg += self.adjacencyMatrix[node][i]

        return deg

    def maxDegree(self):
        # returns the maximum degree in the network
        maxd = self.degree(0)
        for i in range(1,len(self.nodes)):
            d = self.degree(i)
            if (d > maxd):
                maxd = d

        return maxd
