from operator import itemgetter

class Prim:

    def __init__(self):
        self.nodes = {}
        self.order = {}
        self.aristas = [] # Árbol de Expansion Mínima

        self.met = []

    def prepare_structure(self, node): 
        self.nodes[node] = node # {2: 2, 5: 5}
        self.order[node] = 0 # {2: 0, 5:0}

    def find_node(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        return self.nodes[node]

    def verify_union(self, origin, destination):
        init_node = self.find_node(origin)
        final_node = self.find_node(destination)
        if init_node != final_node:
            if self.order[init_node] > self.order[final_node]:
                pass
            else:
                if self.order[init_node] == self.order[final_node]:
                    self.order[final_node] += 1


    def apply_Prim(self, nodes, edges, nodoSelected):
        # met => [['a', 'd', 5], ['d', 'f', 6]]
        for node in nodes:
            self.prepare_structure(node)
        # Ordenamos las aristas de acuerdo al peso de menor a mayor
        edges.sort(key = itemgetter(2))
        # Recorremos las aristas para determinar el camino más eficiente a todos los nodos
        for edge in edges:
            origin, destination, weight = edge
            
            if self.find_node(origin) == self.find_node(nodoSelected) or self.find_node(destination) == self.find_node(nodoSelected):
                # asristas con el valor elegido
                self.aristas.append(edge)
                #Aqui ya encontramos al nodo seleccionado que ser el punto de partida
                print(f"Ya encontre la arista entre estos nodos: {edge}")

        for arista in self.aristas:
            origin, destination, weight = arista

            self.verify_union(origin, destination)
            # validacion 
            
            self.met.append(self.aristas[0])  
            self.aristas.pop(0)
            if self.order[origin] != 1:
                if origin == nodoSelected:
                    nodoSelected = destination
                else:
                    nodoSelected = origin
                    self.nextRoute(edges, nodoSelected)

        return self.met

    def nextRoute(self, edges, nodoSelected):
        for edge in edges:
            origin, destination, weight = edge
            
            if origin == nodoSelected or destination == nodoSelected:
                if self.order[origin] < 1 and self.order[destination] < 1:
                    self.aristas.append(edge)
                    print(f"Ya encontre la arista entre estos nodos: {edge}")
                
        for arista in self.aristas:
            origin, destination, weight = arista
            
            if origin == nodoSelected or destination == nodoSelected:
                self.verify_union(origin, destination)
                self.met.append(arista)  

