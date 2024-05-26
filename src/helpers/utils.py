import json

class Utils:
    def sanitize(self, value=''):
        if type(value) is str:
            return value.replace(' ', '_').lower()
        
        return ''

    def dict_to_json(self, value={}):
        if type(value) is dict:
            return json.dumps(value, indent=2)

        return ''