matrix =[]
rows = 0
cols = 0
def searchNeighbors(i,j):
    if matrix[i][j] == 1:
        matrix[i][j] = -1 
        s = 0
        for ii in range(max(0, i-1), min(i+2, rows)):
            for jj in range(max(0, j-1), min(j+2, cols)):
                s += searchNeighbors(ii,jj)
        print(i,j,s)
        return 1 + s
    return 0

def connectedCell(matrix):
    global rows
    global cols
    rows = len(matrix)
    cols = len(matrix[0])
    mx = 0
    for i in range(0, rows):
        for j in range(0, cols):
            mx = max(mx, searchNeighbors(i,j))
    return mx





