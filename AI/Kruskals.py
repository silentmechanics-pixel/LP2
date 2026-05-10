edges=[]
num = int(input("Enter no of EDGES: "))
for i in range(num):
  v1 = input("Enter v1: ")
  v2 = input("Enter v2: ")
  weight = input("Enter weight:")

  edges.append((weight,v1,v2))


edges.sort()

vertices = ['A','B','C','D']

parent = {}

for v in vertices:
  parent[v] = v


def find(vertex):

  if parent[vertex] == vertex:
    return vertex

  return find(parent[vertex])


def union(v1, v2):

  root1 = find(v1)
  root2 = find(v2)

  parent[root2] = root1


print("Minimum Spanning Tree:\n")

for edge in edges:

  weight, v1, v2 = edge

  if find(v1) != find(v2):

    union(v1, v2)

    print(v1, "-", v2, "=", weight)