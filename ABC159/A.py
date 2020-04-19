
from math import factorial

def conb2(a):
    if a == 1:
        return 0
    else:
        return int(a*(a-1)/2)


if __name__ == "__main__":
    M, N = list(map(int, input().split()))
    print(conb2(M)+conb2(N))
