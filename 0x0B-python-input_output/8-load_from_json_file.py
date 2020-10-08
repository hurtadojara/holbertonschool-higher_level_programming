#!/usr/bin/python3
import json
'''module load_from_json_file'''


def load_from_json_file(filename):
    '''
    function load_from_json_file
    '''
    with open(filename, encoding="UTF-8") as file:
        return json.load(file)
