import requests

response1=requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':"lion"}})

print('Essay: ', response1.json()['output'])

response2=requests.post(
    "http://localhost:8000/joke/invoke",
    json={'input':{'topic':"frog"}})

print('\nJoke: ', response2.json()['output'])