from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # base case
        if not nums:
            return None
        
        max_val = max(nums)
        tree = TreeNode(max_val)
        index = nums.index(max_val)
        tree.left = self.constructMaximumBinaryTree(nums[:index])
        tree.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return tree
        