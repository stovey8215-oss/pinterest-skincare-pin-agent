# Pinterest Pin Generation System for Skincare Products

import random
import json

# List of 15 Amazon skincare products
products = [
    {"name": "Hydrating Face Cream", "image_url": "https://example.com/image1.jpg", "description": "A hydrating cream for glowing skin.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD123?tag=l76827-20"},
    {"name": "Moisturizing Lotion", "image_url": "https://example.com/image2.jpg", "description": "Lightweight lotion for everyday use.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD124?tag=l76827-20"},
    {"name": "Anti-Aging Serum", "image_url": "https://example.com/image3.jpg", "description": "Serum that reduces signs of aging.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD125?tag=l76827-20"},
    {"name": "Sunscreen SPF 50", "image_url": "https://example.com/image4.jpg", "description": "Broad spectrum sunscreen protection.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD126?tag=l76827-20"},
    {"name": "Gentle Cleanser", "image_url": "https://example.com/image5.jpg", "description": "Cleansing gel for sensitive skin.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD127?tag=l76827-20"},
    {"name": "Exfoliating Scrub", "image_url": "https://example.com/image6.jpg", "description": "Scrub that removes dead skin cells.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD128?tag=l76827-20"},
    {"name": "Hydrating Face Mask", "image_url": "https://example.com/image7.jpg", "description": "Mask for deep hydration.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD129?tag=l76827-20"},
    {"name": "Brightening Night Cream", "image_url": "https://example.com/image8.jpg", "description": "Night cream that brightens skin overnight.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD130?tag=l76827-20"},
    {"name": "Renewing Eye Cream", "image_url": "https://example.com/image9.jpg", "description": "Eye cream that reduces dark circles.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD131?tag=l76827-20"},
    {"name": "Clay Face Mask", "image_url": "https://example.com/image10.jpg", "description": "Detoxifying clay mask for oily skin.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD132?tag=l76827-20"},
    {"name": "Lip Balm", "image_url": "https://example.com/image11.jpg", "description": "Nourishing lip balm for chapped lips.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD133?tag=l76827-20"},
    {"name": "Vitamin C Serum", "image_url": "https://example.com/image12.jpg", "description": "Serum that brightens and revitalizes.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD134?tag=l76827-20"},
    {"name": "Threading Hair Removal Cream", "image_url": "https://example.com/image13.jpg", "description": "Cream for painless hair removal.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD135?tag=l76827-20"},
    {"name": "Facial Oil", "image_url": "https://example.com/image14.jpg", "description": "Nourishing oil for dry skin.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD136?tag=l76827-20"},
    {"name": "Cooling Gel", "image_url": "https://example.com/image15.jpg", "description": "Soothing gel for after sun care.", "affiliate_link": "https://www.amazon.com/dp/B01ABCD137?tag=l76827-20"}
]

# Function to generate pin details

def generate_pins(products, affiliate_tag):
    pins = []
    for day in range(1, 31):  # 30 days
        for product in products:
            for variation in range(1, 4):  # 3 variations
                pin = {
                    "day": day,
                    "product_name": product["name"],
                    "image_url": product["image_url"],
                    "description": product["description"],
                    "affiliate_link": product["affiliate_link"].replace("l76827-20", affiliate_tag),
                    "variation": variation
                }
                pins.append(pin)
    return pins


# Generate the 450 pins
affiliate_tag = 'l76827-20'
generated_pins = generate_pins(products, affiliate_tag)

# Output the generated pins to a JSON file
with open('generated_pins.json', 'w') as f:
    json.dump(generated_pins, f, indent=4)

print(f"Generated {len(generated_pins)} pins successfully!")
