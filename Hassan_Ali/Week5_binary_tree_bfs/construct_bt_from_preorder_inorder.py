# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not inorder:
            return
        elem = preorder.pop(0)
        idx = inorder.index(elem)
        node = TreeNode(elem)
        node.left = self.buildTree(preorder,inorder[:idx])
        node.right = self.buildTree(preorder,inorder[idx+1:])
        return node