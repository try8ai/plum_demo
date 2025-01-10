from config import input_output_file, plum_url, auth_header

import requests
import json

with open(input_output_file, 'r') as f:
    data = json.load(f)

response = requests.post(
    f'{plum_url}/data/seed',
    json=data,
    headers=auth_header
    )
print(response.text)

with open('ids.json', 'w') as f:
    json.dump({'dataset_id': response.json()['id']}, f)