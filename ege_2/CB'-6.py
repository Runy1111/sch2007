w, h = map(int,  input().split())
n, m = map(int,  input().split())
k = int(input())
if n != 0:
    a = list(map(int,  input().split()))
else:
    a = []

if m != 0:
    b = list(map(int,  input().split()))
else:
    b = []
nl = [0] + a + [w]
ml = [0] + b + [h]
lands = []
nq = []
mq = []
for i in range(1, n+2):
    nq.append(nl[i]-nl[i-1])
for i in range(1, m+2):
    mq.append(ml[i]-ml[i-1])
for i in range(n+1):
    for j in range(m+1):
        lands.append(nq[i] * mq[j])
lands.sort()
print(lands[-k], lands[-1])

