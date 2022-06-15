from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root, k: int) -> bool:
    arr = dfs(root)
    mapping = {}
    for i in range(len(arr)):
        curr = arr[i]
        complement = k - curr
        if complement in mapping:
            return True
        else:
            mapping[curr] = i
    return False


def dfs(root) -> List:
    if not root:
        return []

    lst = []
    stack = [root]
    while stack:
        node = stack.pop()
        lst.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return lst


if __name__ == "__main__":
    # root = [5,3,6,2,4,null,7], k = 9
    # Output: True
    '''
         5
       /  \
      3    6
     /  \   \
    2    4   7

    '''

    tree = TreeNode(5)
    tree.left = TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None))
    tree.right = TreeNode(6, None, TreeNode(7, None, None))

    print(findTarget(tree, 9))
