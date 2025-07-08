import numpy as np
from numpy import random
import time
import math

luminosity = 0  # Global placeholder for luminosity (unused here)

# Class representing a star with its key physical and spectral properties
class Star:
    def __init__(self, name, mass, spectral_type, temperature, vector, luminosity_class, luminosity):
        self.name = name                  # Star identifier, e.g. "Star-1"
        self.mass = mass                  # Star mass in solar masses
        self.spectral_type = spectral_type  # Spectral classification based on temperature (O, B, A, F, G, K, M)
        self.temperature = temperature    # Surface temperature in Kelvin
        self.vector = vector              # Radial velocity component (direction & speed relative to observer/planet)
        self.luminosity_class = luminosity_class  # Luminosity class (main sequence, giant, etc.)
        self.luminosity = luminosity      # Luminosity in solar units

    # String representation to print star info clearly
    def __repr__(self):
        return f"<{self.name}: Mass={self.mass:.2f} Solar Masses, Temp={self.temperature:.0f} K, Type= {self.spectral_type}, Class= {self.luminosity_class}, Vector={self.vector:.2f}>"

# Class representing a planet with basic orbital and physical properties
class Planet:
    def __init__(self, name, mass, surface_temp, orbital_radius, orbital_period):
        self.name = name                  # Planet identifier, e.g. "Star-1 β"
        self.mass = mass                  # Planet mass in Earth masses
        self.surface_temp = surface_temp  # Equilibrium surface temperature in Celsius
        self.orbital_radius = orbital_radius  # Orbital radius in AU
        self.orbital_period = orbital_period  # Orbital period in Earth years

    def __repr__(self):
        return f"<{self.name}: Mass={self.mass:.2f} Earth Masses, Surface temperature={self.surface_temp:.0f}C, Orbital radius={self.orbital_radius:.2f} AU, Orbital period={self.orbital_period:.2f} years."

# Sample stellar mass according to the Salpeter Initial Mass Function (IMF)
def salpeter_IMF(m_min=0.08, m_max=20.0, alpha=0.95):
    y = random.uniform(0, 1)           # Random uniform sample [0,1]
    a = 1 - alpha                      # Used for inverse transform sampling
    # Return mass following a power-law IMF distribution via inverse transform sampling
    return ((y * (m_max**a - m_min**a)) + m_min**a) ** (1 / a)

# Generate a star with physical properties based on sampled mass
def star_generation(name):
    # Constants
    temp_sun = 5778                   # Sun’s effective temperature in Kelvin
    radius_sun = 6.957e8              # Sun’s radius in meters
    stefan_boltzmann = 5.670374419e-8 # Stefan-Boltzmann constant (W·m⁻²·K⁻⁴)
    L_sun = 3.828e26                 # Solar luminosity in Watts

    mass = salpeter_IMF()  # Sample star mass

    # Approximate temperature scaling by mass:
    # Smaller stars scale differently from larger stars
    temperature = temp_sun * (mass ** 0.505) if mass < 1.0 else temp_sun * (mass ** 0.4)

    radius = radius_sun * (mass ** 0.8)  # Radius scaling with mass

    # Calculate luminosity using Stefan-Boltzmann law: L = σ * 4πR² * T⁴
    luminosity = stefan_boltzmann * 4 * np.pi * radius ** 2 * temperature ** 4
    luminosity /= L_sun  # Normalize to solar luminosity units

    vector = random.uniform(-1, 1)  # Random radial velocity component (direction & magnitude)

    # Classify star spectral type based on temperature thresholds
    if temperature > 30000:
        spectral_type = "O-class main sequence"
    elif temperature > 10000:
        spectral_type = "B-class main sequence"
    elif temperature > 7500:
        spectral_type = "A-class main sequence"
    elif temperature > 6000:
        spectral_type = "F-class main sequence"
    elif temperature > 5200:
        spectral_type = "G-class main sequence"
    elif temperature > 3700:
        spectral_type = "K-class main sequence"
    elif temperature <= 3700:
        spectral_type = "M-class main sequence"
    else:
        spectral_type = "Unknown"

    # Assign luminosity class based on luminosity and mass thresholds
    if luminosity > 1e6 and mass > 30:
        luminosity_class = "0 - Hypergiant"
    elif luminosity > 1e4 and mass > 10:
        luminosity_class = "I - Supergiant"
    elif 1e3 < luminosity <= 1e4 and 5 < mass <= 10:
        luminosity_class = "II - Bright giant"
    elif 100 < luminosity <= 1e3 and 1 < mass <= 5:
        luminosity_class = "III - Giant"
    elif 10 < luminosity <= 100 and 0.8 <= mass <= 1.5:
        luminosity_class = "IV - Subgiant"
    elif 0.01 <= luminosity <= 10 and 0.08 <= mass <= 20:
        luminosity_class = "V - Main sequence"
    elif luminosity < 0.01 and mass < 0.5:
        luminosity_class = "VI - Subdwarf"
    elif 1e-4 <= luminosity <= 1e-2 and 0.5 <= mass <= 1.4:
        luminosity_class = "D - White dwarf"
    else:
        luminosity_class = "Unknown"

    # Return constructed Star object
    return Star(name, mass, spectral_type, temperature, vector, luminosity_class, luminosity)

