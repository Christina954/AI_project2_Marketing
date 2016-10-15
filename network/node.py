
class Node:
    'a node in a network'

    def __init__(self,nodeId,initStatus=0):
        self.id = nodeId
        self.status = initStatus
        self.savedStatus = initStatus

    def updateStatus(self,status):
        #update status as specified
        self.status = status

    def resetStatus(self):
        #set to default status, which is 0 (non-adopter)
        self.status = 0

    def save(self):
        # saves current status
        self.savedStatus = self.status
        
    def reverse(self):
        # resets the node state to last saved version
        self.status = self.savedStatus
        
    def adopt(self):
        # set status to "adopt"
        self.status = 1

    def unadopt(self):
        # set status to "unadopt"
        self.status = 0

    def adopted(self):
        # return True iff adopted
        if self.status == 1:
            return True
        else:
            return False

    def getStatus(self):
        # return the adoption status
        return self.status

    def display(self):
        print "nodeId: ", self.id, " status: ", self.status
