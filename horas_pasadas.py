import datetime
print("introduce cualquier fecha")

year = int (input("Dime el año: "))
month = int (input("Dime el mes: "))
day = int (input("Dime el dia: "))

user_date = datetime.datetime(year=year, month=month, day=day)


horas_pasadas = datetime.datetime.now() - user_date

print("Las horas que han pasado desde tu fecha es: {}".format(horas_pasadas.total_seconds() / 3600))