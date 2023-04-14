import random

def prims(graph):
    # select a random starting point (row?)
    # TODO setup an array with all the vertex currently connected/adjacent

    starting_vertex = random.randint(0, len(graph) - 1)
    
    for edge in graph[starting_vertex]:
        print(edge)


input_graph = [
    [0, 1, 0, 3], 
    [1, 0, 2, 3], 
    [0, 2, 0, 0], 
    [3, 3, 0, 0]]

prims(input_graph)