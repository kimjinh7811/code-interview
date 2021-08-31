def solution(n, t, m, timetable):
    answer = ''
    hour, minute = 9, 0
    timetable.sort(reverse=True)


    for bus in range(n):
        rider_list = []
        curTime = '%02d:%02d' % (hour, minute)              # 현재 시간

        while timetable and curTime >= timetable[-1]:       # 일찍 도착한 사람 태우기
            crew = timetable.pop()
            
            if bus == n-1 and len(rider_list) == m-1:       # 마지막 버스면 마지막 승객보다 1분 전
                ans_h, ans_m = crew.split(':')
                ans_h, ans_m = int(ans_h) + (int(ans_m) - 1) // 60,  (int(ans_m) - 1) % 60
                answer = '%02d:%02d' % (ans_h, ans_m)
                return answer

            rider_list.append(crew)                         

            if len(rider_list) == m:                        # 꽉찼으면 출발
                break
        
        if bus == n-1:                                      # 마지막 버스에 자리가 남았으면
            answer = '%02d:%02d' % (hour, minute)
            break

        hour, minute = hour + ((minute+t) // 60), (minute+t) % 60 
    return answer




test_case = [
    [1, 1, 5, ["08:00", "08:01", "08:01", "08:03"]],
    [2, 10, 2, ["09:10", "09:09", "08:00"]],
    [2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]],
    [1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]],
    [1, 1, 1, ["23:59"]],
    [10, 60, 45, ["23:59","23:59", "23:59", "23:59", 
                  "23:59", "23:59", "23:59", "23:59", 
                  "23:59", "23:59", "23:59", "23:59", 
                  "23:59", "23:59", "23:59", "23:59"]]
]

for n, t, m, table in test_case:
    print(solution(n, t, m, table))