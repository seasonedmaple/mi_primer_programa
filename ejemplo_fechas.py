import datetime

year = int (input("Dime el año: "))
month = int (input("Dime el mes: "))
day = int (input("Dime el dia: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()

print("faltan {} dias y {} horas".format(time_remaining.days,time_remaining.seconds / 3600))