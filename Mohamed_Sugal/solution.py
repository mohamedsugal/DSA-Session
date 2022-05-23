class TreeNode:
    def __init__(self, name, distance) -> None:
        self.name = name
        self.distance = distance
        self.left = self.right = None


class Solution:
    @staticmethod
    def find_path(cities, destination):
        total_path = []

        def dfs(city, path):
            if not city:
                return
            if city.name == destination:
                path += city.name
                total_path.append(path)
                return
            path += city.name + " -> "
            dfs(city.left, path)
            dfs(city.right, path)

        dfs(cities, "")
        return "".join(total_path)

    def find_path_iter(self, cities, destination):
        stack = [(cities, "")]
        while stack:
            city, path = stack.pop()
            if city.name == destination:
                path += city.name
                return path
            path += city.name + " -> "
            if city.right:
                stack.append((city.right, path))
            if city.left:
                stack.append((city.left, path))
        return "path not found!"

    def find_distance(self, cities, destination):
        self.total_distance = 0

        def dfs(city, curr_distance):
            if not city:
                return
            if city.name == destination:
                self.total_distance = curr_distance + city.distance
                return
            curr_distance += city.distance
            dfs(city.left, curr_distance)
            dfs(city.right, curr_distance)

        dfs(cities, 0)
        return self.total_distance

    def find_distance_iter(self, cities, destination):
        stack = [(cities, 0)]
        while stack:
            city, dist = stack.pop()
            if city.name == destination:
                dist += city.distance
                return dist
            dist += city.distance
            if city.right:
                stack.append((city.right, dist))
            if city.left:
                stack.append((city.left, dist))
        return 0


if __name__ == '__main__':
    cities = TreeNode("Seattle", 0)
    cities.left = TreeNode("Denver", 1305)
    cities.right = TreeNode("New York", 2401)
    cities.right.right = TreeNode("Boston", 216)
    cities.left.left = TreeNode("Miami", 2064)
    cities.left.right = TreeNode("Los Angles", 1016)
    cities.left.right.left = TreeNode("Dallas", 1435)
    cities.left.right.left.right = TreeNode("Minneapolis", 990)

    print(Solution().find_path(cities, "Dallas"))
    print(Solution().find_path_iter(cities, "Dallas"))
    print(Solution().find_distance(cities, "Minneapolis"))
    print(Solution().find_distance_iter(cities, "Minneapolis"))
