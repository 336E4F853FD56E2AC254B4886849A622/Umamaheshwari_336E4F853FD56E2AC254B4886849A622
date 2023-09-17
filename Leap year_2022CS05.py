year = int(input('Enter year : '))

if (year%4 == 0 and year%100 != 0):
    print(year, "is a leap year.")
else :
    print(year, "isyear not a leap year.")
