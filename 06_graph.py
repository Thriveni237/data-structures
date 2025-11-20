# Graph Implementation (Adjacency List)
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an edge to the graph"""
        self.graph[u].append(v)
    
    def add_undirected_edge(self, u, v):
        """Add an undirected edge"""
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        """Breadth-First Search"""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.graph[vertex])
        
        return result
    
    def dfs(self, start):
        """Depth-First Search"""
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
    
    def display(self):
        """Display the graph"""
        for vertex, neighbors in self.graph.items():
            print(f'{vertex} -> {neighbors}')

# Test the Graph
if __name__ == '__main__':
    g = Graph()
    g.add_undirected_edge(0, 1)
    g.add_undirected_edge(0, 2)
    g.add_undirected_edge(1, 2)
    g.add_undirected_edge(1, 3)
    g.add_undirected_edge(2, 3)
    
    print('Graph:')
    g.display()
    
    print('BFS from 0:', g.bfs(0))
    print('DFS from 0:', g.dfs(0))
