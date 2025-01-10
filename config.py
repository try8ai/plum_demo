# If you bring your own data, please provide the path to the file in the input_output_file variable below.
input_output_file = 'data/input_output_pairs.json' 

try:
  from api_key import plum_api_key
except ImportError:
  print("Plum API Key not found! Please ensure you've provided your PLUM API key in the plum_api.py file.")
  exit()

ids_destination = 'ids.json'
training_data_destination = 'train.jsonl'

plum_url = 'https://beta.getplum.ai/v1'
auth_header = {'Authorization': plum_api_key}