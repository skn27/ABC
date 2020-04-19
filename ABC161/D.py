def num_of_lunlun(n):

def judge(mat):
    flag = 0 in mat[0][1:]
    for i in range(1, N):
        flag = flag|(0 in mat[i][i+1:])

    return flag

if __name__ == "__main__":
    N, X, Y = list(map(int, input().split()))
    d = [[0 for i in range(N)] for j in range(N)]
    for i in range(N-1):
        d[i][i+1] = 1

    d[X-1][Y-1] = 1
    for i in range(1, N):
        if judge(d):
            d = renew(d, i)
        else:
            break

    num = 0
    for j in range(1, N):
        for i in range(N):
            num += d[i][i+1:].count(j)
        print(num)
        num = 0
    
# %%
# N, X, Y = 7, 3, 7
# d = [[0 for i in range(N)] for j in range(N)]
# for i in range(N-1):
#     d[i][i+1] = 1

# d[X-1][Y-1] = 1

# for i in range(1, N):
#     if judge(d):
#         d = renew(d, i)
#     else:
#         max_d = i
#         break
# # %%
# num = 0
# max_d = 4
# for j in range(1, max_d+1):
#     for i in range(N):
#         num += d[i][i+1:].count(j)
#     print(num)
#     num = 0
    
# # %%
# d[0:1].count(1)
# # %%


# # %%
# judge(renew(d, 3))
# # %%
# # 更新
# for i in range(N):
#     for j in range(i, N):
#         if d[i][j] == 1:
#             if i-1 > 0:
#                 d[i-1][j] = 2
#             if i+1 < N:
#                 d[i+1][j] = 2
#             if j-1 > 0:
#                 d[i][j-1] = 2
#             if j+1 < N:
#                 d[i][j+1] = 2

# # %%
# for i in range(N):
#     for j in range(i, N):
#         if d[i][j] == 2:
#             print(i, j)
#             if (i-1 >= 0):
#                 if (d[i-1][j] == 0):
#                     d[i-1][j] = 3
#             if (i+1 < N):
#                 if (d[i+1][j] == 0):
#                     d[i+1][j] = 3
#             if (j-1 >= 0):
#                 if (d[i][j-1] == 0):
#                     d[i][j-1] = 3
#             if (j+1 < N):
#                 if (d[i][j+1] == 0):
#                     d[i][j+1] = 3


# # %%
# renew(d, 2)

# # %%
