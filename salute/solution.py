def solution(s):
    hallway = list(s)
    counter = 0
    lefts = 0
    for x, y in enumerate(hallway):
        if y == ">":
            hallway[0:x] = [0]*x
            lefts = hallway.count("<")
            counter += lefts
    return counter*2
