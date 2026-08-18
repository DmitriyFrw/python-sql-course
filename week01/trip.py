# Дано
distance = 750
fuel_consumption = 7.4 / 100
prise_per_liter = 62.5
passengers = 3

# Сколько литров бензина потребуется на 750км
needed_fuel = fuel_consumption * distance
print (f"На 750 километров потребуется {round(needed_fuel, 1)} литров бензина")

#Сколько литров бензина потребуется на каждого пассажира
fuel_per_passenger = needed_fuel / passengers
print (f"На каждого пассажира потребуется {round(fuel_per_passenger, 1)} литров бензина")

#Цена за топливо на одного пассажира
price_per_passenger = fuel_per_passenger * prise_per_liter
print(f"Сумма потраченная на топливо за пассажира составит {round(price_per_passenger, 1)}₽")

# Цена за всю поездку
overall_price = needed_fuel * prise_per_liter
print (f"Сумма потраченная на весь бензин составит {round(overall_price, 1)}₽")