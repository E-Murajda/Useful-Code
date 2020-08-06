try:
    date = int(input('Enter your date of birth - DDMMYYYY (30052020):'))
    date_str = str(date)
    date_s = [char for char in date_str]
    int_date = [int(i) for i in date_s]
    sum1 = sum(int_date)
    str_date2 = str(sum1)
    next_date = [i for i in str_date2]
    int_next_date = [int(i) for i in next_date]
    sum2 = sum(int_next_date)
    if sum2>9:
        sum2 = str(sum2)
        next_date2 = [i for i in sum2]
        int_next_date2 = [int(i) for i in next_date2]
        sum3 = sum(int_next_date2)
        print(sum3)
    else:
        print(sum2)
except ValueError:
    print('ValueError')