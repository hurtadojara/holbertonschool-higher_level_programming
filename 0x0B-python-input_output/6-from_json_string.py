#!/usr/bin/python3
'''module from_json_string'''


def from_json_string(my_str):
    '''
    function from_json_string
    '''
    import json
    return json.loads(my_str)
