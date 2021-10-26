datas = input()

lst = []
N = 0

for data in datas:
  if data == '(':
    lst.append([tmp, N])
    N = 0
  elif data == ')': 
    multi, num = lst.pop()
    print(multi, num)
    N = multi*N + num-1
  else: # 만일 숫자라면
    N += 1
    tmp = int(data) # '('앞의 숫자를 저장할 변수

print(N)