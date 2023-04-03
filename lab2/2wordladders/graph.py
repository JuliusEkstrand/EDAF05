from collections import deque

class Graph:
    def __init__(self):
        # self.graph = dict()
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
    
    def add_vertex_and_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []

        self.graph[vertex1].append(vertex2)

    def print_graph(self):
        print(self.graph)

    def BFS(self, s, t):
        visited = []
        # visited = set()
        que = deque(self.graph[s])
        que.append(s)
        visited.append(s)
        # dist = {s:0}
        if s == t:
            return "Impossible"
        
        level = 0
        while que:
            v = que.popleft()
            for w in self.graph[v]:
                if w not in visited:
                    visited.append(w)
                    # visited.add(w)
                    # dist[w] = dist[v] + 1
                    que.append(w)
                    if w == t:
                        return level
            level += 1
        return "Impossible" 
