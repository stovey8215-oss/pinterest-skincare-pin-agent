import requests
import random
import time

class PinterestPinGenerator:
    def __init__(self, affiliate_tag):
        self.affiliate_tag = affiliate_tag

    def generate_pin(self, image_url, title, description, link):
        # Mock Pinterest API url
        pin_url = 'https://api.pinterest.com/v1/pins/'
        pin_data = {
            'image_url': image_url,
            'title': title,
            'description': description,
            'link': f'{link}?aff={self.affiliate_tag}'
        }

        response = requests.post(pin_url, json=pin_data)

        if response.status_code == 201:
            print('Pin created successfully!')
            return response.json()
        else:
            print('Failed to create pin: ', response.content)
            return None

    def batch_generate_pins(self, pin_info_list):
        for pin_info in pin_info_list:
            self.generate_pin(**pin_info)
            # Sleep to avoid hitting API limits
            time.sleep(2)

if __name__ == '__main__':
    affiliate_tag = 'l76827-20'
    pin_generator = PinterestPinGenerator(affiliate_tag)
    pin_info_list = [
        {'image_url': 'http://example.com/image1.jpg', 'title': 'Example Pin 1', 'description': 'Description for Pin 1', 'link': 'http://example.com/page1'},
        {'image_url': 'http://example.com/image2.jpg', 'title': 'Example Pin 2', 'description': 'Description for Pin 2', 'link': 'http://example.com/page2'},
        # Add more pin information as needed
    ]
    pin_generator.batch_generate_pins(pin_info_list)