#!/usr/bin/python3
''' defining pascal_triangle function '''


def pascal_triangle(n):
    ''' returns a list of lists of integers representing the Pascal’s
    triangle of n '''
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        temp = [1]
        for j in range(len(tria) - 1):
            temp.append(tria[j] + tria[j+1])
        temp.append(1)
        triangles.append(temp)
    return trianlges
