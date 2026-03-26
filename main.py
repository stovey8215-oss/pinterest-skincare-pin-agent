import json
import csv
import random

# Constants
TOTAL_PINS = 450  # Total number of pins to generate (30 days x 15 pins)
AFFILIATE_TAG = 'l76827-20'
DESIGN_VARIATIONS = 3

# Sample list of skincare products (in practice, this can be fetched from an API or other source)
SKINCARE_PRODUCTS = [
    {'name': 'Hydrating Facial Cream', 'url': 'https://www.amazon.com/dp/B000XXXXXX'},
    {'name': 'Anti-Aging Serum', 'url': 'https://www.amazon.com/dp/B000XXXXXX'},
    {'name': 'Brightening Face Mask', 'url': 'https://www.amazon.com/dp/B000XXXXXX'},
    # Add more products as needed
]

# Function to generate pin data
def generate_pins():
    pins = []
    for _ in range(TOTAL_PINS):
        product = random.choice(SKINCARE_PRODUCTS)
        for design in range(1, DESIGN_VARIATIONS + 1):
            pin = {
                'title': f"{product['name']} - Design {design},"
                'description': f"Check out this amazing product! {product['name']}.",
                'affiliate_url': f"{product['url']}?tag={AFFILIATE_TAG}",
                'design_variation': design,
            }
            pins.append(pin)
    return pins

# Generate pins
pins_data = generate_pins()

# Export to JSON format
with open('pins.json', 'w') as json_file:
    json.dump(pins_data, json_file, indent=4)

# Export to CSV format
with open('pins.csv', 'w', newline='') as csv_file:
    fieldnames = ['title', 'description', 'affiliate_url', 'design_variation']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for pin in pins_data:
        writer.writerow(pin)

print('Pins generated and exported to pins.json and pins.csv!')