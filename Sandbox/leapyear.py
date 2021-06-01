
def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# -----------------------------------------------------------------

year = int(input('Give a year: '))

print(year, is_leap_year(year))
