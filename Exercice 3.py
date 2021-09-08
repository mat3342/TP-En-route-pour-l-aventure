temp_c = float(input('Choisir une température en degré'))

def deg_far(x):
    far = (x * 1.8) + 32
    return far

temp_f = deg_far(temp_c)

print('La température en degré fareneight est de', float(temp_f), '°F')
