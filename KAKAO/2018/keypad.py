import math
def solution(numbers, hand):
    answer = ''
    left, right = (0,0), (0,2)
    pos_table = {1: (3, 0), 2: (3, 1), 3: (3, 2),
                 4: (2, 0), 5: (2, 1), 6: (2, 2),
                 7: (1, 0), 8: (1, 1), 9: (1, 2),  
                            0: (0, 1)}
    for num in numbers:
        if num in [1, 4, 7]:
            h = 'L'
        elif num in [3, 6, 9]:
            h = 'R'
        else:
            num_pos = pos_table[num]
            L_dist = abs(left[0] - num_pos[0]) + abs(left[1] - num_pos[1])
            R_dist = abs(right[0] - num_pos[0]) + abs(right[1] - num_pos[1])
            
            if L_dist < R_dist:
                h = 'L'
            elif L_dist > R_dist:
                h = 'R'
            elif L_dist == R_dist:
                h = 'L' if hand == 'left' else 'R'
                
        answer += h
        if h == 'L':
            left = pos_table[num]
        else:
            right = pos_table[num]
    
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))