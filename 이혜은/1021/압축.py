data = input()
stack = []
N = 0
tmp = ''

for s in data:
  if s.isdigit():
    N += 1
    tmp = s
  elif s == '(':
    stack.append((tmp, N-1))
    N = 0
    tmp = ''
  else:
    multi, preL = stack.pop()
    N = (int(multi)*N) + preL

print(N)