#238 - Celsius To Fahreinheit

C = float(input('Temperature in °C: '))
Coef = 9.0/5.0
F = (C*Coef) + 32
print(f'Temperature in Fahreinheit is {F}°F')