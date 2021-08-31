def solution(n, arr1, arr2):
    answer = []
    map_dict = {True: '#', False: ' '}
    for i, (p1, p2) in enumerate(zip(arr1, arr2)):
        temp = ''
        result = format((p1 | p2), 'b')
        result = result.zfill(n)

        for r1 in result:
            temp += map_dict[bool(int(r1))]
        answer.append(temp)

    return answer

a = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
print(a)