def solve():
    count = 0
    with open('input.txt') as f:
        depths = [int(line) for line in f.readlines()]
        for i in range(1, len(depths)):
            if depths[i] > depths[i - 1]:
                count += 1
        
    return count

if __name__ == '__main__':
    print(f'Answer: {solve()}') 
