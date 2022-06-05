from typing import List
from itertools import defaultdict
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        sum_dict = defaultdict(int)
        level_item_count = defaultdict(int)
        def dfs(node,level=0):
           
            if not node:
                return level
            sum_dict[level] += node.val
            level_item_count[level] += 1
            
            
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        
        dfs(root)
        res = []
        for k,v in sum_dict.items():
            if k in level_item_count:
                res.append(v/level_item_count[k])
        return res
            
        
        
     
            
                