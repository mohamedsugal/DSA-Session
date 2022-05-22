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

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        root1_sum = self.findLeafSum(root1, [])
        root2_sum = self.findLeafSum(root2, [])
        
        return root1_sum == root2_sum


    def DepthFirstSearch(self, array, root):

        if not root:
            return


        if not root.left and not root.right:
            array.append(root.val)


        DepthFirstSearch(array,root.left)
        DepthFirstSearch(array,root.right)
        
        