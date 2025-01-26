# Python Day-to-Day Code

This project contains a collection of Python scripts that provide solutions to various common problems, including but not limited to mathematical calculations.

## Purpose

The purpose of this project is to offer reusable code snippets that can be used in day-to-day programming tasks. The scripts are designed to be simple and easy to understand, making them suitable for both beginners and experienced programmers.

## Usage

To use the scripts, simply import the desired function from the corresponding task file. For example:

```python
from tasks.lcm import compute_lcm

# Example usage
lcm_result = compute_lcm(4, 5)
```

## Tasks

### LCM Calculation

The `lcm.py` file contains functions to calculate the greatest common divisor (GCD) and the least common multiple (LCM) of two numbers using recursion.

### LCM Using Math Module

The `lcm using math module.py` file contains a function to calculate the LCM of two numbers using Python's built-in `math` module.

### Merge Alternately

The `merge alternately.py` file contains a function to merge two strings by adding letters in alternating order. If one string is longer than the other, the additional letters are appended to the end of the merged string.

```python
from tasks.merge_alternately import merge_alternately

# Example usage
merged_string = merge_alternately("abc", "pqr")
print(merged_string)  # Output: "apbqcr"
```