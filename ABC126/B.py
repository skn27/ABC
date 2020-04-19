def ismonth(a):
    return 0 < a < 13
# 入力の受け取り
s = input()

#前後2つに分ける
a, b = int(s[:2]), int(s[2:])
if ismonth(a) and ismonth(b):
    print('AMBIGUOUS')
elif ismonth(a):
    print('MMYY')
elif ismonth(b):
    print('YYMM')
else:
     print('NA')

