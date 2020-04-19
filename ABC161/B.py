if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    sorted_A = sorted(A, reverse=True)
    num_of_vote = sum(A)
    flag = True
    for i in range(M):
        if sorted_A[i]*4*M < num_of_vote:
            flag = False
            break

    if flag:
        print('Yes')
    else:
        print('No')

# %%
# N, M = 4, 1
# A = [5, 4, 2, 1]
# sorted_A = sorted(A, reverse=True)
# num_of_vote = sum(A)
# flag = True


# %%
sorted_A

# %%
