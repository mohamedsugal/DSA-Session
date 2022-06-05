class TreeNode:
    def __init__(self,val:str):
        self.val = val
        self.left = None
        self.right = None


class Solution:
   #using recursion
    def are_they_cousins(self,root:TreeNode,person1:str,person2:str)->bool:
        map = {}
        def dfs(root, parent, depth, person1, person2):
            if not root:
                return False
        
            dfs(root.left, root, depth + 1, person1, person2)
            dfs(root.right, root, depth + 1, person1, person2)
            
            if root.val in (person1, person2):
                map[root.val] = (parent, depth)
        
        dfs(root, None, 0, person1, person2)

        return person1 in map and person2 in map and map[person1][0] != map[person2][0] and map[person1][1] == map[person2][1]
        

        # self.p1_parent = None
        
        # self.p1_depth = 0
        # self.p1_found = False

        # self.p2_parent = None
        # self.p2_depth = 0
        # self.p2_found = False

        # # using a helper function to keep track of the parent and depth of the tree

        # def find_cousins(node:TreeNode,parent:TreeNode,depth:int)->bool:
        #     if not node:
        #         return False

        #     if person1 == node.val:
            
        #         self.p1_found = True
                
        #         self.p1_depth = depth
                
        #         self.p1_parent = parent

        #     if person2 == node.val:
            
        #         self.p2_found = True
            
        #         self.p2_depth = depth
            
        #         self.p2_parent = parent

            
        #     find_cousins(node.left,node,depth+1)
        #     find_cousins(node.right,node,depth+1)

        # find_cousins(root,None,0)
        # if self.p1_parent != self.p2_parent and self.p1_depth == self.p2_depth and self.p1_found and self.p2_found:
        #     return True
        # return False




    # using iteration

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

sol = Solution()
print(sol.are_they_cousins(tree,"Abdi","Greg"))

       