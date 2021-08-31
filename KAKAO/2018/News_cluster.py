from collections import Counter

def solution(str1, str2):
    answer = 0
    str1_set = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_set = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    inter_size = sum( (Counter(str1_set) & Counter(str2_set)).values() )
    union_size = sum( (Counter(str1_set) | Counter(str2_set)).values() )

    
    if union_size == 0:
        return 1 * 65536

    answer = int((inter_size / union_size) * 65536)
    
    return answer


test_case = [
    ['FRANCE', 'french'],
    ['handshake', 'shake hands'],
    ['aa1+aa2', 'AAAA12'],
    ['E=M*C^2', 'e=m*c^2']
]

for t in test_case:
    print(solution(*t))