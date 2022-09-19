import os
import yaml

SETTINGS = dict()

with open(f"{os.path.dirname(os.path.realpath(__file__))}/config.yaml", 'r', encoding='utf-8') as f:
    SETTINGS = yaml.load(f, Loader=yaml.FullLoader)
