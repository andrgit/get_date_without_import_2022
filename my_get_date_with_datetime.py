from datetime import datetime, timedelta


def get_date_with_imports(input_date, days):
    my_date = datetime.strptime(input_date, '%d.%m.%Y').date()
    end_date = my_date + timedelta(days=days)
    return f"{end_date:%d.%m.%Y}"


###Input mode
date = input("Input Date:")  # Format: 10.01.2008
number_of_days = int(input("Enter number of days:"))  # Format: 10
print(get_date_with_imports(date, number_of_days))

# print(get_date_with_imports("10.01.2008", 10))  # Example 1: output 20.01.2008
# print(get_date_with_imports("29.06.2020", 8))  # Example 1: output 07.07.2020
# #
# print(get_date_with_imports("25.02.2000", 8))  # output 04.03.2000  #Leap year
# print(get_date_with_imports("25.02.2001", 8))  # output 05.03.2001  #No Leap year
