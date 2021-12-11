def solve():
    result = 0

    with open('input.txt') as f:
        lines = f.readlines() 
        length = len(lines[0].strip())
        counts = [[0, 0] for _ in range(length)]

        for l in lines:
            for i in range(length):
                if l[i] == '0':
                    counts[i][0] += 1
                else:
                    counts[i][1] += 1
        
        # How about when the counts are the same?
        gamma = []
        epsilon = []
        for count in counts:
            if count[0] > count[1]:
                gamma.append('0')
                epsilon.append('1')
            else:
                gamma.append('1')
                epsilon.append('0')

        gamma = int(''.join(gamma), 2)
        epsilon = int(''.join(epsilon), 2)
        result = gamma * epsilon

    return result
    
if __name__ == '__main__':
    print(f'Answer: {solve()}')
