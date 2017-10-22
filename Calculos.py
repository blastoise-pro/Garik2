import math

earth_radius = 6371000
boltzmann_constant = 1.36 * 10 ** -23
estrellas = {"O": float(33000), "B": float(10000), "A": float(75000), "F": float(6000), "G": float(5200), "K": float(3700)}
exoplanet_radius = float(input("Radi exoplaneta: ")) * 69911000
star_type = input("Tipus estrella: ").capitalize()
earth_flux = 7.54 * 10 ** 14
star_radius = float(input("Radi estrella: ")) * 695000000


def calculate_surface_area (r):
    return 4 * math.pi * r ** 2


def calculate_L (star_radius, star_type):
    return estrellas[star_type] ** 4 * 4 * math.pi * star_radius ** 2 * boltzmann_constant


def calculate_exoplanet_fluxe (exoradius, L):
    return L / calculate_exosurface(exoradius)


def calculate_exosurface(exoradius):
    return 4 * math.pi * exoradius ** 2


def calculate_IST (exoplanet_radius, star_radius):
    flux_exo = calculate_exoplanet_fluxe(exoplanet_radius, calculate_L(star_radius, star_type))
    return  math.sqrt(
        (((flux_exo - earth_flux)/(flux_exo + earth_flux)) ** 2) -
        (((exoplanet_radius - earth_radius)/(exoplanet_radius + earth_radius)) ** 2)) * 100


print("L'índex de similitud amb la Terra és ", str(calculate_IST(exoplanet_radius, star_radius)), "%")
