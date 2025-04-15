from datetime import date
def age(dob):
    today = date.today()
    years = dob.year - today.year
    if (today.month, today.day) < (dob.month, dob.day):
        years -=1
    return years
print('Age:', age(date(2000, 7, 1)))
