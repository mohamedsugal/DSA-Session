class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = [i for i in range(n)]
        
        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node])
            
            return parent[node]
        
        def union(node1, node2):
            parent1, parent2 = find_parent(node1), find_parent(node2)
            
            if parent1 == parent2:
                return False
            parent[parent1] = parent[parent2]
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        return []
        