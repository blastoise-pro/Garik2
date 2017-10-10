import math

EARTH_FLUX = 754361889825524406
EARTH_RADIUS = 6371


def IST(mbol, r):
    print("mbol ist = ", mbol)
    sfinal = calculate_s(mbol, r)
    print("sfinal = ", sfinal)
    primera_relacion = division_squared(sfinal, EARTH_FLUX)
    print("primera relacion = ", primera_relacion)
    segunda_relacion = division_squared(r, EARTH_RADIUS)
    print("segunda relacion = ", segunda_relacion)
    radicand =  primera_relacion + segunda_relacion
    print("radicand = ", radicand)
    final = 1 - math.sqrt(radicand / 2)
    print("final = ", final)
    return final


def division_squared(x, y):
    xmenosy = x - y
    xmasy = x + y
    print("x menos y = ", xmenosy)
    print("x mas y = ", xmasy)
    return (xmenosy / xmasy) ** 2


def calculate_s(mbol, r):
    print("mbol s = ", mbol)
    surface_area = calculate_surface_area(r)
    print("surface area = ", surface_area)
    sfinal = calculate_L(mbol) / surface_area
    print("S = ", sfinal)
    return sfinal


def calculate_surface_area(r):
    return 4 * math.pi * (r ** 2)


def calculate_L(mbol):
    print("mbol l = ", mbol)
    lfinal = 10 ** ((mbol - 4.2)/-2.5)
    print("lfinal = ", lfinal)
    return lfinal


bolometric_magnitude = float(input("Por favor introduce la magnitud bolometrica: "))
exo_radius = 1.6 #float(input("Por favor introduce el radio del exoplaneta: "))
print(bolometric_magnitude)
print(exo_radius)
print(IST(bolometric_magnitude, exo_radius * 69911) * 100)
