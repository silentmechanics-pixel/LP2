# edges = [
#     (2, 'A', 'B'),
#     (3, 'B', 'D'),
#     (5, 'C', 'D'),
#     (6, 'A', 'C'),
#     (8, 'A', 'D')
# ]
edges = []
vertices = int(input("Enter no of vertices: "))
num = int(input("Number of edges: "))
for i in range (num):
    v1 = input("Enter v1: ")
    v2 = input("Enter v2: ")
    weight = int(input("Input enter weight: "))
    edges.append((weight, v1, v2))
print(edges)

start = input("Enter starting vertice: ")
selected = [start]

print("Minimum Spanning Tree:\n")

while len(selected) < vertices:

    minimum = 999

    x = ""
    y = ""

    for weight, v1, v2 in edges:

        if v1 in selected and v2 not in selected:

            if weight < minimum:

                minimum = weight

                x = v1
                y = v2

        elif v2 in selected and v1 not in selected:

            if weight < minimum:

                minimum = weight

                x = v2
                y = v1

    print(x, "-", y, "=", minimum)

    selected.append(y)