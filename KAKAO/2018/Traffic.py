from datetime import datetime

def solution(lines):

    time_lines = []

    for line in lines:
        _, end_time, lapse_time = line.split(' ')
        dt = datetime.strptime(end_time, '%H:%M:%S.%f')
        end_time = dt.hour * 3600 + dt.minute * 60 + dt.second + dt.microsecond * 1e-6
        lapse_time = float(lapse_time[:-1])
        start_time = round(end_time - lapse_time + 0.001, 3)
        
        time_lines.append((start_time, 1))
        time_lines.append((end_time, -1))

    time_lines.sort(key=lambda x: x[0])
    
    num_traffic = 0
    answer = 1
    
    for i, line1 in enumerate(time_lines):
        cur = num_traffic
        for line2 in time_lines[i:]:
            if line2[0] - line1[0] > 0.999:
                break
            if line2[1] > 0:
                cur += line2[1]
        answer = max(answer, cur)
        num_traffic += line1[1]
    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))