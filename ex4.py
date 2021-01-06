import datetime
month_number = str(input('enter month_number : '))
DO = datetime.datetime.strptime(month_number, "%m")
month_name = DO.strftime('%B')
print(month_name)