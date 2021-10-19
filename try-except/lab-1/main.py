from pprint import pprint


class Client:
    def __init__(self, name, doc_number, job):
        self.name = name
        self.doc_number = doc_number
        self.job = job


client = Client('Jhon', '321', 'dev')
pprint(client.__dict__, width=40)

# Raise AttributeError
# print(client.age)
