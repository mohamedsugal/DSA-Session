from typing import List


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    # left, root, right
    def inorder_traversal(self, root) -> None:
        # Base case:
        if not root:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

    # Function that finds the leaf nodes of root1
    @staticmethod
    def root1(root) -> List:
        ls = []
        root1_helper(root, ls)
        return ls

    @staticmethod
    def root2(root) -> List:
        ls = []
        root2_helper(root, ls)
        return ls

    # @staticmethod
    # def leaf_similar(r1, r2) -> bool:
    #     return r1 == r2


# Root 1 utility function
def root1_helper(root: TreeNode, ls: List) -> List:
    # Base case:
    if not root:
        return

    if root.left is None and root.right is None:
        ls.append(root.val)

    root1_helper(root.left, ls)
    root1_helper(root.right, ls)


# Root 2 utility function
def root2_helper(root: TreeNode, ls: List) -> List:
    # Base case:
    if not root:
        return

    if root.left is None and root.right is None:
        ls.append(root.val)

    root2_helper(root.left, ls)
    root2_helper(root.right, ls)


# Function that builds our tree nodes
def build_tree() -> None:
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(3)
    tree2.right = TreeNode(2)

    # tree1.inorder_traversal(tree1)
    # print()
    print("Leaf nodes of root1:")
    print(tree1.root1(tree1))
    print()
    print("Leaf nodes of root2:")
    print(tree2.root2(tree2))

    # Check leaf similarity
    print(tree1.root1(tree1) == tree2.root2(tree2))


# Tree 1:
#                1
#              /   \
#             2     3

# Tree 2:
#                1
#              /   \
#             3     2

if __name__ == "__main__":
    build_tree()