# Create a list of 3 stars with unique names
def create_stars():
    stars = []
    for i in range(3):
        star = star_generation(f"Star-{i+1}")
        stars.append(star)
    return stars

# Main launch function to generate stars and a planet, then print results
def launch():
    stars = create_stars()
    print("New system")
    for star in stars:
        print(star)

    hostStar = np.random.choice(stars)  # Randomly pick one star as the host star
    print(f"\nHost star is: {hostStar.name}. It is a {hostStar.spectral_type} star, {hostStar.luminosity_class} class.")

    planet = create_planet(hostStar)  # Generate a planet orbiting the host star
    print(planet)
    return stars, hostStar, planet

# Wrapper to generate a planet for the given host star
def create_planet(host_star):
    planet = planet_generation(host_star)
    return planet

# Calculate planetary surface temperature assuming blackbody equilibrium
def calculate_surface_temp(luminosity_watts, orbital_radius_AU, albedo=0.3):
    StefanBoltzmann = 5.670374419e-8  # Stefan-Boltzmann constant in W·m⁻²·K⁻⁴
    AU_in_meters = 1.496e11  # 1 AU in meters
    d = orbital_radius_AU * AU_in_meters  # Convert AU to meters

    # Planet equilibrium temperature formula assuming isotropic radiation and given albedo
    temp_K = ((1 - albedo) * luminosity_watts / (16 * math.pi * StefanBoltzmann * d ** 2)) ** 0.25
    temp_C = temp_K - 273.15  # Convert Kelvin to Celsius
    return temp_C

# Generate a planet orbiting the host star within habitable zone limits
def planet_generation(host_star):
    x = random.choice(['ɑ', 'β', 'γ'])  # Random Greek letter for planet designation
    name = f"{host_star.name} {x}"
    mass = random.uniform(0.5, 3)  # Planet mass in Earth masses

    # Approximate conservative habitable zone boundaries (in AU)
    inner_hz = (host_star.luminosity / 1.1) ** 0.5
    outer_hz = (host_star.luminosity / 0.53) ** 0.5

    # Choose orbital radius randomly within habitable zone
    orbital_radius = random.uniform(inner_hz, outer_hz)

    # Calculate orbital period in years using Kepler's Third Law
    orbital_period = math.sqrt(orbital_radius ** 3 / host_star.mass)

    # Convert luminosity from solar units to Watts for temperature calculation
    L_sun = 3.828e26
    luminosity = host_star.luminosity * L_sun

    surface_temp = calculate_surface_temp(luminosity, orbital_radius)

    # Return planet object with all properties
    return Planet(name, mass, surface_temp, orbital_radius, orbital_period)

# Run the launch function when script is executed directly
if __name__ == "__main__":
    stars = launch()
