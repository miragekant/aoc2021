def solve():
    result = 0 

    with open('input.txt') as f:
        ps = sorted([int(p) for p in f.readline().strip().split(',')])
        n = len(ps)
        med = ps[n // 2] if n % 2 != 0 else \
              (ps[n // 2] + ps[n // 2 - 1]) // 2

        result = sum([abs(p - med) for p in ps])

    return result


def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()
