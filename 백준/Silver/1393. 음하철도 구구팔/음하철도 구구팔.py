from math import gcd
import sys
input = sys.stdin.readline
xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

x = xs - xe
y = ys - ye
GCD = gcd(dx, dy)
dx //= GCD
dy //= GCD

mx, my = x, y
Min = (mx**2 + my**2)**0.5
for i in range(201):
    x -= dx
    y -= dy
    temp = (x**2 + y**2)**0.5
    if Min > temp:
        Min = temp
        mx, my = x, y
        
print(xs-mx, ys-my)