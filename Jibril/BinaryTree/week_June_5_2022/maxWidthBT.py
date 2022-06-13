from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Bfs traversal.
    
        largest_width = 0
        
        q = deque() # (node, pos)
        q.append((root, 0))
        
        while q:
            size = len(q)
            lpos = q[0][1] # left pos
            rpos = q[-1][1] # right pos
            
            for _ in range(size):
                node, pos = q.popleft()
                
                #process the node
                if node.left:
                    q.append((node.left, pos * 2 + 1))
                if node.right:
                    q.append((node.right, pos * 2 + 2))
            
            largest_width = max(largest_width, rpos - lpos + 1)
            
        return largest_width
            
        