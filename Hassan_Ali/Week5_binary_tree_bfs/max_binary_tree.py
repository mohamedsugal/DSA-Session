from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) ->TreeNode:
        
        if not nums:
            return
            
        maxnum = max(nums)
        idx = nums.index(maxnum)
        
        node = TreeNode(maxnum)
        node.left = self.constructMaximumBinaryTree(nums[0:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+ 1:])
        return node