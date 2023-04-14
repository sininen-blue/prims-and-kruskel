import random

def prims(graph):
    # select a random starting point (row?)
    # TODO setup an array with all the vertex currently connected/adjacent
    # TODO setup an array for all edges

    connected_vertices = []
    connected_vertices.append(random.randint(0, len(graph) - 1)) #random starting point

    # lmao pretty sure thiw won't work for now, rework this entirely
    for vertex in connected_vertices:
        print(graph[vertex])
        
        current_minimum_distance = 9999
        vertex_to_add = 0
        for edge in graph[vertex]:
            if edge < current_minimum_distance and edge != 0:
                current_minimum_distance = edge
                vertex_to_add = graph[vertex].index(edge) 
                # if there are multiple vertices that have the same ewight, it can't differentiate, but that works in this scenario\
                
                # TODO figure out which edge is chose here to repersent the graph
                # TODO also figure out how to present output
        
        connected_vertices.append(vertex_to_add)


input_graph = [
    [0, 1, 0, 3], 
    [1, 0, 2, 3], 
    [0, 2, 0, 0], 
    [3, 3, 0, 0]]

prims(input_graph)