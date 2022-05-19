# A class to store a binary tree node
class City:
    def __init__(self, cityName, left=None, right=None, distance=0):
        self.cityName = cityName
        self.distance = distance
        self.left = left
        self.right = right


class Tree:

	def __init__(self, root):
		self.root = root




root = City("Seattle")

root.right = City("Denver",distance=1305)
root.right.right = City("Maimi",distance=2064)
root.right.left = City("Los Angeles",distance=1016)
root.right.left.right = City("Dallas",distance=1435)
root.right.left.left = City("Minneapolis",distance=990)

root.left = City("New York",distance=1305)
root.left.left = City("Boston",distance=216)

tree = Tree(root)

