# Python Day-to-Day Code

This project contains a collection of Python scripts that provide solutions to common mathematical problems, specifically focusing on calculating the Least Common Multiple (LCM) and the Highest Common Factor (HCF) or Greatest Common Divisor (GCD).

## Purpose

The purpose of this project is to offer reusable code snippets that can be used in day-to-day programming tasks involving basic arithmetic operations. The scripts are designed to be simple and easy to understand, making them suitable for both beginners and experienced programmers.

## Files

- **tasks/lcm.py**: Contains a function to calculate the least common multiple of two or more numbers. This script includes input validation and error handling to ensure that the inputs are valid.

- **tasks/hcf.py**: Contains a function to calculate the highest common factor (HCF) or greatest common divisor (GCD) of two or more numbers. Similar to the LCM script, it includes input validation and error handling.

- **requirements.txt**: Lists the Python packages required for the project. You can install the necessary packages using pip.

## Usage

To use the scripts, simply import the desired function from the corresponding task file. For example:

```python
from tasks.lcm import calculate_lcm
from tasks.hcf import calculate_hcf

# Example usage
lcm_result = calculate_lcm(4, 5)
hcf_result = calculate_hcf(20, 30)
```

## Installation

To install the required packages, run the following command:

```
pip install -r requirements.txt
```

## Future Enhancements

This project is structured to allow for easy addition of more task files in the `tasks` directory. Feel free to contribute by adding new functionalities or improving existing ones.