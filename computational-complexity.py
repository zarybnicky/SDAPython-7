

xs = [1, 2, 3, 4, 5, 6]
n = len(xs)

# O(1)
# array access
# appending to linked list
# mathematical operations (addition)

# O(log n)
# tree algorithms (access)

# O(n)
for i in range(n):
    expensive_operation(i)

# O(n * log n)
# sorting algorithms
# tree algorithms (creation)

# O(n^2)
# bubble sort
for i in range(n):
    for i in range(n):
        expensive_operation(i)

# O(n^3)
# matrix multiplication
for i in range(n):
    for i in range(n):
        for i in range(n):
            expensive_operation(i)
