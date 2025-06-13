def solution(babbling):
    answer = 0
    li = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in li:
            i = i.replace(j, " ")
        i = i.strip()
        if i == "":
            answer += 1
    return answer