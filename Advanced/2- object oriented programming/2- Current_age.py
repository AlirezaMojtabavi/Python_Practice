from datetime import datetime,date

flag = True

def calculate_age(born):
    
    today = date.today()

    today_day = today.day
    today_month = today.month

    if today_month > born.month:
        return (today.year - born.year)

    elif today_month < born.month:
        return (today.year - born.year)-1

    elif (today_month == born.month) and (today_day > born.day):
        return (today.year - born.year)

    elif  (today_month == born.month) and (today_day < born.day):
        return (today.year - born.year)-1

    elif (today_month == born.month) and (today_day == born.day):
        return (today.year - born.year)

try:
    dateOfBirth = datetime.strptime(input(),"%Y/%m/%d")
    age = calculate_age(dateOfBirth)
    print(age)
    
except ValueError:
    print("WRONG")