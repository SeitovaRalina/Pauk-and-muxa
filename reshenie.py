import math
def result(x, y):
    return math.sqrt(x**2 + y**2)
for i in range(1, 21):
    number = "%02d" % (i,)
    f = open(f'input_s1_{number}.txt')
    a, b, c = map(int, f.readline().split())
    sx, sy, sz = map(int, f.readline().split())  # паук
    fx, fy, fz = map(int, f.readline().split())  # муха
    res = 0
    r = []
    if abs(fx - sx) == a or abs(fy - sy) == b or abs(fz - sz) == c:
        # противоположные стены
        if abs(fx - sx) == a:
            r.append(result(a + 2 * b - (fy + sy), fz - sz))
            r.append(result(a + fy + sy, fz - sz))
            r.append(result(a + 2 * c - (fz + sz), fy - sy))
            r.append(result(a + fz + sz, fy - sy))
        if abs(fy - sy) == b:
            r.append(result(b + 2 * a - (fx + sx), fz - sz))
            r.append(result(b + fx + sx, fz - sz))
            r.append(result(b + 2 * c - (fz + sz), fx - sx))
            r.append(result(b + fz + sz, fx - sx))
        if abs(fz - sz) == c:
            r.append(result(c + 2 * a - (fx + sx), fy - sy))
            r.append(result(c + fx + sx, fy - sy))
            r.append(result(c + 2 * b - (fy + sy), fx - sx))
            r.append(result(c + fy + sy, fx - sx))
        res = min(r)
    else:
        # смежные стены и на одной стене
        if fx not in [0, a] and sx not in [0, a] or abs(fy - sy) == 0:
            res = result(abs(sz - fz) + abs(sy - fy), fx - sx)
        if fy not in [0, b] and sy not in [0, b] or abs(fz - sz) == 0:
            res = result(abs(fx - sx) + abs(fz - sz), fy - sy)
        if fz not in [0, c] and sz not in [0, c] or abs(fx - sx) == 0:
            res = result(abs(fx - sx) + abs(fy - sy), fz - sz)
    print(i, '%.3f' % res, open(f'output_s1_{number}.txt').readline())