def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        idx = query[0]
        x = query[1]
        y = query[2]

        if idx == 1:
            idx = (x ^ lastAnswer) % n
            arr[idx].append(y)
        elif idx == 2:
            idx = (x ^ lastAnswer) % n
            lastAnswer = arr[idx][y % len(arr[idx])]

            answers.append(lastAnswer)

    return answers
