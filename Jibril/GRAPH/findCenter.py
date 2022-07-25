class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        map = {}
        
        for k, v in edges:
            map[k] = map.get(k, 0) + 1
            map[v] = map.get(v, 0) + 1
        
        for k, v in map.items():
            if v == len(edges):
                return k
        return 