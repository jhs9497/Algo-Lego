def solution(people, limit):
    answer = 0
    people.sort()
    rescue_people = []
    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            rescue_people.append(left)
            rescue_people.append(right)
            left += 1
            right -= 1
            answer += 1
        else:
            rescue_people.append(right)
            right -= 1
            answer += 1

    while len(rescue_people) < len(people):
        rescue_people.append('just count')
        answer += 1

    return answer