from typing import List
class TreeNode:
    def __init__(self,value:str,weight:int):
        self.value = value
        self.left = None
        self.right = None
        self.weight = weight

def find_path(root:TreeNode,city:str)->str:
    def helper(node:TreeNode,path:List[str],city:str)->bool:
        if not node: return
        path.append(node.value) 
        if city == node.value or helper(node.left,path,city) or helper(node.right,path,city):          
            return True
        path.pop() 
        return False

    paths:List[str] = []
    helper(root,paths,city)
    res = ""
    for p in paths:
         res += p + " -> "
    return res

# find distance
def measure_dist(root:TreeNode,city:str)->list[int]:

    dist1:List[int]= [root.weight]

    def helper(node:TreeNode,path:List[str],city:str)->bool:
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