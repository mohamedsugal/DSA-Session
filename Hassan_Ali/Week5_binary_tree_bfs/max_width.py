# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        
        queue = [(root,1)]
        maxwidth = 1
        
        while queue:
            sizq = len(queue)
            level = []
            for _ in range(sizq):
                node,pos = queue.pop(0)
                level.append((root.val,pos))
                if node.left:
                    queue.append((node.left,pos*2))
                if node.right:
                    queue.append((node.right,pos*2+1))
            maxwidth = max(maxwidth,level[-1][1] - level[0][1]+1)
            
        return maxwidth