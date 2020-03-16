

from datetime import datetime,date

flag = True

def calculate_age(born):
    
    today = date.today()

    temp = today.day
    today_day = today.month
    today_month = temp  

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
    date_of_birth = datetime.strptime(input(),"%Y/%m/%d")
    age = calculate_age(date_of_birth)
    print(age)
    
except ValueError:
    print("WRONG")




