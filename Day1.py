# WPA Accepting the challenge from  Jagriti Srivastava in Different Methods ways.

# accepting challenge using class and Objects
class Hello_World:
    def __init__(self):
        self.challenge = "\nHello World! I have acept the 100 days coding challenge."
    
    @staticmethod
    def Day1_challenge():
        print(Hello_World().challenge )

# Direct Print message of accepting challenge
print("\nHello World! I have acept the 100 days coding challenge.")

# Veriable Assignment for accepting challenge
challenge  = "\nHello World! I have acept the 100 days coding challenge."
print(challenge)

# String formating for accepting challenge
print(f"{challenge}")

# Accepting challenge with Class and Object
Hello_World.Day1_challenge()
print("\nThank you\n")
