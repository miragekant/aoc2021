def solve():
    result = 0

    with open('input.txt') as f:
        lines = f.readlines()
        ocean = [[0 for _ in range(1000)] for _ in range(1000)]

        for l in lines:
            start, _, end = l.strip().split()
            start = [int(x) for x in start.split(',')]
            end = [int(x) for x in end.split(',')]
         
            if start[0] == end[0]:
                if start[1] > end[1]:
                    start[1], end[1] = end[1], start[1]

                for i in range(start[1], end[1] + 1):
                    ocean[start[0]][i] += 1
            elif start[1] == end[1]:
                if start[0] > end[0]:
                    start[0], end[0] = end[0], start[0]

                for i in range(start[0], end[0] + 1):
                    ocean[i][start[1]] += 1
        
        count = 0
        for i in range(1000):
            for j in range(1000):
                if ocean[i][j] >= 2:
                    count += 1
        
        result = count

    return result 

if __name__ == '__main__':
    print(f'Answer: {solve()}')
