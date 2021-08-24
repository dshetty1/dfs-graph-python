#Name: Dhruv Shetty

# Undiscovered
WHITE = 0

# Visited, but not finished (still on the call stack)
GRAY = 1

# Finished
BLACK = 2

# THE BELOW 2 DATA STRUCTURES (Graph and DFSINnfo) ARE NOT MY CODE

# Data structure for representing a graph
class Graph():

    # Initalize a graph with n vertices and no edges
    def __init__(self, n):

        # Number of nodes in the graph
        self.n = n

        # For u in [0..n), A[u] is the adjacency list for u
        self.A = [[] for i in range(n)]

    # Add an edge u -> v to the graph
    def add_edge(self, u, v):
        self.A[u].append(v)

# Data structure holding data computed by DFS
class DFSInfo():
    def __init__(self, graph):

        # Number of nodes in graph
        n = graph.n

        # Color of each node during DFS (WHITE, GRAY, or BLACK)
        self.color = [-1 for i in range(n)]

        # Parent of each node in DFS forest                                   
        self.parent = [-1 for i in range(n)]
                                             
        # Discovery time of each node in DFS forest
        self.d = [0 for i in range(n)]
                                             
        # Finishing time of each node in DFS forest
        self.f = [0 for i in range(n)]

        # Current time
        self.t = 0;               

# Performs a recursive DFS, starting at u
def rec_DFS(u, graph, dfs_info):
    # Node is discovered
    dfs_info.color[u] = GRAY
    dfs_info.t += 1
    dfs_info.d[u] = dfs_info.t

    # If a node is undiscovered, perform another recursive DFS
    for v in (graph.A[u]):
        if dfs_info.color[v] == WHITE:
            dfs_info.parent[v] = u
            rec_DFS(v, graph, dfs_info)

    # Node is finished
    dfs_info.color[u] = BLACK
    dfs_info.t += 1
    dfs_info.f[u] = dfs_info.t


# Performs a larger DFS on given graph.
# Returns DFSInfo object (outlined above)
def DFS(graph):
    d_info = DFSInfo(graph)

    # Sets each node to WHITE (undiscovered)
    for v in range(graph.n):
        d_info.color[v] = WHITE
        d_info.parent[v] = -1
    d_info.t = 0

    # If a node is undiscovered, perform a recursive DFS
    for v in range(graph.n):
        if d_info.color[v] == WHITE:
            rec_DFS(v, graph, d_info)

    return d_info


# Scan edges of graph until a back edge is located. Then build a list of nodes in the cycle
def find_cycle(graph, dfs_info):
    cycle = []
    back_edge_present = False
    for u in range(graph.n):
        # See if a back edge is present
        for v in graph.A[u]:
                if (dfs_info.f[u]) <= dfs_info.f[v]:
                    back_edge_present = True
                    back_edge_successor = u
                    break
        if back_edge_present:
            break
    
    # We have a loop, cycle through node's parents and return the loop
    if back_edge_present:
        temp_node = back_edge_successor
        while len(cycle) == len(set(cycle)):
            if dfs_info.parent[back_edge_successor] == -1:
                break
            cycle.append(dfs_info.parent[back_edge_successor])
            back_edge_successor = dfs_info.parent[back_edge_successor]
        
        cycle_in_order = []

        for i in reversed(cycle):
            cycle_in_order.append(i)
        cycle_in_order.append(temp_node)

        return cycle_in_order
        
    else:
        return 0



if __name__ == "__main__":

    # Code for standard line input rather than text file
    '''
    inputs = input()

    rooms = int(inputs.split()[0])
    paths = int(inputs.split()[1])

    g = Graph(rooms)

    while paths > 0:
        inputs = input()

        starting_node = int(inputs.split()[0]) - 1
        destination_node = int(inputs.split()[1]) - 1

        g.add_edge(starting_node, destination_node)

        paths -= 1
    '''



    # Code for text file input
    f = open('graph.txt', 'r')
    inputs = f.readline()

    # Identifies total nodes and edges
    nodes = int(inputs.split()[0])
    edges = int(inputs.split()[1])

    # Constructs graph
    g = Graph(nodes)

    # Adds nodes to graph based on input instructions
    while edges > 0:
        inputs = f.readline()

        starting_node = int(inputs.split()[0]) - 1
        destination_node = int(inputs.split()[1]) - 1
        g.add_edge(starting_node, destination_node)

        edges -= 1

    # Perform depth first search on graph
    info = DFS(g)
    
    # Determine if there is a cycle
    result = find_cycle(g, info)

    # Print result
    if result == 0:
        print(0)
    elif None in result:
        print(0)
    else:
        print(1)
        for k in range(len(result)):
            print(result[k] + 1, end =" ")