def temp():
    T = [-10, 1, 24, 32, -14, 9, -3, 21, 16, 12, 10, -7]
    total = sum(T)
    average = total/len(T)
    maxTemp = max(T)
    minTemp = min(T)
    print('Total: 'f'{total}' "°C")
    print('Average: 'f'{average}' "°C")
    print('Max Temp: 'f'{maxTemp}' "°C")
    print('Min Temp: 'f'{minTemp}' "°C")

temp()