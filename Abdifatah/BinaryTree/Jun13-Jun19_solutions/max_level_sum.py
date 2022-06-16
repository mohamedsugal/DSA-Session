import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum(root):
    if not root:
        return 0

    queue = collections.deque([root])
    levels_sum = []

    while queue:
        level_size = len(queue)
        total = 0

        for _ in range(level_size):
            curr = queue.popleft()
            total += curr.val

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        levels_sum.append(total)

    maximal = levels_sum[0]
    max_index = 0
    for i in range(len(levels_sum)):
        num = levels_sum[i]
        if num > maximal:
            max_index = i
            maximal = num

    return max_index + 1


if __name__ == "__main__":
    # root = [1,7,0,7,-8,null,null]
    # Output: 2 --> 7 + -8 = -1
    '''
         1
       /  \
      7    0
     /  \   
    7    -8   

    '''

    tree = TreeNode(1)
    tree.left = TreeNode(7, TreeNode(7, None, None), TreeNode(-8, None, None))
    tree.right = TreeNode(0, None, None)

    print(max_level_sum(tree))
