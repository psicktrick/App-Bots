import requests

class Http:

    def __init__(self , api , data ,header):
        self.api = api
        self.data =  data
        self.header = header

    def post(self):
        return requests.post(self.api ,data = self.data ,headers = self.header)
