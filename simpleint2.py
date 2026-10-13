import sys

def simpInt(princpal, rate, time):
    return (princpal * rate * time) / 100

if __name__ == "__main__":
    p=int(sys.argv[1])
    r=int(sys.argv[2])
    t=int(sys.argv[3])
    print(simpInt(p, r, t))