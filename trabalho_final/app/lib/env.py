import json

ENVFILE = 'env.json'

def get_env():
  with open(ENVFILE, 'r') as f:
    return json.load(f)
