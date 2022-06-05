from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevelsIter(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()
        q.append(root)
        levels = []
        
        
        while q:
            values = 0
            count = 0
            for _ in range(len(q)):
                node = q.popleft()
                
                if node:
                    # do something with the nodes in that level.
                    values += node.val
                    count += 1
                    
                    # append left and right nodes to the queue.
                    q.append(node.left)
                    q.append(node.right)
            # prevents division by zero.
            if count > 0:
                levels.append(values/count)
        return levels
      
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # recursive solution
        levels = []
        height = self.height(root)
        for level in range(height):
            curr_level = []
            self.getLevels(root, level, curr_level)
            values = 0
            for val in curr_level:
                values += val
            lenLevel = len(curr_level)
            if lenLevel > 0:
                levels.append(values / lenLevel)
        
        return levels
    
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1

    def getLevels(self, root, levelIndex, level):
        if not root:
            return None
        if levelIndex == 0:
            level.append(root.val)
        elif levelIndex > 0:
            self.getLevels(root.left, levelIndex-1, level)
            self.getLevels(root.right, levelIndex-1, level)