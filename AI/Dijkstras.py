graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

visited = []

distance = {
    'A': 999,
    'B': 999,
    'C': 999,
    'D': 999
}

start = input("Enter starting vertex: ")

distance[start] = 0

while len(visited) < len(graph):

    minimum = 999
    current = ""

    # Find nearest unvisited vertex
    for vertex in distance:

        if vertex not in visited and distance[vertex] < minimum:

            minimum = distance[vertex]
            current = vertex

    visited.append(current)

    # Update distances
    for neighbour, weight in graph[current]:

        if distance[current] + weight < distance[neighbour]:

            distance[neighbour] = distance[current] + weight

print("\nShortest Distances:\n")

for vertex in distance:

    print(start, "to", vertex, "=", distance[vertex])