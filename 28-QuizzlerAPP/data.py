import requests

api_url = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}


class Data:

    def __init__(self):
        self.response = requests.get(api_url, params=parameters)
        self.response.raise_for_status()
        self.question_data = self.response.json()['results']

    def get_questions_list(self):
        return self.question_data

