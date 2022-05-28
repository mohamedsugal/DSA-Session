class TreeNode:
    def __init__(self,val:str):
        self.val = val
        self.left = None
        self.right = None

#using recursion

def are_they_cousins(root:TreeNode,person1:str,person2:str)->bool:

    p1_parent = None
    p1_depth = 0
    p1_found = False

    p2_parent = None
    p2_depth = 0
    p2_found = False

    # using a helper function to keep track of the parent and depth of the tree

    def find_cousins(node:TreeNode,parent:TreeNode,depth:int)->bool:
        if not node:
            return False

        if person1 == node.val:
           nonlocal p1_found 
           p1_found = True
           nonlocal p1_depth 
           p1_depth = depth
           nonlocal p1_parent
           p1_parent = parent

        if person2 == node.val:
            nonlocal p2_found
            p2_found = True
            nonlocal p2_depth
            p2_depth = depth
            nonlocal p2_parent
            p2_parent = parent

        
        find_cousins(node.left,node,depth+1)
        find_cousins(node.right,node,depth+1)

    find_cousins(root,None,0)
    if p1_parent != p2_parent and p1_depth == p2_depth and p1_found and p2_found:
        return True
    return False




# using iterative

# def are_they_cousins(root,person1,person2):

#     if not root:
#         return False
#     stack = [(root,None,0)]

#     while stack:
#         node,parent,depth = stack.pop()

#         if person1 == node.val:
#             p1_found = True
#             p1_depth = depth
#             p1_parent = parent
#         if person2 == node.val:
#             p2_found = True
#             p2_depth = depth
#             p2_parent = parent

#         if node.right:
#             stack.append((node.right,node,depth+1))
#         if node.left:
#             stack.append((node.left,node,depth+1))

#     if p1_parent != p2_parent and p1_depth == p2_depth and p1_found and p2_found:
#         return True
#     return False


tree = TreeNode("Omar")
tree.left = TreeNode("Jama")
tree.right = TreeNode("Gedi")
tree.left.left = TreeNode("Abdi")
tree.right.right = TreeNode("Nimo")

print(are_they_cousins(tree,"Abdi","Nimo"))

       