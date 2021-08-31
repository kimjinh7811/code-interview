def score_pow(score, record):
    if record == 'S':
        return score
    elif record == 'D':
        return score ** 2
    else:
        return score ** 3

def solution(dartResult):
    answer = 0
    each_result = []

    prev = None
    score = 0
  
    for i, ch in enumerate(dartResult):
        if ch.isdigit():
            score = score * 10 + int(ch)
        elif ch.isalpha():
            score = score_pow(int(score), ch)
            each_result.append(score)
            score = 0
        else:
            if ch == '*':
                each_result[-1] *= 2
                if len(each_result) > 1:
                    each_result[-2] *= 2
            else:
                each_result[-1] *= -1
    
    answer = sum(each_result)       
    return answer

test_case = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
for x in test_case:
    print(solution(x))