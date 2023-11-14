num_pol, num_vr = map(int, input().split())
set_pol = set()
set_vr = set()
for i in range(num_pol):
    set_pol.add(input())
for i in range(num_vr):
    set_vr.add(input())
if len(set_vr & set_pol) % 2 == 0:
    if len(set_pol) > len(set_vr):
        print('YES')
    else:
        print('NO')
else:
    if len(set_pol) >= len(set_vr):
        print('YES')
    else:
        print('NO')
