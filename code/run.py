# Search methods

import search

print("DESDE B hasta A\n")
ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("\nBusqueda por ramificacion y acotacion")
print(search.bab(ab).path())
print("\nBusqueda por ramificacion y acotacion con subestimacion")
print(search.consubestimacion(ab).path())

# Result:

# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
print("------------------------------------------------------------------------------------")
print("DESDE E hasta S\n")

se = search.GPSProblem('S', 'E'
                       , search.romania)
print("\nBusqueda por ramificacion y acotacion")
print(search.bab(se).path())
print("\nBusqueda por ramificacion y acotacion con subestimacion")
print(search.consubestimacion(se).path())

# Result:

# [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>] : 547
# [<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>] : 547

print("------------------------------------------------------------------------------------")
print("DESDE O hasta C\n")

co = search.GPSProblem('C', 'O'
                       , search.romania)
print("\nBusqueda por ramificacion y acotacion")
print(search.bab(co).path())
print("\nBusqueda por ramificacion y acotacion con subestimacion")
print(search.consubestimacion(co).path())

# Result:

# [<Node O>, <Node S>, <Node R>, <Node C>] : 377
# [<Node O>, <Node S>, <Node R>, <Node C>] : 377

print("------------------------------------------------------------------------------------")
print("DESDE B hasta N\n")

nb = search.GPSProblem('N', 'B'
                       , search.romania)
print("\nBusqueda por ramificacion y acotacion")
print(search.bab(nb).path())
print("\nBusqueda por ramificacion y acotacion con subestimacion")
print(search.consubestimacion(nb).path())

#[<Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
#[<Node B>, <Node U>, <Node V>, <Node I>, <Node N>]

print("------------------------------------------------------------------------------------")
print("DESDE R hasta Z\n")

zr = search.GPSProblem('Z', 'R'
                       , search.romania)
print("\nBusqueda por ramificacion y acotacion")
print(search.bab(zr).path())
print("\nBusqueda por ramificacion y acotacion con subestimacion")
print(search.consubestimacion(zr).path())

#[<Node R>, <Node S>, <Node A>, <Node Z>]
#[<Node R>, <Node S>, <Node A>, <Node Z>]