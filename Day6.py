"""
Author :   Kusmakhar Pathak
Created:   1 August 2020
(c) Copyright by Kusmakhar Pathak.
"""
# program to calculate Kinetic Energy using class and object

"""
We know that the energy of an object when it is moving from the state of rest to motion is KE.
We have KE   = 1/2(mv2)
"""

class KE:
    def __init__(self, mass, velocity, *args):
        self.mass = mass
        self.velocity = velocity

    def calculate_ke(self):
        if self.mass < 0 and self.velocity < 0:
            return "Mass and velocity could not be negative"
        else:
            return (self.mass * (self.velocity ** 2)) / 2

if __name__ == "__main__":
    mass_of_obj = float(input("Enter Mass of an object:\t"))
    velocity_of_bj = float(input("Enter Velocity of an object:\t"))
    kinetic_energy = KE(mass_of_obj, velocity_of_bj)
    print(f"Mass\t\t= {mass_of_obj} Kg\nVelocity\t= {velocity_of_bj} m/s\nKinetic Energy = {kinetic_energy.calculate_ke()} Joules")
