class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class TreeNode:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(data)
                        break
                if data > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(data)
                        break

    def average_of_levels(self, root):
        if root is None:
            return []

        queue, res, = [root], []
        while len(queue) != 0:
            level_sum = 0
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            res.append(level_sum / size)

        return res

    '''
             3
            / \
           9   20
              /  \
             15   7


        [3,9,20,null,null,15,7] for level order BFS
        [3.00000,14.50000,11.00000] Average of levels

    '''


tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)

print(TreeNode().average_of_levels(tree))
