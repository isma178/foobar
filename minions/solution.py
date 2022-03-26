def solution(data, n):
    res = []
    for x, y in enumerate(data):
        if data.count(y) <= n:
            res.append(y)
    return res
