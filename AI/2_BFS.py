graph = {}

num = int(input("Enter no of vertices: "))
for i in range(num):
  name = input("Enter name of vertex: ")
  graph[name] = []

e =  int(input("Enter no of edges: "))

for i in range(e):
  v1 = input("Enter v1: ")
  v2 = input("Enter v2: ")
  
  graph[v1].append(v2)
  graph[v2].append(v1)

def bfs(start):

  visited =  set()
  queue = []

  visited.add(start)
  queue.append(start)

  while queue:
    vertex = queue.pop(0)
    print(vertex)

    for neighbours in graph[vertex]:
      if neighbours not in visited:
        visited.add(neighbours)
        queue.append(neighbours)

start = input("Enter start: ")
bfs(start)