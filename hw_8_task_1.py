import heapq


def heap_sort_desc(iterable):
    if len(iterable) % 2 != 0:
        raise Exception("Not enough cables to unite. Add one more.")
    h = []
    heapq.heapify(iterable)

    for value in iterable:
        heapq.heappush(h, value)
    min_values = [heapq.heappop(h) for _ in range(len(h))]
    min_values = min_values[:len(min_values) // 2]
    print(f"Min values: {min_values}")

    for value in iterable:
        heapq.heappush(h, -value)
    max_values = [-heapq.heappop(h) for _ in range(len(h))]
    max_values = max_values[:len(max_values) // 2]
    print(f"Min values: {max_values}")

    res = [a + b for a, b in zip(max_values, min_values)]
    print(f"Sum of two: {res}")
    return sum(res)


arr = [12, 11, 13, 5, 6, 7]
print("Sum of all:", heap_sort_desc(arr))
