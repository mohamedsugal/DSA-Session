class TreeNode: 
    def __init__(self, name, distance) -> None:
        self.name = name 
        self.distance = distance
        self.left = self.right = None 

cities = TreeNode("Seattle", 0)
cities.left = TreeNode("Denver", 1305)
cities.right = TreeNode("New York", 2401)
cities.right.right = TreeNode("Boston", 216)
cities.left.left = TreeNode("Miami", 2064)
cities.left.right = TreeNode("Los Angles", 1016)
cities.left.right.left = TreeNode("Dallas", 1435)
cities.left.right.left.right = TreeNode("Minneapolis", 990)

def find_path(city: TreeNode, destination: str, totalPath: str) -> str: 
	# return if city is None
	if not city:
		return 

	# we arrive at the city that we are looking for
	if city.name == destination:  
		return totalPath + " -> " + city.name

	# recursive
	return find_path(city.left, destination, totalPath + " -> " + city.name) or \
	find_path(city.right, destination, totalPath + " -> " +  city.name)  
 
def find_distance(city: TreeNode, destination: str, totalDis: int) -> str:   
	# return if city is None
	if city is None:
		return 

	# we arrive at the city that we are looking for
	if city.name == destination:    
		return totalDis + city.distance 

	return find_distance(city.left, destination, totalDis + city.distance) or \
	find_distance(city.right, destination, totalDis + city.distance) 


print(find_path(cities, "Dallas","")) 

print(find_distance(cities, "Dallas",0)) 
print(find_distance(cities, "Minneapolis",0)) 
