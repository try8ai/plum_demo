from plum_config import plum_url, auth_header, training_data_destination

import requests
import json

with open('ids.json', 'r') as f:
    synthetic_data_id = json.load(f)['synthetic_data_id']

synthetic_data = requests.get(
        f'{plum_url}/data/synthetic_openai/{synthetic_data_id}',
        headers=auth_header
    )
print(synthetic_data.text)

with open(training_data_destination, 'w') as f:
    f.write(synthetic_data.text)
