def arrayManipulation(n, queries):
    arr = [0] * n

    for a, b, k in queries:
        arr[a - 1] += k
        if b < n:
            arr[b] -= k

    max_val = 0
    running_sum = 0

    for val in arr:
        running_sum += val
        if running_sum > max_val:
            max_val = running_sum

    return max_val
