import random

def prims(graph):
    number_of_vertices = len(graph)

    connected_vertices = []
    connected_vertices.append(random.randint(0, len(graph) - 1)) #random starting point

    used_edges = 0

    while (used_edges < number_of_vertices - 1):
        lowest_weight = 9999

        # for all the connected vertices
        # check for all the connected edges on that vertex
        # check if that vertex is already connected
        # get the minimum weight for that vertex
        # pick that vertex, add it to connected, and then add that edge somewhere


    
input_graph = [
    [0, 1, 0, 3], 
    [1, 0, 2, 3], 
    [0, 2, 0, 0], 
    [3, 3, 0, 0]]

prims(input_graph)
