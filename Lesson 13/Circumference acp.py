import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
r = 7
print(f"The circumference of a circle with radius {r} is {calculate_circumference(r):.2f}")
