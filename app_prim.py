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
app_tree= Prim()
