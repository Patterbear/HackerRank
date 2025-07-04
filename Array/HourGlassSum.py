def hourglassSum(arr):
    max_sum = -float("inf")
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            mid = arr[i + 1][j + 1]
            bot = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            hourglass = top + mid + bot
            if hourglass > max_sum:
                max_sum = hourglass
    return max_sum
