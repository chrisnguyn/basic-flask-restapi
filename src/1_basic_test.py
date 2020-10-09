"""
1. Start the Flask server in 1_basic.py
2. Test it by running this file
"""

import requests

base_url = 'http://127.0.0.1:5000/'
hello_get = requests.get(base_url + 'hello')
hello_post = requests.post(base_url + 'hello')

print(hello_get.json())
print(hello_post.json())
