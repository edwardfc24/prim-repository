#class Prim:

#     def __init__(self):
#        self.nodes = {}
#        self.order = {}

#    def prepare_structure(self, node):
#        self.nodes[node] = node
#        self.order[node] = 0

#    def find_node(self, node):
#        if self.nodes[node] != node:
#            self.nodes[node] = self.find_node(self.nodes[node])
#        return self.nodes[node]

#    def verify_union(self, origin, destination):
#        init_node = self.find_node(origin)
#        final_node = self.find_node(destination)
#        if init_node != final_node:
#            if self.order[init_node] > self.order[final_node]:
#                self.nodes[final_node] = init_node
#            else:
#                self.nodes[init_node] = final_node
#                if self.order[init_node] == self.order[final_node]:
#                    self.order[final_node] += 1

# nodes ['a', 'b', 'c', ..... , 'z']
# edges ['a', 'g', 2]

#    def apply_prim(self, nodes, edges):
#        met = [] #Arbol de expansion minima
#        for node in nodes:
#            self.prepare_structure(node)

