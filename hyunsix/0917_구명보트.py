def solution(people, limit):
    answer = 0
    # 우선 정렬하고
    people.sort()
    rescue_people = []
    # 가장 가벼운 친구와 가장 무거운 친구부터 짝지어주기
    left = 0
    right = len(people) - 1
    while left < right:
        # 짝지어질 수 있다면!
        if people[left] + people[right] <= limit:
            # 함께 탑승
            rescue_people.append(left)
            rescue_people.append(right)
            # 다음 덜 가벼운 친구, 다음 덜 무거운 친구로 인덱스 한 칸씩 모으기
            left += 1
            right -= 1
            # 카운팅
            answer += 1

        # 초과한다면!
        else:
            # 무거운 친구만 탑승
            rescue_people.append(right)
            right -= 1
            answer += 1

    # solo가 0 초과면 짝지어지지 못한 친구들이 남아있다는 뜻이므로씩 추가해주면 됨!
    solo = len(people) - len(rescue_people)
    answer += solo

    return answer