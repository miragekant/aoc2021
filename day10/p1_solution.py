brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
open_brackets = ['(', '[', '{', '<']
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def check_corrupt(line):
    stack = []
    for c in line:
        if c in open_brackets:
            stack.append(c)
        else:
            if not stack or brackets[c] != stack[len(stack) - 1]:
                return scores[c] 
            else:
                stack.pop()

    return 0

def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        scores = sum([check_corrupt(line) for line in lines])
        print(f'Answer: {scores}')

if __name__ == '__main__':
    main()