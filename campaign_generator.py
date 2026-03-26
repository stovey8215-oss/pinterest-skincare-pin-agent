import random
import datetime

# Constants
NUM_PINS = 450
DAYS = 30
AFFILIATE_TAG = 'l76827-20'
BASE_URL = 'https://www.pinterest.com/affiliate-link/'

# Sample data for titles and descriptions
titles = [
    'Skincare tip 1',
    'Skincare tip 2',
    'Skincare tip 3',
    'Skincare tip 4',
    'Skincare tip 5'
]

descriptions = [
    'Learn how to care for your skin the right way!',
    'Discover amazing skincare products just for you.',
    'Get the glow you want with our top tips!',
    'Skincare secrets that experts don’t tell you!',
    'The best skincare routine for your skin type!'
]

# Function to generate affiliate links
def generate_affiliate_link(pin_number):
    return f'{BASE_URL}?tag={AFFILIATE_TAG}&pin={pin_number}'

# Generate pins over the specified number of days
pins = []
start_date = datetime.datetime(2026, 3, 26)

for i in range(NUM_PINS):
    date = start_date + datetime.timedelta(days=i // (NUM_PINS // DAYS))
    title = random.choice(titles)
    description = random.choice(descriptions)
    affiliate_link = generate_affiliate_link(i + 1)
    pins.append({
        'date': date.strftime('%Y-%m-%d'),
        'title': title,
        'description': description,
        'affiliate_link': affiliate_link
    })

# Output the generated pins
for pin in pins:
    print(f"Date: {pin['date']} | Title: {pin['title']} | Description: {pin['description']} | Link: {pin['affiliate_link']}")