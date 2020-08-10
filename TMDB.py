import requests
import json

class Api:

    def __init__(self, api_key, base_url="https://api.themoviedb.org/3/", language="en"):
        self.api_key = api_key
        self.base_url = base_url
        self.language = language
    
    # Usage
    # api.url('movie/500')
    def url(self, segment, parameters = {}):
        parameters["api_key"] = self.api_key
        if not "lang" in parameters:
            parameters["lang"] = self.language
        query_string = "?"
        for key, value in parameters.items():
            query_string = query_string + key + "=" + value + "&"
        query_string = query_string.strip("&")
        if query_string == "?":
            query_string = ""
        return self.base_url + segment + query_string

    # Usage
    # api.request('movie/500')
    def request(self, segment, parameters = {}):
        url = self.url(segment, parameters)
        response = requests.get(url).text
        return json.loads(response)