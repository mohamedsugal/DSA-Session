from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # Recursive Solution
        height = self.height(root)
        deepest_leaves = [0]
        self.dfs(root, 0, height, deepest_leaves)
        
        return deepest_leaves[0]
    
    def dfs(self, root, curr_height, height, deepest_leaves):
        if not root:
            return
        curr_height += 1
        if not root.left and not root.right and curr_height == height:
            deepest_leaves[0] += root.val
        self.dfs(root.left, curr_height, height, deepest_leaves)
        self.dfs(root.right, curr_height, height, deepest_leaves)
        
        
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1
      