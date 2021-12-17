def solve():
    result = 0

    # Input is an 100 x 100 matrix
    with open('input.txt') as f:
        lines = f.readlines()

        risk = 0

        # Check four corners 
        if lines[0][0] < lines[0][1] and lines[0][0] < lines[1][0]:
            risk += int(lines[0][0]) + 1
        
        if lines[0][99] < lines[0][98] and lines[0][99] < lines[1][99]:
            risk += int(lines[0][99]) + 1

        if lines[99][0] < lines[99][1] and lines[99][0] < lines[98][0]:
            risk += int(lines[99][0]) + 1

        if lines[99][99] < lines[99][98] and lines[99][99] < lines[98][99]:
            risk += int(lines[99][99]) + 1

        # Check border
        for i in range(1, 99):
            if lines[0][i] < lines[0][i - 1] and lines[0][i] < lines[0][i + 1] \
               and lines[0][i] < lines[1][i]:
                risk += int(lines[0][i]) + 1

            if lines[i][0] < lines[i - 1][0] and lines[i][0] < lines[i + 1][0] \
               and lines[i][0] < lines[i][1]:
                risk += int(lines[i][0]) + 1
            
            if lines[99][i] < lines[99][i - 1] and lines[99][i] < lines[99][i + 1] \
               and lines[99][i] < lines[98][i]:
                risk += int(lines[99][i]) + 1
            
            if lines[i][99] < lines[i - 1][99] and lines[i][99] < lines[i + 1][99] \
               and lines[i][99] < lines[i][98]:
                risk += int(lines[i][99]) + 1

        # Check inner
        for i in range(1, 99):
            for j in range(1, 99):
                if lines[i][j] < lines[i - 1][j] and lines[i][j] < lines[i + 1][j] \
                   and lines[i][j] < lines[i][j - 1] and lines[i][j] < lines[i][j + 1]:
                    risk += int(lines[i][j]) + 1

        result = risk

    return result

def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()