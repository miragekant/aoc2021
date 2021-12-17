"""def equal(s1, s2):
    segs1 = {'a': False, 'b': False, 'c': False, 'd': False,
             'e': False, 'f': False, 'g': False}
    
    segs2 = {'a': False, 'b': False, 'c': False, 'd': False,
             'e': False, 'f': False, 'g': False}

    for i in range(len(s1)):
        segs1[s1[i]] = True

    for i in range(len(s2)):
        segs2[s2[i]] = True

    for k in segs1:
        if segs1[k] != segs2[k]:
            return False

    return True
"""

def diff(s1, s2):
    """Returns a dict which represents segments. 
    """
    segments = {'a': False, 'b': False, 'c': False, 'd': False,
            'e': False, 'f': False, 'g': False}

    for i in range(len(s1)):
        segments[s1[i]] = True 
    
    for i in range(len(s2)):
        if s2[i] in segments and segments[s2[i]]:
            segments[s2[i]] = False 

    result = ''    
    for k, v in segments.items():
        if v:
            result += k
    
    return result 



def derive(ps):
    cipher = {}
    length_5s = []
    length_6s = []
    one = four = seven = eight = -1

    for i in range(10): 
        # Figure out 1, 4, 7, 8
        # and group 2, 3, 5 (with length 5)
        # and group 0, 6, 9 (with length 6)

        length = len(ps[i])
        if length == 5:
            length_5s.append(i)
        elif length == 6:
            length_6s.append(i)
        elif length == 2:
            one = i
            cipher[''.join(sorted(ps[i]))] = '1' 
        elif length == 4:
            four = i
            cipher[''.join(sorted(ps[i]))] = '4' 
        elif length == 3:
            seven = i
            cipher[''.join(sorted(ps[i]))] = '7' 
        elif length == 7:
            eight = i
            cipher[''.join(sorted(ps[i]))] = '8' 

    b_and_d = diff(ps[four], ps[one])
    e_and_g = diff(diff(ps[eight], ps[four]), ps[seven])

    # Check 2, 3, 5, get 3 and e (g)
    if len(diff(diff(ps[length_5s[0]], ps[length_5s[1]]), ps[length_5s[2]])) == 0:
        three = length_5s[0]
        two_and_five = [length_5s[1], length_5s[2]]
    elif len(diff(diff(ps[length_5s[1]], ps[length_5s[0]]), ps[length_5s[2]])) == 0:
        three = length_5s[1]
        two_and_five = [length_5s[0], length_5s[2]]
    else:
        three = length_5s[2]
        two_and_five = [length_5s[0], length_5s[1]]
    cipher[''.join(sorted(ps[three]))] = '3'

    e = diff(e_and_g, ps[three])
        
    # Check 0, 6, 9, get 9 (9 has no e)
    zero_and_six = []
    for i in length_6s:
        if e not in ps[i]:
            nine = i
        else:
            zero_and_six.append(i)
    cipher[''.join(sorted(ps[nine]))] = '9'

    if len(diff(ps[zero_and_six[0]], b_and_d)) > len(diff(ps[zero_and_six[1]], b_and_d)):
        zero, six = zero_and_six[0], zero_and_six[1]
    else:
        zero, six = zero_and_six[1], zero_and_six[0]
    cipher[''.join(sorted(ps[zero]))] = '0'
    cipher[''.join(sorted(ps[six]))] = '6'

    # Figure out 2, 5
    if e in ps[two_and_five[0]]:
        two, five = two_and_five[0], two_and_five[1]
    else:
        two, five = two_and_five[1], two_and_five[0]
    cipher[''.join(sorted(ps[two]))] = '2'
    cipher[''.join(sorted(ps[five]))] = '5'

    #return [zero, one, two, three, four, five, six, seven, eight, nine]
    return cipher
        
def decode(cipher, signals):
    return int(''.join([cipher[''.join(sorted(s))] for s in signals]))

def solve():
    result = 0

    with open('input.txt') as f:
        inputs = [line.strip().split(' | ') for line in f.readlines()]
        result = 0

        for entry in inputs:
            patterns = entry[0].split()
            signals = entry[1].split()

            # Decode patterns  
            cipher = derive(patterns)
            result += decode(cipher, signals)
    
    return result

def main():
    print(f'Answer: {solve()}')

if __name__ == '__main__':
    main()