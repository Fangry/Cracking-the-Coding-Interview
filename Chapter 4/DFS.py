# from geeksforgeeks
# doesn't handle disconnected graph
from collections import defaultdict


class Graph:

    def __init__(self):
        # dict object, key = node, val = [] of connected nodes
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True  # starting node visited
        print(v)
        for i in self.graph[v]:  # recur for all adjacent vertices
            print('checking node', i, ', visited:', visited[i])
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, start):
        visited = [False]*len(self.graph)
        self.DFSUtil(start, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.graph)

g.DFS(2)
