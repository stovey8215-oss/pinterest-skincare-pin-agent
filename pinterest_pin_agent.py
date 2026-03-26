import requests
import json

class PinterestPinAgent:
    def __init__(self, affiliate_tag):
        self.affiliate_tag = affiliate_tag
        self.api_url = 'https://api.pinterest.com/v1/pins/'
        self.headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

    def create_pin(self, board, note, image_url, link):
        payload = {
            'board': board,
            'note': note,
            'image_url': image_url,
            'link': f'{link}?utm_source={self.affiliate_tag}'
        }

        response = requests.post(self.api_url, headers=self.headers, data=payload)
        if response.status_code == 201:
            print('Pin created successfully!')
            return response.json()
        else:
            print('Error creating pin:', response.json())
            return None

    def update_pin(self, pin_id, note=None, link=None):
        payload = {}
        if note:
            payload['note'] = note
        if link:
            payload['link'] = link

        response = requests.patch(f'{self.api_url}{pin_id}/', headers=self.headers, data=payload)
        if response.status_code == 200:
            print('Pin updated successfully!')
            return response.json()
        else:
            print('Error updating pin:', response.json())
            return None

    def delete_pin(self, pin_id):
        response = requests.delete(f'{self.api_url}{pin_id}/', headers=self.headers)
        if response.status_code == 204:
            print('Pin deleted successfully!')
            return True
        else:
            print('Error deleting pin:', response.json())
            return False

# Example usage:
if __name__ == '__main__':
    agent = PinterestPinAgent(affiliate_tag='l76827-20')
    agent.create_pin(board='My Board', note='Check this out!', image_url='http://example.com/image.jpg', link='http://example.com')