
year = int(input('Enter a year:'))
month = int(input('Enter month:'))


def isYearLeap(year):  # checks if a year is a leap year
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31   # if Jan,Mar,May ... return 31
    if month == 2:  # if Feb - >
        if isYearLeap(year) == True:  # checks for leap
            return 29
        else:
            return 28
    else:
        return 30


print(daysInMonth(year, month))


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
print()
