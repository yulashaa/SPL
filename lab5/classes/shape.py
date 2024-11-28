import sys, time

w, h, out = 80, 24, sys.stdout
cube = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
s = 0.1
c = (1 - s**2)**0.5

ym = h/3
xm = 2*ym

edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

class Shape:
    def run():
        while True:
            cube = [(c*x + s*z, y, -s*x + c*z) for x, y, z in cube]
            proj = [(round(w/2+xm*x/(z+2)), round(h/2+ym*y/(z+2))) for x, y, z in cube]

            for edge in edges:
                start = proj[edge[0]]
                end = proj[edge[1]]
                for i in range(1, 9):
                    x = start[0] + i * (end[0] - start[0]) // 10
                    y = start[1] + i * (end[1] - start[1]) // 10
                    proj.append((x, y))

            out.write('\033[H' + '\n'.join(
                    ''.join(('*' if (x, y) in proj else ' ') for x in range(w))
                    for y in range(h)))
            out.flush()
            time.sleep(1/15.0)