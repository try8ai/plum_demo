try:
  from plum_api import plum_api_key
except ImportError:
  print("Plum API Key not found! Please ensure you've provided your PLUM API key in the plum_api.py file.")
  exit()

input_output_file = 'input_output_pairs.json'
ids_destination = 'ids.json'
training_data_destination = 'train.jsonl'

plum_url = 'https://beta.getplum.ai/v1'
auth_header = {'Authorization': plum_api_key}