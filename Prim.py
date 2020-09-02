from operator import itemgetter

class Prim:

    def __init__(self):
        self.nodes = {}
        self.order = {}

    def prepare_structure(self, node): 
        self.nodes[node] = node # {2: 2, 5: 5}
        self.order[node] = 0 # {2: 0, 5:0}


    def find_node(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        return self.nodes[node]

    def veify_union(self, origin, destination):
        init_node = self.find_node(origin)
        find_node = self
        