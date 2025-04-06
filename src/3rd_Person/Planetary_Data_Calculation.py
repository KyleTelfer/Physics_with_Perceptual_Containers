"""
Planetary Data Calculation Based on Visually Observed Data

This script calculates the volume, centripetal acceleration, relative mass, and relative density of planets in a single mass system (e.g., a star with orbiting planets) using only the following inputs:
- Radius of the planet (km)
- Orbital radius (million km)
- Orbital period (days)

The calculations are based on the assumption of a single dominant mass (e.g., the Sun) and multiple smaller masses (e.g., planets) orbiting it. The outputs are meaningful because they are calculated using relative values, which allow for comparisons between the properties of different volumes (planets) within the system.

Key Concepts:
1. **Single Mass System**: The system is dominated by a single large mass (e.g., the Sun), and the gravitational influence of smaller masses (e.g., planets) on each other is negligible.
2. **Relative Values**: By using relative orbital radii and periods, the script calculates properties such as centripetal acceleration, relative mass, and relative density without requiring absolute measurements of gravitational force or mass.
3. **Volume Interactions**: The script models the planets as volumes in space, allowing for the calculation of physical properties based on their observed dimensions and orbital characteristics.

Example Input:
- Radius: Radius of the planet in kilometers.
- Orbital Radius: Distance from the planet to the star in million kilometers.
- Orbital Period: Time taken for the planet to complete one orbit around the star in days.

Outputs:
- Volume: Volume of the planet in cubic meters.
- Centripetal Acceleration: Acceleration due to the planet's orbital motion around the star in m/s².
- Relative Mass: Mass of the planet relative to a reference planet (e.g., Earth).
- Relative Density: Density of the planet relative to a reference planet (e.g., Earth).
"""

import math

# Function to calculate volume of a sphere
def calculate_volume(radius):
    return (4/3) * math.pi * (radius * 1000)**3  # Convert radius from km to meters

# Function to calculate centripetal acceleration
def calculate_centripetal_acceleration(orbital_radius, orbital_period):
    orbital_radius_m = orbital_radius * 10**9  # Convert orbital radius from million km to meters
    orbital_period_s = orbital_period * 24 * 3600  # Convert orbital period from days to seconds
    v = (2 * math.pi * orbital_radius_m) / orbital_period_s  # Orbital velocity
    a_c = (v**2) / orbital_radius_m  # Centripetal acceleration
    return a_c

# Function to calculate relative mass
def calculate_relative_mass(centripetal_acceleration, orbital_radius, reference_mass, reference_orbital_radius):
    # Relative mass is proportional to (a_c * r²) / (a_c_ref * r_ref²)
    relative_mass = (centripetal_acceleration * orbital_radius**2) / (reference_mass * reference_orbital_radius**2)
    return relative_mass

# Function to calculate relative density
def calculate_relative_density(relative_mass, volume, reference_density, reference_volume):
    # Relative density is proportional to (relative_mass / volume) / (reference_density / reference_volume)
    relative_density = (relative_mass / volume) / (reference_density / reference_volume)
    return relative_density

# Main function to calculate properties for each planet
def calculate_planet_properties(planet_data, reference_planet):
    results = []
    for planet in planet_data:
        name = planet['name']
        radius = planet['radius']
        orbital_radius = planet['orbital_radius']
        orbital_period = planet['orbital_period']
        
        # Calculate volume
        volume = calculate_volume(radius)
        
        # Calculate centripetal acceleration
        a_c = calculate_centripetal_acceleration(orbital_radius, orbital_period)
        
        # Calculate relative mass (using reference planet as baseline)
        relative_mass = calculate_relative_mass(a_c, orbital_radius, reference_planet['centripetal_acceleration'], reference_planet['orbital_radius'])
        
        # Calculate relative density (using reference planet as baseline)
        relative_density = calculate_relative_density(relative_mass, volume, reference_planet['density'], reference_planet['volume'])
        
        # Append results
        results.append({
            'name': name,
            'volume': volume,
            'centripetal_acceleration': a_c,
            'relative_mass': relative_mass,
            'relative_density': relative_density
        })
    
    return results

# Input data for the star and planets
star_data = {
    'name': 'Sun',
    'radius': 696340,  # Radius of the Sun in km
    'orbital_radius': 0,  # The Sun doesn't orbit itself
    'orbital_period': 0  # The Sun doesn't orbit itself
}

# Example input for planets
planet_data = [
    {'name': 'Mercury', 'radius': 2439.7, 'orbital_radius': 57.91, 'orbital_period': 87.97},
    {'name': 'Venus', 'radius': 6051.8, 'orbital_radius': 108.2, 'orbital_period': 224.7},
    {'name': 'Earth', 'radius': 6371, 'orbital_radius': 149.6, 'orbital_period': 365.25},
    {'name': 'Mars', 'radius': 3389.5, 'orbital_radius': 227.9, 'orbital_period': 687},
    {'name': 'Jupiter', 'radius': 69911, 'orbital_radius': 778.5, 'orbital_period': 4333},
    {'name': 'Saturn', 'radius': 58232, 'orbital_radius': 1429, 'orbital_period': 10759},
    {'name': 'Uranus', 'radius': 25362, 'orbital_radius': 2871, 'orbital_period': 30687},
    {'name': 'Neptune', 'radius': 24622, 'orbital_radius': 4495, 'orbital_period': 60190}
]

# Reference planet (e.g., Earth)
reference_planet = {
    'name': 'Earth',
    'radius': 6371,  # Radius of Earth in km
    'orbital_radius': 149.6,  # Orbital radius of Earth in million km
    'orbital_period': 365.25,  # Orbital period of Earth in days
    'centripetal_acceleration': 0.00593,  # Centripetal acceleration of Earth in m/s² (example value)
    'density': 5514  # Density of Earth in kg/m³ (example value)
}

# Calculate properties for each planet
results = calculate_planet_properties(planet_data, reference_planet)

# Print results
for result in results:
    print(f"Planet: {result['name']}")
    print(f"  Volume: {result['volume']:.3e} m³")
    print(f"  Centripetal Acceleration: {result['centripetal_acceleration']:.3e} m/s²")
    print(f"  Relative Mass: {result['relative_mass']:.3f} (relative to Earth)")
    print(f"  Relative Density: {result['relative_density']:.3f} (relative to Earth)")
    print()