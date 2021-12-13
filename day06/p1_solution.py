def solve():
    result = 0

    with open('input.txt') as f:
        prev = [int(t) for t in f.readlines()[0].strip().split(',')]
        curr = prev 
        for _ in range(80):
            new_count = 0
            curr = []

            for t in prev:
                if t != 0:
                    curr.append(t - 1)
                else:
                    curr.append(6)
                    new_count += 1

            for _ in range(new_count):
                curr.append(8)
            
            prev = curr

        result = len(curr)    

    return result 

def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()