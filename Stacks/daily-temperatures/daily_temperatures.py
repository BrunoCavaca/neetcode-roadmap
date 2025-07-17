def dailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for i,v in enumerate(temperatures):
        while stack and v > stack[-1][1]:
            idx = stack[-1][0]
            res[idx] = i - idx
            stack.pop()
        stack.append([i,v])

    return res