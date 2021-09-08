def solution(play_time, adv_time, logs):
    
#     각 시작&&엔드 포인트를 기준으로 리스트를 생성할 껄...

    all_times = [0]*(100*60*60)
    
    hour, miniute, second = map(int, play_time.split(":"))
    ad_hour, ad_miniute, ad_second = map(int, adv_time.split(":"))
    
    video_times = hour*60*60+miniute*60+second
    ad_times = ad_hour*60*60+ad_miniute*60+ad_second
    
#     play_start_time = hour*60*60+miniute*60+second
#     play_end_time = hour*60*60+miniute*60+second+ad_hour*60*60+ad_miniute*60+ad_second
    
    for j in range(len(logs)):
        log = logs[j]
        
        start, end = map(str, log.split("-"))
        s_hour, s_miniute, s_second = map(int, start.split(":"))
        e_hour, e_miniute, e_second = map(int, end.split(":"))
        
        log_start_time = s_hour*60*60+s_miniute*60+s_second
        log_end_time = e_hour*60*60+e_miniute*60+e_second
        
        for i in range(log_start_time, log_end_time+1):
            all_times[i] += 1
    
    val = 0
    if video_times-ad_times:
        for i in range(ad_times):
            val += all_times[i]

    ans = 0
    tmp = 0
    
    for i in range(1, video_times-ad_times):
        val -= all_times[i-1]
        val += all_times[i+ad_times]
        if val > tmp:
            tmp = val
            ans = i

    print(ans)
    
    answer = ''
    hr_ans = str(ans//3600)
    if len(hr_ans) == 1:
        hr_ans = '0'+hr_ans
    ans = ans - (ans//3600)*3600
    min_ans = str(ans//60)
    if len(min_ans) == 1:
        min_ans = '0'+min_ans
    ans = ans - (ans//60)*60
    sec_ans = str(ans)
    if len(sec_ans) == 1:
        sec_ans = '0'+sec_ans
    answer = (hr_ans)+":"+(min_ans)+":"+(sec_ans)
    print(answer)
    return answer