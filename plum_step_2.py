from plum_config import plum_url, auth_header, input_output_file

import requests
import json

# Step 2: Generate metric definitions based on your system prompt
with open(input_output_file, 'r') as f:
    system_prompt = json.load(f)['system_prompt']

with open('ids.json', 'r') as f:
    ids = json.load(f)

response = requests.post(
    f'{plum_url}/questions',
    json={'system_prompt': system_prompt},
    headers=auth_header
    )
print(response.text)

ids['metrics_id'] = response.json()['metrics_id']
with open('ids.json', 'w') as f:
    json.dump(ids, f)