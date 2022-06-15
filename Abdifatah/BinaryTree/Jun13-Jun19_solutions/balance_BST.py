from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanceBST(root: TreeNode) -> List:
    lst = []

    def inorder(node) -> None:
        if not node:
            return

        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            lst.append(node.val)
            node = node.right

    def balance_tree(left, right) -> List:
        if left > right:
            return []

        mid = left + right >> 1
        node = TreeNode(lst[mid])
        node.left = balance_tree(left, mid - 1)
        node.right = balance_tree(mid + 1, right)
        # return node
        return [*[node.val], *node.left, *node.right]

    inorder(root)
    return balance_tree(0, len(lst) - 1)


if __name__ == "__main__":
    # root = [1,null,2,null,3,null,4,null,null]
    # Output: [2,1,3,null,null,null,4] or [3,1,4,null,2,null,null]
    '''
    1                   2               3
     \                 /  \            /  \
      2               1    3          1    4 
       \     ------>        \    OR    \      
        3                    4          2     
         \
          4     
    '''

    # Test Case 1:
    tree = TreeNode(1)
    tree.right = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, None)))

    # Test Case 2:
    # tree = TreeNode(2)
    # tree.left = TreeNode(1, None, None)
    # tree.right = TreeNode(3, None, None)
    print(balanceBST(tree))
