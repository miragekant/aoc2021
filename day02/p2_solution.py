def solve():
    coordinate = [0, 0, 0]

    with open('input.txt') as f:
        courses = f.readlines() 

        for c in courses:
            direction, distance = c.strip().split() 
            distance = int(distance)

            if direction == 'forward':
                coordinate[0] += distance
                coordinate[1] += distance * coordinate[2]
            elif direction == 'down':
                coordinate[2] += distance
            else:
                coordinate[2] -= distance

    return coordinate[0] * coordinate[1]

if __name__ == '__main__':
    print(f'Answer: {solve()}')
