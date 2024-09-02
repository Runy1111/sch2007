def vis(y_1, y_x):
    num = y_x - y_1 - 1




a_0 = input()
a_1 = input()
d_v = ''
m_v = ''
y_1 = ''
d_x = ''
m_x = ''
y_x = ''
k = 0
for i in a_0:
    if i != '.':
        if k == 0:
            d_v += i
        elif k == 1:
            m_v += i
        else:
            y_1 += i
    else:
        k += 1
d_v, m_v, y_1 = int(d_v), int(m_v), int(y_1)
k = 0
for i in a_1:
    if i != '.':
        if k == 0:
            d_x += i
        elif k == 1:
            m_x += i
        else:
            y_x += i
    else:
        k += 1
d_x, m_x, y_x = int(d_x), int(m_x), int(y_x)

