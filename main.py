"""
 - Graph
 - Vertixes: 6
 * 1--2---3
   |   -/ |
 * |  7   |
 * 4-/    5
 * | ----/
   |/
 * 6--7---8
 
 - Vertix 1 points to 2 & 4
 - Vertix 2 points to 1 & 3
 - Vertix 3 points to 2, 5 & 7
 - Vertix 4 points to 1, 6, & 7 
 - Vertix 5 points to 3 & 6
 - Vertix 6 points to 4, 5 & 8
 - Vertix 7 points to 3 & 4
 - Vertix 8 points to 6
 
 Problems to solve:
     - How many edges is there in total of this graph?
     - What is the fastest path between Vertix 1 and Vertix 8?
     
 TODO:
     - Add as much concepts learnt and displayed on paper
     - Expand this project to handle multiple graphs
     - Determine the efficiency difference between each method used on any particular graph
"""

from collections import deque

class Vertix:
    def __init__(self, index, edges, points_to):
        self.index = index # Vertex Number
        self.edges = edges # Edges this Vertex has.
        self.points_to = points_to # Array of Vertix Numbers this Vertex points too.

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # Graph holding the amount of Vertexes
        
# Function to count total edges in the graph.
def count_total_edges(graph):
    totaldeg = 0
    
    for v in graph.vertices: # Iterate through each Vertex
        if v is not None:
            totaldeg = totaldeg + v.edges # Store all edges from each vertex as the graph degrees
        
    return totaldeg / 2; # Divide the count by 2, getting the total edges for the graph.

# Implementation of a Breadth-First search
# First In First Out Approach
# if v1 is end_index, return path
# if not? record node to our visited history and goto next node
# rinse & repeat
# if children of nodes do not result in end_index, goto unchecked node & repeat
def solve_fastest_path(graph, start_index, end_index):
    queue = deque() # Initialize queue, is the C style equivalent of an array with indices.
    visited = set() # Python equivalent of a hash set in C
    
    parent_map = {} # Key-Value pairs
                    # Key: Current Vertex Index
                    # Value: Previous Vertex Index
                    
    queue.append(start_index) # Add the start index to the queue
    visited.add(start_index) # Add the start index to the visited hash set

    parent_map[start_index] = None # Start of our search
    
    while queue:
        currentIndex = queue.popleft() # Dequeue the current Vertex index.
        
        if currentIndex == end_index:
            break
            
        currentVertex = graph.vertices[currentIndex]

        # Tracking neighbor vertexes
        for neighbor in currentVertex.points_to:
            if neighbor not in visited:
                visited.add(neighbor) # Add neighbor to visited Vertex set
                queue.append(neighbor) # Add neighbor to queue list
                parent_map[neighbor] = currentIndex
                # Record the path to this neighbor, we have added neighbor to visited
                # This means we will not process this neighbor index again
                # This prevents backtracking or looping.
                
    # Define path to be returned.
    path = []
    step = end_index
    
    # We require our end index to be found from our tracks above before attempting
    # to build the fastest path to return.           
    if end_index in parent_map:         
        while step != None: # Step cannot be invalid
            path.append(step) # Append the step to our new path
            step = parent_map[step] # Assign the step to the step in the built parent map.

    path.reverse() # Reverse the path list to hold original order
    return path
    
    
def main():      
    # Initialize Vertixes in Graph
    # Basically an Adjacent List in code form.
    # vN = Vertix(index, edges, [index vertix array])
    v1 = Vertix(1, 2, [1, 4]) # Vertix 1 has two edges  that points to Vertix 2 & 4
    v2 = Vertix(2, 2, [1, 3]) # ...
    v3 = Vertix(3, 3, [2, 5, 7])
    v4 = Vertix(4, 3, [1, 6, 7])
    v5 = Vertix(5, 2, [3, 6])
    v6 = Vertix(6, 3, [4, 5, 8])
    v7 = Vertix(7, 2, [3, 4])
    v8 = Vertix(8, 1, [6])
    
    # Store all Vertixes in the graph structure (class)
    vGraph = Graph([None,v1,v2,v3,v4,v5,v6,v7,v8])
    
    # Print all Vertex information in graph
    for v in vGraph.vertices:
        if v is not None:
            print(f"Vertex: {v.index}")
            print(f"Edges: {v.edges}")
            print(f"Points To: {v.points_to}\n")
    
    print("Total Edges:")
    print(count_total_edges(vGraph))
    print("")

    print("Fastest Path From v1 to v8")
    print(solve_fastest_path(vGraph, v1.index, v8.index))
    
    return 0

if __name__ == "__main__":
    main()