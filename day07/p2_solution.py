from math import ceil, floor

def cost(x, arr):
    return sum([(x - xi) ** 2 + abs(x - xi) for xi in arr])   

def solve():
    result = 0 

    with open('input.txt') as f:
        ps = sorted([int(p) for p in f.readline().strip().split(',')])
        n = len(ps)

        """
        med = ps[n // 2] if n % 2 != 0 else \
              (ps[n // 2] + ps[n // 2 - 1]) // 2

        avg = sum(ps) / n 
        avg = ceil(avg) if avg > med else floor(avg)

        left = min(med, avg)
        right = max(med, avg)
        """

        left = 0
        right = max(ps)

        """
        while left < right:
            mid = (left + right) // 2
            curr_cost = cost(mid, ps)
            curr_left_cost = cost(mid - 1, ps)
            curr_right_cost = cost(mid + 1, ps)
            print(curr_cost)
            if curr_left_cost < curr_cost and curr_cost < curr_right_cost:
                right = mid
            elif curr_left_cost > curr_cost and curr_cost > curr_right_cost:
                left = mid
            else:
                break

        result = cost(right, ps) // 2 
        """

        result = min([cost(x, ps) for x in range(max(ps))]) // 2

    return result  


def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()
