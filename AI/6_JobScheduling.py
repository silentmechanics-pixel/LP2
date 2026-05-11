jobs = [
    ('J1', 100, 2),
    ('J2', 50, 1),
    ('J3', 150, 2),
    ('J4', 200, 1)
]

# Sort jobs by profit descending
jobs.sort(key=lambda x: x[1], reverse=True)

slots = [False] * 3

result = []

profit = 0

for job in jobs:

    name, gain, deadline = job

    # Find free slot
    for j in range(deadline - 1, -1, -1):

        if slots[j] == False:

            slots[j] = True

            result.append(name)

            profit += gain

            break

print("Selected Jobs:", result)

print("Total Profit:", profit)