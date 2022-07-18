
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        province = 0
        rows = len(isConnected)
        cols = len(isConnected[0])
        parent = [i for i in range(n)]
        
        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node])
            
            return parent[node]
        
        def union(node1, node2):
            nonlocal province
            parent1, parent2 = find_parent(node1), find_parent(node2)
            
            if parent1 != parent2:
                parent[parent1] = parent[parent2]
                province += 1
        
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j] == 1 and i != j:
                    union(i, j)
        return n - province
                