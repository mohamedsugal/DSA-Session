# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        queue = collections.deque()
        
        global_depth = 0
        result = 0
        
        queue.append((root,0))
        
        while queue: 
            
            node,depth = queue.popleft()
            
            # reset the global variable
            if depth > global_depth:
                result = 0
                global_depth = depth
            
            # increment the result
            if depth == global_depth: result += node.val
            
            
            if node.left:
                queue.append((node.left,depth+1))
                
            if node.right:
                queue.append((node.right,depth+1))
        
        return result
        