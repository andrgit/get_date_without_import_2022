def get_date_without_imports(start, days):
    add_days = days
    days_of_months_no_leap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_of_months_leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    get_days, get_month, get_year = list(map(int, start.split('.')))
    # Leap year Check
    # If True, it's Leap Year
    if get_year % 4 == 0 and get_year % 100 != 0 or get_year % 400 == 0:
        days_of_month = days_of_months_leap_year
    else:
        days_of_month = days_of_months_no_leap

    if get_days + add_days < days_of_month[get_month]:  # IF days in input + add days < when days of months
        return f"{format(get_days + days, '02')}.{format(get_month, '02')}.{get_year}"
        # OR
        # return f"{str(get_days).zfill(2)}.{str(get_month).zfill(2)}.{get_year}"

    elif get_days + add_days > days_of_month[get_month]:
        days_1 = get_year * 365 + get_days + add_days
        for i in range(1, get_month):
            days_1 += days_of_month[i]
        years = days_1 // 365
        days = days_1 % 365
        month = 1
        while days > days_of_month[month]:
            days -= days_of_month[month]
            month += 1
        return f"{format(days, '02')}.{format(month, '02')}.{years}"
        # OR
        # return f"{str(days).zfill(2)}.{str(month).zfill(2)}.{years}"

# date = input("Input Date:") #Format: 10.01.2008
# number_of_days = int(input("Enter number of days:")) #Format: 10
# print(my_calendar_2022(date, number_of_days))

# print(my_calendar_2022("10.01.2008", 10))  # Example 1: output 20.01.2008
# print(my_calendar_2022("29.06.2020", 8))  # Example 1: output 07.07.2020

# print(get_date_without_imports("25.02.2000", 8))  # output 07.07.2020  #Leap year
# print(get_date_without_imports("25.02.2001", 8))  # output 07.07.2020  #No Leap year
