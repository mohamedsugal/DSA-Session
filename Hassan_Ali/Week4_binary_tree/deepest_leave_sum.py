from itertools import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        sumdict = defaultdict(int)
        
        def dfs(node,depth):
            
            if not node:
                return 0
            
            sumdict[depth] += node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0) 
        maxk = max(sumdict.keys())
        return sumdict[maxk]

# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
        
      
        
#         def max_depth(node,depth):
#             if not node:
#                 return 0
           
#             leftDepth = max_depth(node.left,depth + 1)
#             rightDepth = max_depth(node.right,depth + 1)
            
          
#             return 1 + max(leftDepth,rightDepth)
#         my_root = root   
#         self.max_d =(max_depth(my_root,0))
#         self.totalSum = 0
        
#         def leaveSum(node,level):
#             if not node:
#                 return 0
#             if not node.left and not node.right and level == self.max_d-1:
#                 self.totalSum += node.val
#             leaveSum(node.left,level+1)
#             leaveSum(node.right,level+1)
            
#         leaveSum(root,0)
#         return self.totalSum