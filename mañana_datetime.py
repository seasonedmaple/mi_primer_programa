import datetime

mañana = datetime.datetime.now() + datetime.timedelta(days=1)
mañana_medianoche = datetime.datetime(year=mañana.year, month=mañana.month, day=mañana.day)
hoy = datetime.datetime.now()
faltante_para_mañana = mañana_medianoche - hoy

print ("mañana es {}".format(mañana.strftime("%d del %m de %Y")))
print("Faltan {} horas para mañana".format(int(faltante_para_mañana.total_seconds()/3600)))