from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Itterative solution
    def leafSimilar_itter(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leave_nodes_itter(root1) == self.leave_nodes_itter(root2)
        
    
    def leave_nodes_itter(self, root):
        leaves = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.left and not root.right:
                leaves.append(root.val)
            root = root.right
        return leaves
      
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leave_nodes(root1) == self.leave_nodes(root2)
        
    
    def leave_nodes(self, root):
        leaves = []
        self.helper_leave_nodes(root, leaves)
        return leaves
    
    def helper_leave_nodes(self, root, leaves):
        if not root:
            return
        self.helper_leave_nodes(root.left, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        self.helper_leave_nodes(root.right, leaves)
        