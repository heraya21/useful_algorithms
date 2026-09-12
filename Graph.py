from Stack import Stack1
import json

class Graph:
"""
Representation of a graph (directed or undirected, with positive edge weights).
You may choose the internal representation, e.g., adjacency list (with weights) or
adjacency/distance matrix.
"""

def __init__(self, number_of_nodes, directed=True):
    """Initialize the graph with a given number of nodes and orientation.

    Args:
        number_of_nodes (int): Number of nodes in the graph.
        directed (bool): True for a directed graph, False for undirected.

    Exception handling:
        Check that number_of_nodes is a non-negative integer. Raise ValueError if invalid.
    """

    if not((type(number_of_nodes) is int) and number_of_nodes >= 0):
        raise ValueError("number of nodes must be a natural number")

    self.number_of_nodes = number_of_nodes
    """number of nodes in Graph"""
    self.directed = directed
    """bool whether graph is directed"""
    self.adjacency_list = [[] for _ in range(number_of_nodes)]
    """list of lists of edges going from each node"""


def add_or_change_edge(self, u, v, weight=1):
    """Add a new edge or change the weight of an existing edge from node u to node v.

    To remove an edge, set weight = None.
    Behavior may differ depending on whether the graph is directed or not.

    Exception handling:
       Check that 0 <= u, v < number_of_nodes.
       Check that weight is positive number or None (for removal).
       Raise ValueError or IndexError if invalid.

    """

def add_or_change_edge(self, u, v, weight=1):
if not (0 <= u < self.number_of_nodes and 0 <= v < self.number_of_nodes):
raise IndexError("Index out of node range")

if weight is not None and weight < 0:
    raise ValueError("weight must be non-negative number or None for removal")

if weight is None:
    self.adjacency_list[u] = [edge for edge in self.adjacency_list[u] if edge[0] != v]

    if not self.directed:
        self.adjacency_list[v] = [edge for edge in self.adjacency_list[v] if edge[0] != u]
    return

for i in range(len(self.adjacency_list[u])):
    if self.adjacency_list[u][i][0] == v:
        self.adjacency_list[u][i] = (v, weight)

        if not self.directed:
            for j in range(len(self.adjacency_list[v])):
                if self.adjacency_list[v][j][0] == u:
                    self.adjacency_list[v][j] = (u, weight)

        return

self.adjacency_list[u].append((v, weight))

if not self.directed:
    self.adjacency_list[v].append((u, weight))       

def get_edge_weight(self, u, v):
    """Return the weight of the edge from u to v.

    Returns None if the edge does not exist.

    Exception handling:
        Check valid node indices. Raise ValueError or IndexError if invalid.
    """

    if not((u >= 0 and v >= 0) and (u < self.number_of_nodes and v < self.number_of_nodes)):
        raise IndexError("Index out of node range")
    
    for i in range(len(self.adjacency_list[u])):
        if self.adjacency_list[u][i][0] == v:
            return self.adjacency_list[u][i][1]
    return None

def get_number_of_nodes(self):
    """Return the total number of nodes in the graph."""

    return self.number_of_nodes

def get_neighbors(self, u):
    """Return a list of all neighbors (reachable nodes) from node u.

    Example: [1, 3, 8]

    Exception handling:
        Raise ValueError or IndexError if u is out of range.
        Return empty list if u has no neighbors.
    """

    if not(u >= 0 and u < self.number_of_nodes):
        raise IndexError("Index out of node range")

    neighbors = []
    for i in range(len(self.adjacency_list[u])):
        neighbors.append(self.adjacency_list[u][i][0])
    
    return neighbors

def get_neighbors_with_weights(self, u):
    """returns a list of neighbors with their weights"""
    if not 0 <= u < self.number_of_nodes:
        raise IndexError("Index out of node range")

    return self.adjacency_list[u].copy()

def __str__(self) -> str:
    """Return a string representation of the graph 
    based on the internal structure (e.g., adjacency matrix or list).
    """
    string = ""
    for i in range(self.number_of_nodes):
        string += str(self.adjacency_list[i])
        string += "\n"
    return string


