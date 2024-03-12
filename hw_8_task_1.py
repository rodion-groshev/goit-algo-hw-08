import heapq


def heap_sort_desc(iterable):
    h = []
    heapq.heapify(iterable)
    total = 0

    for value in iterable:
        heapq.heappush(h, value)

    while len(h) > 1:
        cable_1 = heapq.heappop(h)
        cable_2 = heapq.heappop(h)

        sum_of_2 = cable_1 + cable_2
        total += sum_of_2

        heapq.heappush(h, sum_of_2)

    return total


arr = [4, 6, 8, 12]
print("Sum of all:", heap_sort_desc(arr))
