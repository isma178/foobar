def solution(h, q):
    root = 2**h -1
    def_parent = -1
    depth = 0
    p = []
    for conv in q:
        node = root
        x = depth
        parent = def_parent
        while conv != node:
            parent = node
            x += 1
            left = node - 2**(h-x)
            right = node -1
            if conv > left:
                node = right
            else:
                node = left
        p.append(parent)
    return p
    