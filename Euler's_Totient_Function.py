def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    """Calculate Euler's Totient Function for a given number n."""
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

# Get user input
number = int(input("Enter a number to find its Euler's Totient Function: "))

# Calculate Euler's Totient Function
result = euler_totient(number)

# Display the result
print(f"Euler's Totient Function φ({number}) = {result}")
