import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def level_order_bottom(root) -> int:
    res = collections.deque()

    def bfs(root):
        if not root:
            return []

        queue = collections.deque([root])
        while queue:
            level_size = len(queue)
            nested_list = []
            for _ in range(level_size):
                curr = queue.popleft()
                nested_list.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.appendleft(nested_list)

    bfs(root)
    return res


if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]

    '''
            3
           /  \
          9    20
              /  \
             15   7 
    '''

    tree = TreeNode(3)
    tree.left = TreeNode(9, None, None)
    tree.right = TreeNode(20, TreeNode(15, None, None),
                          TreeNode(7, None, None))

    print(level_order_bottom(tree))
