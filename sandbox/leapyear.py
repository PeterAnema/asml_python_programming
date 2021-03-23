response = input('Give a year: ')

year = int(response)

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(year, is_leap_year)