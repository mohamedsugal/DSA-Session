class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstToGst(root: TreeNode) -> TreeNode:
    total = 0

    # Order is (right, root, left) --> basically reversed in-order traversal.
    # Reverse inorder traversal, calculate total and then update root.val to total.
    def dfs(node):
        nonlocal total
        if not node:
            return node

        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
    dfs(root)
    return root


if __name__ == "__main__":
    # root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    '''
              4
           /     \
          1       6
         /  \    /  \
        0    2  5    7
              \       \
               3       8
    '''

    tree = TreeNode(4)
    tree.left = TreeNode(1, TreeNode(0, None, None),
                         TreeNode(2, None, TreeNode(3, None, None)))
    tree.right = TreeNode(6, TreeNode(5, None, None),
                          TreeNode(7, None, TreeNode(8, None, None)))
    print(bstToGst(tree))
