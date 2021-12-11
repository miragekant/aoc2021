def solve():
    with open('input.txt') as f:
        depths = [int(d) for d in f.readlines()]
        sum_of_depths = []

        for i in range(len(depths) - 2):
            sum_of_depths.append(depths[i] + depths[i + 1] + depths[i + 2])
        
        count = 0
        for i in range(1, len(sum_of_depths)):
            if sum_of_depths[i] > sum_of_depths[i - 1]:
                count += 1

    return count 

if __name__ == '__main__':
    print(f'Answer: {solve()}')
