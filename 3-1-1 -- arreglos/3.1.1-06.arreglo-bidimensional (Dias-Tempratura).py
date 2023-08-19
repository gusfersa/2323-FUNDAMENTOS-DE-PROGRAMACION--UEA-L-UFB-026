daily_temperatures = [
    ['Lunes', 75.2],
    ['Martes', 78.6],
    ['Miércoles', 82.1],
    ['Jueves', 79.8],
    ['Viernes', 85],
    ['Sabado', 88.0],
    ['Domingo', 87.5]
]

for day in range(0, 7, 1):
    print(f'La temperatura el dia {daily_temperatures[day][0]} es: {daily_temperatures[day][1]}')