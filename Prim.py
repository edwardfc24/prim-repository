from operator import itemgetter

class Prim:

    def __init__(self):
        self.nodes = {}
        self.order = {}

    def prepare_structure(self, node): 
        self.nodes[node] = node # {2: 2, 5: 5}
        self.order[node] = 0 # {2: 0, 5:0}

    # {'a': 'd'}
    # {'d': 'd'}
    # {'f': 'd'}
    def find_node(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        return self.nodes[node]

    ## {'a': 0}
    ## {'d': 1}
    ## {'f': 0 }
    # def verify_union(self, origin, destination):
    #     init_node = self.find_node(origin)
    #     final_node = self.find_node(destination)
    #     if init_node != final_node:
    #         if self.order[init_node] > self.order[final_node]:
    #             self.nodes[final_node] = init_node
    #         else:
    #             self.nodes[init_node] = final_node
    #             if self.order[init_node] == self.order[final_node]:
    #                 self.order[final_node] += 1

    # nodes ['a', 'b', 'c'... , 'z']
    # array [ 0 ,  1 , 2]
    # edges ['a', 'g', 2]
    def apply_Prim(self, nodes, edges):
        nodes.sort(key = itemgetter(0))#ordenar los nodos
        origenes =False #origen
        desinos =False #destino
        caunter=0 #contador
        vertices=[] # mi control
        met = [] # Árbol de Expansion Mínima
        # met => [['a', 'd', 5], ['d', 'f', 6]]
        # contador n veces haiga cantidad de nodos
        for node in nodes:
            self.prepare_structure(node)
            caunter+=1
        # contador -3
        caunter-=1
        # Ordenamos las aristas de acuerdo al peso de menor a mayor
        edges.sort(key = itemgetter(2))
        # Agregamos la primera arista
        met.append(edges[0])
        # String origin = edge[0];
        # String destination = edge[1];
        # int weight = edge[2];
        origin, destination, weight = edges[0]
        # registro del control
        vertices.append(origin)
        vertices.append(destination)
        # eliminamos la primera arista puesta
        edges.pop(0)
        # Recorremos las aristas n-2 veces
        while caunter > 0 :
            print(vertices)
            # Recorremos las aristas para determinar el camino más eficiente a todos los nodos
            for edge in edges:
                    # String origin = edge[0];
                    # String destination = edge[1];
                    # int weight = edge[2];
                origin, destination, weight = edge
                origenes =False #origen
                desinos =False #destino
                # por cada vertice si que he guardado comparar con origen y destino
                    # comparo origen
                for aux in vertices:
                    if  origin==(aux):
                        origenes= True
                        # si entra se sale al otro bucle
                        pass
                    # comparo destino
                for aux in vertices:
                    if  destination==(aux):
                        desinos= True
                        # si entra se sale al ver si merece entrar o no
                        pass
                # por medio de o exclusivo se soluciona el proble de ingreso en 
                # cambio de no cumplir vuelve con el sgts edge
                if (origenes==False and desinos==True) or (origenes==True and desinos==False):
                    # registro del control
                    vertices.append(origin)
                    vertices.append(destination)
                    
                    # se agrega a met
                    met.append(edge)
                    # eliminamos la arista puesta
                    edges.remove(edge)
                    # si entra pasa al caunter
                    break
                
                    


                # 
            # para que cumpla la condicion y-1    
            caunter-=1
        return met

    # def review_edge(self, nodes, edges):
    #     met = [] # Árbol de Expansion Mínima
    #     # met => [['a', 'd', 5], ['d', 'f', 6]]
    #     for node in nodes:
    #         self.prepare_structure(node)
    #     # Ordenamos las aristas de acuerdo al peso de menor a mayor
    #     edges.sort(key = itemgetter(0))
    #     # Recorremos las aristas para determinar el camino más eficiente a todos los nodos
    #     for edge in edges:
    #         # String origin = edge[0];
    #         # String destination = edge[1];
    #         # int weight = edge[2];
    #         origin, destination, weight = edge
           
    #         #                   a                            g
    #         if self.find_node(origin) != self.find_node(destination):
    #             self.verify_union(origin, destination)
    #             met.append(edge)
    #     return met