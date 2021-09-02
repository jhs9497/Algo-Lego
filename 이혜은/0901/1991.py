# 백준 1991번 문제
# 트리 기본 구조
# root == A

import sys

def preorder_traverse(alpha):

    global preorder_ans

    preorder_ans += alpha
    if not lst[ord(alpha)-65]:
        return
    if lst[ord(alpha)-65][0] != '.':
        preorder_traverse(lst[ord(alpha)-65][0])
    if lst[ord(alpha)-65][1] != '.':
        preorder_traverse(lst[ord(alpha)-65][1])

def inorder_traverse(alpha):

    global inorder_ans

    if lst[ord(alpha)-65][0] != '.':
        inorder_traverse(lst[ord(alpha)-65][0])
    inorder_ans += alpha
    if lst[ord(alpha)-65][1] != '.':
        inorder_traverse(lst[ord(alpha)-65][1])
    if not lst[ord(alpha)-65]:
        return

def postorder_traverse(alpha):
    global postorder_ans
    
    if lst[ord(alpha)-65][0] != '.':
        postorder_traverse(lst[ord(alpha)-65][0])
    if lst[ord(alpha)-65][1] != '.':
        postorder_traverse(lst[ord(alpha)-65][1])
    postorder_ans += alpha
    if not lst[ord(alpha)-65]:
        return


N = int(sys.stdin.readline())
lst = [[] for _ in range(ord('Z')-ord('A')+1)]

for _ in range(N):
    par, child1, child2 = map(str, sys.stdin.readline().split())
    lst[ord(par)-65].append(child1)
    lst[ord(par)-65].append(child2)


preorder_ans = ''
inorder_ans = ''
postorder_ans = ''

preorder_traverse('A')
inorder_traverse('A')
postorder_traverse('A')

print(preorder_ans)
print(inorder_ans)
print(postorder_ans)
