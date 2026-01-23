### -------------dates--------------------------------
""" Python es un lenguaje que ha crecido mucho
podemos trabajar como en backend, Ciencia de Datos, 
margen learg, inteligencia artificial"""

# datetime - Representa todas las operaciones, y todos los objetos relacionado xon fechas

from datetime import datetime 
# Obtener la fecha y hora actual
now = datetime.now()

def print_name(date):
    print(f"El año es: {date.year}")
    print(f"El mes es: {date.month}")
    print(f"El dia es: {date.day}")
    print(f"El hora es: {date.hour}")
    print(f"Minutos es: {date.minute}")
    print(f"Segundos es: {date.second}")
    print(f"Timestamp: {date.timestamp()}")

print_name(now)
print()
print(f"{now.year}/{now.month}/{now.day}")
print()
print(f"{now.hour} horas : {now.minute} minutos {now.second} segundos")
print()

year_2026 = datetime(2026, 1, 1, 00, 12)
print(year_2026)
print()

from datetime import time

current_time = time(20)
print(current_time)
print()

from datetime import date
current_date = date(2026, 11, 24)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print()
cur = date(current_date.year, current_date.month + 1, current_date.day)
print(cur.month)

print()
currin = date.today()
print(currin)
print()

dif = year_2026 - now
print(dif)
diff = year_2026.date() - current_date
print(diff)
print()
#funtion timedelta opera con varias fechas
from datetime import timedelta 

init_delta = timedelta(200, 100, 100, weeks = 10)
end_delta = timedelta(300, 100, 100, weeks= 13)
print(init_delta - end_delta)
print(init_delta / end_delta)

