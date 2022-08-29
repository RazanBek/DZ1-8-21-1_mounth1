batken = float(input("Температура Баткенской области на сегодня: "))
djalal_abad = float(input("Температура Джалал-Абадской области на сегодня: "))
issik_kul = float(input("Температура Иссык-Кульской области на сегодня: "))
narin = float(input("Температура Нарынской области на сегодня: "))
osh = float(input("Температура Ошской области на сегодня: "))
talas = float(input("Температура Таласской области на сегодня: "))
chuy = float(input("Температура Чуйской области на сегодня: "))

sum_of_weather = batken + djalal_abad + issik_kul + narin + osh + talas + chuy

average_weather = sum_of_weather/7

rounded = '%.1f' % average_weather

print("средний показатель температуры воздуха по КР на сегодня:", rounded, '°C')