def get_edges(self) -> list:
    """Return a list of all edges in the graph.

    Each edge is represented as a tuple: ((u, v), weight)

    Example output:
    [((0, 1), 1), ((1, 2), 1)]         # directed
    or
    [((0, 1), 1), ((1, 2), 1)]         # undirected (only one per pair, u <= v)
    """

    edges = []
    if self.directed:
        for i in range(self.number_of_nodes):
            for edge in self.adjacency_list[i]:
                edges.append(((i, edge[0]), edge[1]))
    elif not self.directed:
        for i in range(self.number_of_nodes):
            for edge in self.adjacency_list[i]:
                if i <= edge[0]: 
                    edges.append(((i, edge[0]), edge[1]))
    return edges

def find_connected_components(self):
    """Return a list of connected components in the undirected graph.

    Each component is represented as a list or set of nodes.

    Example:
        [[0, 2], [1, 3, 7], [4], [5, 6]]
        or
        [{0, 2}, {1, 3, 7}, {4}, {5, 6}]

    Exception handling:
        Raise ValueError if the graph is directed.
    """
    if self.directed:
        raise ValueError("this method is for undirected graphs only")
    
    self.A = [i for i in range(self.number_of_nodes)] #a list of active nodes
    C = [] #a list of components
    while len(self.A) != 0:
        s = self.A[0]
        component = self.DFS_component(s)
        C.append(component)
    return C


def DFS_component(self, s):
    stack = Stack1()
    component = []
    self.A.remove(s)
    stack.push(s)
    while not(stack.is_empty()):
        u = stack.pop()
        component.append(u)
        for i in self.adjacency_list[u]:
            if i[0] in self.A:
                self.A.remove(i[0])
                stack.push(i[0])
    return component

    

def shortest_paths(self, start):
    """Compute the shortest paths from a start node to all other nodes using the Dijksra algorithm.

    Returns:
        tuple:
            distances (list): distances[i] is the shortest distance from start to node i (or float('inf')).
            previous (list): previous[i] == j means j is the predecessor of i on the shortest path.

    Example:
        ([0, 1, inf, 2], [0, 0, -1, 1])
        for start node 0 and edges (0, 1), (1, 3).

    Exception handling:
        Raise IndexError or ValueError if start is invalid.
        Check for negative weights (if using Dijkstra, weights must be non-negative). Raise ValueError if invalid.

    """
    ...

def reconstruct_the_shortest_path(self, destination, previous):
    """Return the list of nodes forming the shortest path to node destination.

    'previous' is the list returned by self.shortest_paths(start).

    Example:
        [0, 1, 3] for node 3,
        [] for unreachable node 2
        in a graph with edges (0, 1), (1, 3) and start node 0.

    Exception handling:
        Raise ValueError or IndexError if destination is out of range.
        Check that previous is a list of valid indices or -1. Raise ValueError if invalid.
        Return [] if node is unreachable.
    """
    ...


@classmethod
def load_from_txt(cls, filename: str): #cls allows to use method on children of class as well, instead of only applying it to Graph class only
    """loads and creates a graph from txt file. 
    expected format of txt file:
    first line: n bool(directed)
    next m lines: u v w; where u and v are connected nodes and w is edge's weight"""
    try: 
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lst_line = lines[0].split()
            """expected format: [n, Optional (True by default) - bool(directed) ]"""
            n = int(lst_line[0])
            """number of nodes in graph"""
            if lst_line[1].lower() == "false":
                directed = False
            else: 
                directed = True
            graph = cls(n, directed)
            lines.pop(0)
            for line in lines:
                line_list = line.split()
                try:
                    u, v, w = int(line_list[0]), int(line_list[1]), float(line_list[2])
                except:
                    raise ValueError("node indexes u and v must be integers, their weight w must be of float or int type")
                graph.add_or_change_edge(u, v, w)
    except OSError as error:
        raise OSError(f"Soubor '{filename}' se nepodařilo načíst") from error
    return graph


def create_json(self) -> str:
    """returns a canonical string to be put into string file or to represent a graph"""
    edges = sorted(self.get_edges(), key=lambda edge: (edge[0][0], edge[0][1], edge[1]))
    """a sorted list of edges in format ((u,v), w)"""
    data = {
        "number of nodes": self.number_of_nodes,
        "directed": self.directed,
        "edges": edges
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def save_to_json(self, filename: str):
    """saves the graph to a json file of a given name"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.create_json())
    except OSError as error:
        raise OSError("An error occurred while writing to a document") from error
        