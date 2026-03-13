from math import pi

o1 = 1*pi
o2 = 7*pi
o3 = 10*pi

h = 10**-4

t = h
while True:
    if (o1*t) % 2*pi + (2/3*pi) - (o2*t) % 2*pi  < h:
        if (o2*t) % 2*pi + (2/3*pi) - (o3*t) % 2*pi < h:
            print(t)
            break
    t+=h
    print(t,end="\r")

print(o1*t, "\t", (o1*t) % 2*pi)
print(o2*t, "\t", (o2*t) % 2*pi)
print(o3*t, "\t", (o3*t) % 2*pi)
print(2*pi)
print(2/3*pi)