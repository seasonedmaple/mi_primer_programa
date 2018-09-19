import datetime

print("ingresa la fecha de tu proximo cumpleaños")

year = int (input("Dime el año: "))
month = int (input("Dime el mes: "))
day = int (input("Dime el dia: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_to_wait = user_date - datetime.datetime.now()

weekday = user_date.weekday()

print("faltan {} dias y {} horas,  y el dia de la semana en que va a tocar es: {}".format(time_to_wait.days, time_to_wait.seconds / 3600, weekday ))