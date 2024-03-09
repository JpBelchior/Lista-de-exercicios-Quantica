import math

def cartesian_to_polar(x, y):
    rho = math.sqrt(x**2 + y**2)  #Raio
    phi = math.atan2(y, x)         #Angulo entre eixos
    return (rho, phi)

# Testando a função
x = 3
y = 4
rho, phi = cartesian_to_polar(x, y)
print("Coordenadas cartesianas:", (x, y))
print("Coordenadas polares:", (rho, phi))