def leap(year):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        return f'{year}' " is a leap year."
    else:
        return f'{year}' " isn't a leap year."

year = int(input('Year: '))
print(leap(year))