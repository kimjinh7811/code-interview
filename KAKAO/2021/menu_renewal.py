from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for n in course:
        course_list = []
        for order in orders:
            candidate = combinations(sorted(order), n)
            course_list += candidate
        course_list = Counter(course_list)
        if course_list and max(course_list.values()) > 1:
            answer += [''.join(k) for k, v in course_list.items() if v == max(course_list.values())]

    return answer 

            
           

            
                

            
                

test_case = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]]
]

for t in test_case:
    print(solution(*t))