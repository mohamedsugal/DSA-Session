from typing import List


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Left -> root -> right
def inorder_traversal(root) -> None:
    res = []
    inorder_traversal_util(root, res)
    print(res)


# Recursive solution
def mergeTrees(root1, root2):
    if not root1:
        return root2

    if not root2:
        return root1

    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1


def inorder_traversal_util(root, res):
    if not root:
        return

    inorder_traversal_util(root.left, res)
    res.append(root.val)
    inorder_traversal_util(root.right, res)


def build_tree():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    inorder_traversal(tree1)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)
    inorder_traversal(tree2)

    tree3 = mergeTrees(tree1, tree2)
    inorder_traversal(tree3)  # [5, 4, 4, 3, 5, 7]


if __name__ == "__main__":
    build_tree()
