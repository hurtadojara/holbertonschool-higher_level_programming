#!/usr/bin/python3
'''module load_from_json_file'''


def load_from_json_file(filename):
    '''
    function load_from_json_file
    '''
    import json
    with open(filename, encoding="UTF-8") as file:
        return json.load(file)
