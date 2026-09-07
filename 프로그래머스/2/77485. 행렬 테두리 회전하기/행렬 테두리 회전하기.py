def solution(rows, columns, queries):
    answer = []
    arr = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = columns*i+j+1

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        visited = []
        temp = arr[x1][y1]
        visited.append(temp)
        
        for x in range(x1, x2):
            arr[x][y1] = (temp2 := arr[x+1][y1])
            visited.append(temp2)
        
        for y in range(y1, y2):
            arr[x2][y] = (temp2 := arr[x2][y+1])
            visited.append(temp2)
        
        for x in range(x2, x1, -1):
            arr[x][y2] = (temp2 := arr[x-1][y2])
            visited.append(temp2)
      
        for y in range(y2, y1, -1):
            arr[x1][y] = (temp2 := arr[x1][y-1])
            visited.append(temp2)
        
        arr[x1][y1+1] = temp
        
        answer.append(min(visited))
        
        
    return answer