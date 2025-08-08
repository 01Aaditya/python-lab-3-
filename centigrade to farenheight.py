celsius = [36.5, 37.0, 39.2, 35.6, 38.7]

# Convert to Fahrenheit
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

# Filter temperatures above 100°F
above_100 = list(filter(lambda f: f > 100, fahrenheit))
print("Above 100°F:", above_100)
