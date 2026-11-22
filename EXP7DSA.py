
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[0 for i in range(vertices)]
                    for j in range(vertices)]
        self.visited = [False] * vertices

    def add_edge(self, source, destination):
        self.adj[source][destination] = 1
        self.adj[destination][source] = 1

    def display_graph(self):
        print("\nAdjacency Matrix:")
        for i in range(self.vertices):
            print(self.adj[i])

    def dfs_util(self, vertex, traversal):
        self.visited[vertex] = True
        traversal.append(vertex)

        for neighbour in range(self.vertices):
            if (self.adj[vertex][neighbour] == 1
                    and not self.visited[neighbour]):
                self.dfs_util(neighbour, traversal)

    def dfs(self, start_vertex):
        if start_vertex < 0 or start_vertex >= self.vertices:
            print("Invalid starting vertex.")
            return []

        self.visited = [False] * self.vertices
        traversal = []

        self.dfs_util(start_vertex, traversal)
        return traversal


def main():
    vertices = int(input("Enter number of vertices: "))
    graph = Graph(vertices)

    edges = int(input("Enter number of edges: "))

    for i in range(edges):
        source, destination = map(int, input("Enter edge: ").split())
        graph.add_edge(source, destination)

    graph.display_graph()

    start = int(input("Enter starting vertex for DFS: "))
    traversal = graph.dfs(start)

    if traversal:
        print("DFS Traversal:", " -> ".join(map(str, traversal)))


if __name__ == "__main__":
    main()
