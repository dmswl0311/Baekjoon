k, r, n = map(str, input().split())
array = [str(input().strip()) for _ in range(int(n))]

kx = int(k[1])
ky = int(ord(k[0])-64)
rx = int(r[1])
ry = int(ord(r[0])-64)

d = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

next_kx = kx
next_ky = ky
next_ry = ry
next_rx = rx

for s in array:
    if s == 'T':
        next_kx = kx+d[0][0]
        next_ky = ky+d[0][1]
    elif s == 'RT':
        next_kx = kx+d[1][0]
        next_ky = ky+d[1][1]
    elif s == 'R':
        next_kx = kx+d[2][0]
        next_ky = ky+d[2][1]
    elif s == 'RB':
        next_kx = kx+d[3][0]
        next_ky = ky+d[3][1]
    elif s == 'B':
        next_kx = kx+d[4][0]
        next_ky = ky+d[4][1]
    elif s == 'LB':
        next_kx = kx+d[5][0]
        next_ky = ky+d[5][1]
    elif s == 'L':
        next_kx = kx+d[6][0]
        next_ky = ky+d[6][1]
    elif s == 'LT':
        next_kx = kx+d[7][0]
        next_ky = ky+d[7][1]
    if next_kx > 8 or next_kx < 1 or next_ky > 8 or next_ky < 1:
        next_kx = kx
        next_ky = ky
        continue
    if next_kx == rx and next_ky == ry:
        next_rx = rx+(next_kx-kx)
        next_ry = ry+(next_ky-ky)
        if next_rx > 8 or next_rx < 1 or next_ry > 8 or next_ry < 1:
            next_rx = rx
            next_ry = ry
        rx = next_rx
        ry = next_ry

    kx = next_kx
    ky = next_ky

king = chr(next_ky+64)+str(next_kx)

print(king)

rock = chr(next_ry+64)+str(next_rx)

print(rock)
