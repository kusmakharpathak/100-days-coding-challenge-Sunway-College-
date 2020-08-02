"""
Author :   Kusmakhar Pathak
Created:   2 August 2020
(c) Copyright by Kusmakhar Pathak.
"""
# program to calculate Potential Energy using class and object

"""We know that the energy possessed by a body by virtue of its position relative to others, stresses within itself, 
electric charge, and other factors. We have PE   = mgh m = mass in kg g = acceleration of gravity = 9.8 m/s**2 h = 
height in meter """

class PE:
    def __init__(self, m, h, *args):
        self.mass = m
        self.height = h
        self.acceleration_of_gravity = 9.8

    def calculate_pe(self):
        if self.mass < 0 and self.height < 0:
            return "Mass and velocity could not be negative"
        else:
            return self.mass*self.acceleration_of_gravity*self.height

if __name__ == "__main__":
    mass = float(input("Enter Mass in Kilogram:\t"))
    height = float(input("Enter Height in Meter:\t"))
    potential_energy = PE(mass, height)
    print(f"Mass\t\t= {mass} Kg\nHeight\t= {height} m\nPotential Energy = {potential_energy.calculate_pe()} Joules")
