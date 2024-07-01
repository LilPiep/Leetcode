def findCenter(edges):
    for e in edges[0]:
        if e in edges[1]:
            return e