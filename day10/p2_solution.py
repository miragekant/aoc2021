brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
open_brackets = ['(', '[', '{', '<']
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
points = {'(': 1, '[': 2, '{': 3, '<': 4}

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

def complete(line):
    stack = []
    score = 0
    for c in line:
        if c in open_brackets:
            stack.append(c)
        else:
            stack.pop()
    while stack:
        c = stack.pop() 
        score = score * 5 + points[c]

    return score
        

def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        incomplete_lines = []
        for line in lines:
            if check_corrupt(line) == 0:
                incomplete_lines.append(line) 

        scores = sorted([complete(line) for line in incomplete_lines])

        print(f'Answer: {scores[len(scores) // 2]}')

if __name__ == '__main__':
    main()