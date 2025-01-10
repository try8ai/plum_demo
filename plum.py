from config import input_output_file, plum_url, auth_header, training_data_destination

import requests
import json

with open(input_output_file, 'r') as f:
    data = json.load(f)
    system_prompt = data['system_prompt']

response = requests.post(
    f'{plum_url}/data/seed',
    json=data,
    headers=auth_header
    )
print(response.text)
dataset_id = response.json()['id']

response = requests.post(
    f'{plum_url}/questions',
    json={'system_prompt': system_prompt},
    headers=auth_header
    )
print(response.text)
metrics_id = response.json()['metrics_id']

response = requests.post(
    f'{plum_url}/evaluate',
    json={'prompt': system_prompt, 'seed_data_id': dataset_id, 'metrics_id': metrics_id},
    headers=auth_header
    )
print(response.text)
eval_results_id = response.json()['eval_results_id']

response = requests.post(
    f'{plum_url}/augment',
    json={'multiple': 2, 'seed_data_id': dataset_id, 'eval_results_id': eval_results_id},
    headers=auth_header
    )
print(response.text)
synthetic_data_id = response.json()['synthetic_data_id']

synthetic_data = requests.get(
        f'{plum_url}/data/synthetic_openai/{synthetic_data_id}',
        headers=auth_header
    )
print(synthetic_data.text)

with open(training_data_destination, 'w') as f:
    f.write(synthetic_data.text)