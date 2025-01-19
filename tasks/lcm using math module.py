import math

def compute_lcm(x, y):
    """Calculate the least common multiple (LCM) of two numbers."""
    return x * y // math.gcd(x, y)

# Example usage
num1 = 12
num2 = 18

print(f"The LCM of {num1} and {num2} is {compute_lcm(num1, num2)}")