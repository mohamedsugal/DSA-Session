from typing import List, Optionalß

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not preorder or not inorder:
            return None
        # The root is first value in preorder.
        tree = TreeNode(preorder[0])
        
        # get the index preorder[0] in inorder.
        mid = inorder.index(preorder[0])
        
        # build your left subtree
        tree.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        # build your right subtree.
        tree.right = self.buildTree(preorder[mid+1: ], inorder[mid+1:])
        
        return tree
        