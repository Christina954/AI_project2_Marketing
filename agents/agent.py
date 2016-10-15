# agent implemented by the players is derived from this superclass
# and must override the selectNodes function below
# 

import ConfigParser
import sys
sys.path.append('..')
from util import ConfigSectionMap

class Agent:

    def __init__(self,agentid,Config):
        self.id = agentid
        self.budget = int(ConfigSectionMap(Config, "AgentParameters")["budget"])

    def selectNodes(self, network, t):
        # select a subset of nodes (up to budget) to seed at current time step t
        # nodes in the network are selected *** BY THEIR INDEX ***
        selected = []
        return selected

    def display():
        print "Agent ID ", self.id
