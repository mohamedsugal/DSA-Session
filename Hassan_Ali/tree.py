
from multiprocessing.dummy import Array


class TreeNode:
    def __init__(self,value:str,weight:int):
        self.value = value
        self.left = None
        self.right = None
        self.weight = weight
# printing using inorder
# def print_tree(tree):
#     if not tree:
#         return

#     print(tree.value,tree.weight)
#     print_tree(tree.left)
#     print_tree(tree.right)

def find_path(root:TreeNode,city:str)->str:
    def helper(node:TreeNode,path:list[str],city:str):
        if not node: return
        path.append(node.value) 
        if city == node.value or helper(node.left,path,city) or helper(node.right,path,city):          
            return True
        path.pop() 
        return False

    paths = []
    helper(root,paths,city)
    res = ""
    for p in paths:
         res += p + " -> "
    return res

# find distance
def measure_dist(root:TreeNode,city:str)->list[int]:

    dist1:list[int]= [root.weight]

    def helper(node,path,city):
        if not node: return
        path.append(node.value) 
        if city == node.value or helper(node.left,path,city) or helper(node.right,path,city):        
            dist1[0] += node.weight
            return True
        path.pop() 
        return False

   
    helper(root,[],city)

    return dist1[0]

tree = TreeNode("Seattle",0)
tree.left = TreeNode("Denver",1305)
tree.right = TreeNode("New York",2401)
tree.left.left = TreeNode("Miami",2064)
tree.left.right = TreeNode("Los Angels",1016)
tree.left.right.left = TreeNode("Dallas",1435)
tree.left.right.left.right = TreeNode("Minneapolis",990)
tree.right.right = TreeNode("Boston",2016)

# print_tree(tree)
print (find_path(tree,"Dallas"))

print(measure_dist(tree,"Dallas"))