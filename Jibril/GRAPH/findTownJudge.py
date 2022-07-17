class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Solution#2
        if not trust and n <= 1:
            return n
        indegree = defaultdict(list)
        
        for src, dest in trust:
            indegree[dest].append(src)
            
        values = []
        for key, val in indegree.items():
            values.extend(val)
            
        for key, val in indegree.items():
            if len(val) == n-1 and key not in values:
                return key
        
        return -1
        
        """
        Solution#1
        count = [0] * (n+ 1)
        
        for edge1, edge2 in trust:
            count[edge1] -= 1
            count[edge2] += 1
        
        for i in range(1, n+ 1):
            if count[i] == n - 1:
                return i
        return -1
        
        """