def update(b, m, index, n):
    """Update the boolean matrix for corresponding
    bingo board.
    """

    for i in range(5):
        for j in range(5):
            if b[index][i][j] == n:
                m[index][i][j] = True
                break

def check(m):
    """Check if a board (5x5) reaches win condition
    given its boolean matrix.
    """

    # Check rows & columns 
    return any([all(row) for row in m]) or any([all([m[j][i] for j in range(5)]) for i in range(5)])

def solve():
    result = 0

    with open('input.txt') as f:
        inputs = f.readlines()
        numbers = [int(n) for n in inputs[0].strip().split(',')] 

        boards = []
        board = []
        for line in inputs[2:]:
            if line != '\n':
                board.append([int(n) for n in line.strip().split()])
            else:
                boards.append(board)
                board = []
        boards.append(board)

        marked = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]

        last_winner = -1
        last = -1
        wins = [False for _ in range(len(boards))]

        for n in numbers:
            for i in range(len(boards)):
                update(boards, marked, i, n)

                if not wins[i] and check(marked[i]):
                    last_winner = i
                    last = n
                    wins[i] = True

            if all(wins):
                break
            
        total = 0  
        for i in range(5):
            for j in range(5):
                if not marked[last_winner][i][j]:
                    total += boards[last_winner][i][j] 
        result = total * last

    return result

if __name__ == '__main__':
    print(f'Answer: {solve()}')
