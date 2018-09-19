import datetime

five_days_ago = datetime.datetime.now() - datetime.timedelta(days=5)

print("La fecha da hace 5 dias es: {} y su respectivo dia de la semana es: {}".format(five_days_ago, five_days_ago.weekday()))

