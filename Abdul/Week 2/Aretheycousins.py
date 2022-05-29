# may 29th
# abdul

class TreeNode:
    def __init__(self,val:str):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def are_they_cousins(self,root:TreeNode,person1:str,person2:str)->bool:

        answer = {}

        def dfs(root, parent = None, l = 0):

            # base case
            if not root: return


            # check to see if the current value
            # matches either person1 or person2
            if root.val in [person1, person2]:
                answer[root.val] = (parent, l)

            # return 
            if len(answer) == 2:
                return

            # recursive call
            dfs(root.left, root, l+1)
            dfs(root.right, root, l+1)

        # recursive call
        dfs(root)

        # recursive call
        return answer[person1][0] != answer[person2][0] and answer[person1][1] == answer[person2][1]





tree = TreeNode("Omar")
tree.left = TreeNode("Jama")
tree.right = TreeNode("Gedi")
tree.left.left = TreeNode("Abdi")
tree.right.right = TreeNode("Nimo")

sol = Solution()
print(sol.are_they_cousins(tree,"Abdi","Nimo"))