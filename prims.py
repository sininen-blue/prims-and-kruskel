import random

def prims(graph):
    number_of_vertices = len(graph)

    connected_vertices = []
    connected_vertices.append(0)
    # connected_vertices.append(random.randint(0, len(graph) - 1)) #random starting point

    while (len(connected_vertices) < number_of_vertices):
        lowest_weight = 9999
        origin_point = 0
        vertex_to_add = 0

        # for all the connected vertices
        for vertex_index in connected_vertices:
            for edge_index in range(len(graph[vertex_index])):
                if (graph[vertex_index][edge_index] != 0 and
                    edge_index not in connected_vertices): #edge index == connected vertex index
                    
                    if graph[vertex_index][edge_index] < lowest_weight:
                        lowest_weight = graph[vertex_index][edge_index]

                        vertex_to_add = edge_index
                        origin_point = vertex_index
            
        
        connected_vertices.append(vertex_to_add)
        print(f"connected vertex: {origin_point} to vertex: {vertex_to_add}, with the edge weight of {lowest_weight}")
        # TODO make a way to represent the tree and return it using this info 

        # check for all the connected edges on that vertex_index and tthat they aren't already connected
        # get the minimum weight for that vertex_index
        # pick that vertex_index, add it to connected, and then add that edge somewhere


    
input_graph = [
[0, 2, 2, 5, 1], 
[2, 0, 0, 3, 0], 
[2, 0, 0, 0, 3], 
[5, 3, 0, 0, 2], 
[1, 0, 3, 2, 0]] 

prims(input_graph)
