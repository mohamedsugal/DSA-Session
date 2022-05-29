class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # left root right
    def inorder_traversal(self, root):
        # Base case:
        if not root:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" -> ")
        self.inorder_traversal(root.right)

    def has_path_sum(self, root, targetSum) -> bool:
        if targetSum in self.sum_path(root):
            return True
        else:
            return False

    # Function sums up each path of the tree
    @staticmethod
    def sum_path(root):
        lst = []
        sum_path_helper(root, lst, 0)
        return lst


def sum_path_helper(root, lst, curSum):
    # Base case:
    if not root:
        return

    curSum += root.val
    if root.left is None and root.right is None:
        lst.append(curSum)

    sum_path_helper(root.left, lst, curSum)
    sum_path_helper(root.right, lst, curSum)


def build_tree():
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.right.left = TreeNode(13)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)

    tree.inorder_traversal(tree)
    print()
    tree.has_path_sum(tree, 22)


if __name__ == "__main__":
    build_tree()
