from collections import deque
import time

# Sample route map (Graph) as an adjacency list
route_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs_route(graph, start, goal):
    start_time = time.time()
    queue = deque([[start]])
    visited = {start}
    nodes_explored = 0
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        nodes_explored += 1
        
        if node == goal:
            return path, nodes_explored, (time.time() - start_time)
            
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None, nodes_explored, (time.time() - start_time)

def dfs_route(graph, start, goal):
    start_time = time.time()
    stack = [[start]]
    visited = set()
    nodes_explored = 0
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node not in visited:
            visited.add(node)
            nodes_explored += 1
            
            if node == goal:
                return path, nodes_explored, (time.time() - start_time)
                
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
                    
    return None, nodes_explored, (time.time() - start_time)

# Test run from 'A' to 'F'
print("BFS:", bfs_route(route_graph, 'A', 'F'))
print("DFS:", dfs_route(route_graph, 'A', 'F'))
