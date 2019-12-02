import math


n = int(input ("Input Number of  polygon Edges: "))

while n < 3:
    n= int(input("insert a value higher than two: "))

i = 0
x = []
y = []

while i < n:
    i = i + 1
    x.append(int(input(f"Input coordinate x{i}: ")))
    y.append(int(input(f"Input coordinate y{i}: ")))

b = 0
c = 0
j = 0
A = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy= 0
print (f"{'Point':>3} {'X':>5} {'Y':>7}")

for b in range(0,n):
    c = c + 1
    print (f"{c:>3} {x[b]:>9.2f} {y[b]:>7.2f}")
print ('-'*30)
while j < (n-1):

    A = 1/2 * ((x [j + 1] + x[j]) * (y[j + 1] - y[j])) + A
    Sx = -(1/6) * ((x [j + 1]) - x[j]) * (y[ j+ 1 ]**2+ y[j]*y[j+1] + y[j]**2) + Sx
    Sy = (1/6) * ((y [j + 1]) - y[j]) * (x[ j+ 1 ]**2+ x[j]*x[j+1] + x[j]**2) + Sy
    Ix = -(1/12) * ((x [j + 1]) - x[j]) * (y[ j+1 ]**3 + y[j+1]**2 * y[j] + y[j+1]* y[j]**2 + y[j]**3) + Ix
    Iy = 1/12 * (y[j+1]-y[j]) * (x[ j+1 ]**3 + x[j+1]**2 * x[j] + x[j+1]* x[j]**2 + x[j]**3) + Iy
    Ixy = -(1/24) * (y[j+1] - y[j]) * ((y[j+1]*((3*x[j+1]**2)+ (2*x[j+1]*x[j]) + x[j]**2)) + y[j]*((3*x[j]**2)+(2*x[j+1]*x[j])+ x[j+1]**2)) + Ixy
    j = j+1

Xt = Sy / A
Yt = Sx / A
Ixt = Ix - Yt**2 * A
Iyt = Iy - Xt**2 * A
Ixyt = Ixy + (Xt * Yt * A)

print(f"Area of Polygon: {A:.2f}")
print(f"Sx: {Sx: .2f}")
print(f"Sy: {Sy: .2f}")
print(f"Ix: {Ix: .2f}")
print(f"Iy: {Iy:.2f}")
print(f"Ixy: {Ixy: .2f}")
print(f"Xt: {Xt: .2f}")
print(f"Yt: {Yt: .2f}")
print(f"Ixt: {Ixy: .2f}")
print(f"Iyt: {Iyt: .2f}")
print(f"Ixyt: {Ixyt: .2f}")
