# dfs-graph-python
### Description:

Depth first search algorithm on a graph in python to identify whether or not there is a loop in the graph.
Assume all edges are one-way.

### Input:
Text file where:
- First line is the total number of nodes and edges
- Each subsequent line identifies the path from one node to another

ex.
4 4
1 2
2 3
3 4
4 1

This can also be done in the same format as a standard input on the command line. This code is commented out at the bottom of the file.

### Output:
If a loop is not found:
- print '0'

If a loop is found:
- print '1'
- print the nodes that make up that loop

ex.
1
1 2 3 4


