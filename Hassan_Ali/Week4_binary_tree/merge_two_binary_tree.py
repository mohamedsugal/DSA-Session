# https://leetcode.com/problems/merge-two-binary-trees/
# 617. Merge Two Binary Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #Iterative
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) :
        if not root1:
                return root2
        if not root2:
            return root1
        stack = [(root1,root2)]
            
        while stack:
            node1,node2 = stack.pop()
            
            node1.val += node2.val
            
            if node1.left and node2.left:
                stack.append((node1.left,node2.left))
            else:
                if node2.left:
                    node1.left = node2.left
            if node1.right and node2.right:
                stack.append((node1.right,node2.right))
            else:
                if node2.right:
                    node1.right = node2.right
                    
        return root1
    # recursion using dfs 
    # def mergeTrees(self, root1: TreeNode, root2: TreeNode) :
       
    #     def dfs(node1,node2):
    #         if not node1:
    #             node1 = node2
    #             return node1
    #         if not node2:
    #             return node1

    #         node1.val += node2.val

    #         node1.left = self.mergeTrees(node1.left,node2.left)
    #         node1.right = self.mergeTrees(node1.right,node2.right)
    #         return node1
            
           
    #     dfs(root1,root2)
    #     return root1
       
       

# tree1 = TreeNode(1)
# tree1.left = TreeNode(3)
# tree1.left.left = TreeNode(5)
# tree1.right = TreeNode(2)

# tree2 = TreeNode(2)
# tree1.left = TreeNode(1)
# tree1.right = TreeNode(3)
# tree1.left.right = TreeNode(4)
# tree1.right.right = TreeNode(7)

# sol = Solution()
# print(sol.mergeTrees(tree1,tree2))
