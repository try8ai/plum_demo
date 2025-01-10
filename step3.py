from config import plum_url, auth_header, input_output_file

import requests
import json

with open(input_output_file, 'r') as f:
    system_prompt = json.load(f)['system_prompt']

with open('ids.json', 'r') as f:
    ids = json.load(f)

dataset_id = ids['dataset_id']
metrics_id = ids['metrics_id']
response = requests.post(
    f'{plum_url}/evaluate',
    json={'prompt': system_prompt, 'seed_data_id': dataset_id, 'metrics_id': metrics_id},
    headers=auth_header
    )
print(response.text)
ids['eval_results_id'] = response.json()['eval_results_id']
with open('ids.json', 'w') as f:
    json.dump(ids, f)