def solve():
    result = 0

    with open('input.txt') as f:
        inputs = [int(t) for t in f.readlines()[0].strip().split(',')]

        # Initialize the timer (counter)
        timer = [0 for _ in range(9)] 
        # Value ranges from 0 to 8
        for i in range(9):
            timer[i] = 0

        for t in inputs:
            timer[t] += 1

        # Loop for 256 days
        for _ in range(256):
            spawn_count = timer[0]
            for i in range(8):
                timer[i] = timer[i + 1]
            timer[8] = 0
            timer[6] += spawn_count
            timer[8] += spawn_count
            print(timer)
        
        result = sum(timer)

    return result

def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()
