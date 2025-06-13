def solution(schedules, timelogs, startday):
    answer = 0
    for idx, schedule in enumerate(schedules):
        convert_minute = schedule % 100 + 10
        convert_hour = schedule // 100 + convert_minute // 60
        deadline = convert_hour * 100 + convert_minute % 60
        date = startday
        result = 0
        
        for timelog in timelogs[idx]:
            if 0 < date < 6 and timelog <= deadline:
                result += 1
            date = (date + 1) % 7
            
        if result == 5:
            answer += 1
            
    return answer