import random

def prims(graph):
    # select a random starting point (row?)
    # TODO setup an array with all the vertex currently connected/adjacent
    # TODO setup an array for all edges

    starting_vertex = random.randint(0, len(graph) - 1)

    # lmao pretty sure thiw won't work for now, rework this entirely
    print(starting_vertex + 1)
    for edge in graph[starting_vertex]:
        if edge != 0:
            # need to loop through this, because it skips numbers
            print("this is vertex that is connected is", graph[starting_vertex], "and it's weights are", edge)


input_graph = [
    [0, 1, 0, 3], 
    [1, 0, 2, 3], 
    [0, 2, 0, 0], 
    [3, 3, 0, 0]]

prims(input_graph)