#543. Diameter of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # variable
        res = [0]

        # depth first search
        def dfs(root):
            
            # base case
            if not root:
                return -1
            
            # recursive function
            left = dfs(root.left)
            right = dfs(root.right)
            
            # update the variable
            res[0] = max(res[0], 2 + right + left)
            
            # return statement
            return 1 + max(left, right)
        
        # call the recursive function
        dfs(root)
        return res[0]
        