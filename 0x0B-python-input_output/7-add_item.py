#!/usr/bin/python3
''' module 7 '''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = list(sys.argv[1:])

try:
    og_data = load_from_json_file('add_item.json')
except Exception:
    og_data = []

og_data.extend(arg_list)
save_to_json_file(og_data, 'add_item.json')
