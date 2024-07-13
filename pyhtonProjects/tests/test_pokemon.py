import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='702b80f39d09f7eec9cf0da26a8384d2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4593'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
