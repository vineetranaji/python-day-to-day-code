# Function to calculate the greatest common divisor (GCD) of two numbers using recursion
def compute_gcd(a, b):
    """Calculate the greatest common divisor (GCD) of two numbers using recursion."""
    # Base case: if b is zero, return a
    if b == 0:
        return a
    # Recursive case: call compute_gcd with b and the remainder of a divided by b
    else:
        return compute_gcd(b, a % b)

# Function to calculate the least common multiple (LCM) of two numbers
def compute_lcm(x, y):
    """Calculate the least common multiple (LCM) of two numbers."""
    # LCM is calculated using the formula: (x * y) // GCD(x, y)
    return x * y // compute_gcd(x, y)

# Example usage of the functions
# Define two numbers
num1 = 12
num2 = 18

# Calculate and print the LCM of the two numbers
print(f"The LCM of {num1} and {num2} is {compute_lcm(num1, num2)}")