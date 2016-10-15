
from cascade import Cascade

class CascadeModel(Cascade):
    'each node chosen to adopt influences exactly 1 neighbor'
    
    def diffuse(self, network):
        inds = []
        for i in range(0,network.numNodes):
            if network.nodes[i].adopted():
                inds.append(i)

        for i in range(0,len(inds)):
            nbrs = network.getNeighbors(inds[i])
            for n in nbrs:
                if not network.nodes[n].adopted():
                    network.nodes[n].save()
                    network.nodes[n].adopt()
                    network.changed.append(n)
                    inds.append(n)

        return len(inds)
