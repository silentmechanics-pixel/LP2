graph = {}

n = int(input("Enter no of Vertices: "))

for i in range(n):
  name = input("Enter name of Vertice: ")
  graph[name] = []

e = int(input("Enter no of edges: "))

for i in range(e):
  v1 = input("Enter vertex 1: ")
  v2 = input("Enter vertex 2: ")

  graph[v1].append(v2)
  graph[v2].append(v1)

visited = set()

def dfs(vertex, visited):
  visited.add(vertex)
  print(vertex)

  for neighbour in graph[vertex]:
    if neighbour not in visited:
      dfs(neighbour, visited)

start = input("Enter starting vertex: ")
print("DFS traversal: ")
dfs(start, visited)