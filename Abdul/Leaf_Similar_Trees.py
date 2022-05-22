# abdul sheikh
# may 22, 2022
# solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findLeafSum(self,root, leaf_sum):
        if not root:
            return 
        
        if not root.left and not root.right:
            leaf_sum.append(root.val)
        
        
        self.findLeafSum(root.left, leaf_sum)
        self.findLeafSum(root.right, leaf_sum)
        
        return leaf_sum
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        root1_sum = self.findLeafSum(root1, [])
        root2_sum = self.findLeafSum(root2, [])
        
        return root1_sum == root2_sum
        
        