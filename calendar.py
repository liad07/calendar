import calendar as cal

x = (int)(input('enter year\n'))
for i in range(1, 13):
    print(cal.month(x, i))
