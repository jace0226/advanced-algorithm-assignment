# Generic Graph Data Structure

class Graph:
    """
    A generic, unweighted directed graph data structure using an adjacency list.
    Vertices can be any type (e.g., strings, custom objects).

    Structure:
        self.adj_list = { vertex: [outgoing_vertices], ... }
    """

    def __init__(self):
        # Adjacency list storing outgoing edges: vertex -> list of target vertices
        self.adj_list = {}

    def addVertex(self, vertex):
        # Adds a new vertex to the graph if it doesn't already exist.
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def addEdge(self, source_vertex, target_vertex):
        """
        Connects source_vertex to target_vertex (Directed Edge: source -> target).
        In course context: target requires source (source unlocked target).
        """
        # Ensure both vertices exist in graph
        if source_vertex in self.adj_list and target_vertex in self.adj_list:
            if target_vertex not in self.adj_list[source_vertex]:
                self.adj_list[source_vertex].append(target_vertex)
                return True
        return False

    def removeEdge(self, source_vertex, target_vertex):
        # Removes a directed edge from source_vertex to target_vertex.
        if source_vertex in self.adj_list and target_vertex in self.adj_list:
            if target_vertex in self.adj_list[source_vertex]:
                self.adj_list[source_vertex].remove(target_vertex)
                return True
        return False

    def getOutgoingAdjacentVertices(self, vertex):
        # Returns all vertices directly unlocked/pointed to by the given vertex.
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        return []

    def listIncomingAdjacentVertex(self, vertex):
        """
        Returns all vertices that have an incoming edge into the given vertex.
        For course context: finds all prerequisites required by this vertex.
        """
        incoming_vertices = []
        if vertex not in self.adj_list:
            return incoming_vertices

        # Iterate over all vertices and check if target 'vertex' is in their outgoing list
        for v, neighbors in self.adj_list.items():
            if vertex in neighbors:
                incoming_vertices.append(v)
        return incoming_vertices

    def getAllVertices(self):
        # Returns a list of all vertices in the graph.
        return list(self.adj_list.keys())