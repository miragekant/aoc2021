def solve():
    result = 0

    with open('input.txt') as f:
        prev_oxygen_ns = f.readlines() 
        prev_co2_ns = prev_oxygen_ns

        length = len(prev_oxygen_ns[0].strip())
        
        for i in range(length):
            if len(prev_oxygen_ns) == 1:
                break

            oxygen_count = [0, 0]
            oxygen_ns = []

            for n in prev_oxygen_ns:
                if n[i] == '0':
                    oxygen_count[0] += 1
                else:
                    oxygen_count[1] += 1
            
            mcb = '0' if oxygen_count[0] > oxygen_count[1] else '1'
            for n in prev_oxygen_ns:
                if n[i] == mcb:
                    oxygen_ns.append(n)
            
            prev_oxygen_ns = oxygen_ns

        for i in range(length):
            if len(prev_co2_ns) == 1:
                break

            co2_count = [0, 0]
            co2_ns = [] 
       
            for n in prev_co2_ns:
                if n[i] == '0':
                    co2_count[0] += 1
                else:
                    co2_count[1] += 1

            lcb = '1' if co2_count[0] > co2_count[1] else '0'
            for n in prev_co2_ns:
                if n[i] == lcb:
                   co2_ns.append(n)

            prev_co2_ns = co2_ns

        gamma = int(prev_oxygen_ns[0].strip(), 2)
        epsilon = int(prev_co2_ns[0].strip(), 2)
        result = gamma * epsilon

    return result
    
if __name__ == '__main__':
    print(f'Answer: {solve()}')
