#251 Write a function called show_stars(rows). If rows is 5, it should print the following:
#*
#**
#***
#****
#*****

i = ''
def show_stars(rows):
    global i
    for i in range(rows+1):
        print(i*'*')
    return ''

rows = int(input('Rows: '))
print(show_stars(rows))