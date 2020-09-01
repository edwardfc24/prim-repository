from Prim import Prim

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
edges = [
    ['a', 'd', 5],
    ['d', 'f', 6],
    ['f', 'g', 11],
    ['g', 'e', 9],
    ['e', 'c', 5],
    ['c', 'b', 8],
    ['b', 'a', 7],
    ['d', 'b', 9],
    ['d', 'e', 15],
    ['f', 'e', 8],
    ['b', 'e', 7]
]
# Instanciamos la clase Prim
app_tree = Prim()
tree = app_tree.apply_Prim(nodes, edges)
# El resultado de aplicar Prim es
cost = 0
print(tree)
for leaf in tree:
    cost += leaf[2]
print(f"El costo de recorrer todos los nodos usando Prim es: {cost}")
# edges = [
#     ['a', 'd', 5],
#     ['e', 'c', 5],
#     ['d', 'f', 6],
#     ['b', 'a', 7],
#     ['b', 'e', 7]
#     ['c', 'b', 8],
#     ['f', 'e', 8],
#     ['d', 'b', 9],
#     ['g', 'e', 9],
#     ['f', 'g', 11],
#     ['d', 'e', 15],


# ]