def kruskal_mst(graph):
    # the plan is to rerpresent the weights as a 2d array
    # with weights | source | destination
    # sort that using the wieghts
    # then pick smallest until there is V-1 edges (also check if it cycles)

    # also because I'm using indexes, the graph starts at vertex 0
    
    weighted_edges = []

    for vertex_index in range(len(graph)):
        for edge_index in range(len(graph[vertex_index])):
            if graph[vertex_index][edge_index] != 0:
                # print(f"weight: {graph[vertex_index][edge_index]}, source: {vertex_index}, destination {edge_index}")
                weighted_edges.append([graph[vertex_index][edge_index], vertex_index, edge_index])
    
    # sort by weight
    weighted_edges.sort(key=return_first)
    
    amount_of_vertices = len(graph)
    connected_vertices = []
    connected_edges = 0
    index = 0
    while (connected_edges < amount_of_vertices): # don't need to -1 because len does that 
        # if not cycle (how) (if the destination is a vertex already connected (both source and distination))
        # that didn't work
        # this is very janky but it works for now
        if weighted_edges[index][1] not in connected_vertices:
            print(weighted_edges[index])

            connected_vertices.append(weighted_edges[index][1])

            connected_edges += 1
        
        index += 1



def return_first(input):
    return input[0]


input_graph = [
[0, 2, 2, 5, 1], 
[2, 0, 0, 3, 0], 
[2, 0, 0, 0, 3], 
[5, 3, 0, 0, 2], 
[1, 0, 3, 2, 0]] 

kruskal_mst(input_graph)
