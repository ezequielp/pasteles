from itertools import permutations
'''
Un pastel es un conjunto de 9 ingredientes
'''
def esRico(pastel):
    #Itero todas las filas del pastel
    for row in (
        #3 ingredientes en forma horizontal
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        #3 ingredientes en forma vertical
        (0, 3, 6), (1, 4, 7), (2, 5, 8)):
        #Calcula ingredientes distintos en linea
        row_ingredients = set([pastel[row[0]], pastel[row[1]], pastel[row[2]]])
        distinctTiles = len(row_ingredients)
        #Si hay 3 ingredientes distintos, esta fila no es rica
        if distinctTiles == 3:
            continue
        #Si hay 1 solo ingrediente en esta fila, el pastel es rico
        elif distinctTiles == 1:
            return True
        #Si hay 2 ingredientes en esta fila y uno es la "masita", entonces el pastel es rico
        elif distinctTiles == 2 and 'm' in row_ingredients:
            return True
    #Si no hay niguna fila que haga el pastel rico, es feo
    return False

'''
Permutations me devuelve todas las permutaciones de 9 de los 10 elementos de la lista (d= dulces,
f= frutas, c= confites, m=masita).
En principio, permutations no repite elementos de la lista. Pero como los elementos de la lista estan 
repetidos, es necesario filtrar las tortas repetidas. Para eso sirve set, que solo mantiene elementos 
distintos.
Finalmente, remuevo los pasteles que no son ricos.
'''
found2 = filter(esRico, set(permutations(['d', 'd', 'd', 'f', 'f', 'f', 'c', 'c', 'c', 'm'], 9)))

#Por cada pastel 'rico' hay 3 mas que son el mismo tablero rotado 90, 180 y 270 grados
print "Cantidad de pasteles ricos:", len(found2)*1.0/4
