# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        # queue
        queue = collections.deque()
        result = []
        
        # non empty queue
        queue.append(root)
        
        # loop until queue is empty
        while queue: 
            
            # local calculation of each row
            calculation = []
            
            # append all the node values of the same row
            for _ in range(len(queue)):
                
                node = queue.popleft()
                
                if not node:
                    continue
                
                calculation.append(node.val)
                
                queue.append(node.left)
                queue.append(node.right)
            
            if calculation:
                result.append(sum(calculation)/len(calculation))
        
        # return the result
        return result