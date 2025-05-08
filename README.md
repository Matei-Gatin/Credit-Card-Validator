# Credit Card Validator

A simple Python implementation of the Luhn algorithm to validate credit card numbers. This tool checks if a credit card number is potentially valid by applying the checksum formula used by financial institutions.

## Features
- Validates credit card numbers using the Luhn algorithm
- Simple and lightweight implementation
- Easy to integrate into other projects

## How It Works
The validator uses the Luhn algorithm (also known as the "modulus 10" algorithm) which:
1. Doubles every second digit from right to left
2. Adds the digits of the doubled numbers and the undoubled digits
3. Checks if the sum is divisible by 10

## Usage
```python
python demo.py
```

## License
MIT
