from config import plum_url, auth_header

import requests
import json

with open('ids.json', 'r') as f:
    ids = json.load(f)

dataset_id = ids['dataset_id']
eval_results_id = ids['eval_results_id']
response = requests.post(
    f'{plum_url}/augment',
    json={'multiple': 2, 'seed_data_id': dataset_id, 'eval_results_id': eval_results_id},
    headers=auth_header
    )
print(response.text)
ids['synthetic_data_id'] = response.json()['synthetic_data_id']
with open('ids.json', 'w') as f:
    json.dump(ids, f)
