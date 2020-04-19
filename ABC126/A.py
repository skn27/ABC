# -*- coding: utf-8 -*-
#%%
# 整数の入力
a = list(map(int, input().split()))
b = input()

#%%
# 出力
s = b[a[1]-1]
s_low = s.lower()
table = str.maketrans(s, s_low)3
print(b.translate(table))