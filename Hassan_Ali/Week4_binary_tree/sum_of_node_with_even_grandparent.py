

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.totalEvgp = 0
        def dfs(node):
         
            if not node:
                return
            
            if node.val %2 == 0:
                if node.left:
                    if node.left.left:
                        self.totalEvgp += node.left.left.val
                    if node.left.right:
                        self.totalEvgp += node.left.right.val
                if node.right:
                    if node.right.right:
                        self.totalEvgp += node.right.right.val
                    if node.right.left:
                        self.totalEvgp += node.right.left.val
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.totalEvgp