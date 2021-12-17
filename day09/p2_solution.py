def bfs(g, t, p):
    queue = []
    size = 0

    queue.append(p)
    t[p[0]][p[1]] = True

    while queue:
        curr = queue.pop(0)
        size += 1

        if curr[0] + 1 <= 99 and not t[curr[0] + 1][curr[1]] and g[curr[0] + 1][curr[1]] != '9':
            queue.append((curr[0] + 1, curr[1]))
            t[curr[0] + 1][curr[1]] = True 
        
        if curr[0] - 1 >= 0 and not t[curr[0] - 1][curr[1]] and g[curr[0] - 1][curr[1]] != '9':
            queue.append((curr[0] - 1, curr[1]))
            t[curr[0] - 1][curr[1]] = True 

        if curr[1] + 1 <= 99 and not t[curr[0]][curr[1] + 1] and g[curr[0]][curr[1] + 1] != '9':
            queue.append((curr[0], curr[1] + 1))
            t[curr[0]][curr[1] + 1] = True 

        if curr[1] - 1 >= 0 and not t[curr[0]][curr[1] - 1] and g[curr[0]][curr[1] - 1] != '9':
            queue.append((curr[0], curr[1] - 1))
            t[curr[0]][curr[1] - 1] = True 

    return size

def solve():
    result = 0

    # Input is an 100 x 100 matrix
    with open('input.txt') as f:
        lines = f.readlines()
        low_points = []

        # Check four corners 
        if lines[0][0] < lines[0][1] and lines[0][0] < lines[1][0]:
            low_points.append((0, 0))
        
        if lines[0][99] < lines[0][98] and lines[0][99] < lines[1][99]:
            low_points.append((0, 99))

        if lines[99][0] < lines[99][1] and lines[99][0] < lines[98][0]:
            low_points.append((99, 0))

        if lines[99][99] < lines[99][98] and lines[99][99] < lines[98][99]:
            low_points.append((99, 99))

        # Check border
        for i in range(1, 99):
            if lines[0][i] < lines[0][i - 1] and lines[0][i] < lines[0][i + 1] \
               and lines[0][i] < lines[1][i]:
                low_points.append((0, i))

            if lines[i][0] < lines[i - 1][0] and lines[i][0] < lines[i + 1][0] \
               and lines[i][0] < lines[i][1]:
                low_points.append((i, 0))
            
            if lines[99][i] < lines[99][i - 1] and lines[99][i] < lines[99][i + 1] \
               and lines[99][i] < lines[98][i]:
                low_points.append((99, i))
            
            if lines[i][99] < lines[i - 1][99] and lines[i][99] < lines[i + 1][99] \
               and lines[i][99] < lines[i][98]:
                low_points.append((i, 99))

        # Check inner
        for i in range(1, 99):
            for j in range(1, 99):
                if lines[i][j] < lines[i - 1][j] and lines[i][j] < lines[i + 1][j] \
                   and lines[i][j] < lines[i][j - 1] and lines[i][j] < lines[i][j + 1]:
                    low_points.append((i, j))

        traversed = [[False for _ in range(100)] for _ in range(100)]
        sizes = sorted([bfs(lines, traversed, p) for p in low_points], reverse=True)
        result = sizes[0] * sizes[1] * sizes[2]

    return result

def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()