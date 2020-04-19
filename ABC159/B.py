def judge(S):
    return S == S[::-1]

if __name__ == "__main__":
    S = input()
    print(judge(S) & judge(S[:len(S)//2]))