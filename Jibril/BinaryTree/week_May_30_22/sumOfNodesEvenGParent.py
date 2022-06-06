from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparentIter(self, root: TreeNode) -> int:
        sum_of_nodes = 0
        grandParent = -1
        parent = -1
        stack = [(root, parent, grandParent)]
        
        while stack:
            root, parent, grandParent = stack.pop()
            # process the root
            
            
            if grandParent % 2 == 0:
                sum_of_nodes += root.val
                
            if root.right:
                stack.append((root.right, root.val, parent))
            if root.left:
                stack.append((root.left, root.val, parent))
            
            
        return sum_of_nodes
            
            
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_of_nodes = 0
        
        def dfs(root, parent, grandParent):
            nonlocal sum_of_nodes
            if not root:
                return 0
            
            if grandParent % 2 == 0:
                sum_of_nodes += root.val
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)
        
        dfs(root, -1, -1)
        
        return sum_of_nodes
        
        