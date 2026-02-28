import numpy as np
import matplotlib.pyplot as plt
import argparse


def modulation(
    x0,y0,
    v0x,v0y,
    k,m,g,
    stepsize
):
    x = x0
    y = y0
    vx = v0x
    vy = v0y

    stepSize = stepsize

    xpoints = []
    ypoints = []

    t = 0
    while True:
        try:
            vx += (-k/m*vx**2)*stepSize
            vy += (-g+k/m*vy**2)*stepSize
        except OverflowError:
            break

        x += vx*stepSize
        y += vy*stepSize

        if y < 0:
            if abs(y) < abs(ypoints[-1]):
                xpoints.append(x)
                ypoints.append(y)
            break

        xpoints.append(x)
        ypoints.append(y)

        t += stepSize
    
    return (xpoints,ypoints)

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-k", type=float, default=0.1)
    parser.add_argument("-m", type=float, default=0.1)
    parser.add_argument("-g", type=float, default=9.82)
    parser.add_argument("-v0x", type=float, default=1)
    parser.add_argument("-v0y", type=float, default=0)
    

    parser.add_argument("--markdp",action="store_true")
    parser.add_argument("-stepsize", type=float, default=10**-3)
    
    args = parser.parse_args()

    k = float(args.k) # Luftmotstånd
    m = float(args.m)
    g = float(args.g)

    x0 = 0
    y0 = 2
    v0x = float(args.v0x)
    v0y = float(args.v0y)

    results = modulation(
        x0,y0,
        v0x,v0y,
        k,m,g,
        args.stepsize
    )
    plt.plot(results[0],results[1],label="variable input",marker="x" if args.markdp else "")
    plt.legend()

    results = modulation(
        x0,y0,
        parser.get_default("v0x"), parser.get_default("v0y"),
        parser.get_default("k"), parser.get_default("m"), parser.get_default("g"),
        args.stepsize
    )
    plt.plot(results[0],results[1],linestyle="dashed",label="default",marker="x" if args.markdp else "")
    plt.legend()

    plt.savefig("modulering/modulation")

main()
