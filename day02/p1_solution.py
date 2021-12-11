def solve():
    coordinate = [0, 0]

    with open('input.txt') as f:
        courses = f.readlines() 

        for c in courses:
            direction, distance = c.strip().split() 
            distance = int(distance)

            if direction == 'forward':
                coordinate[0] += distance
            elif direction == 'down':
                coordinate[1] += distance
            else:
                coordinate[1] -= distance

    return coordinate[0] * coordinate[1]

if __name__ == '__main__':
    print(f'Answer: {solve()}')
