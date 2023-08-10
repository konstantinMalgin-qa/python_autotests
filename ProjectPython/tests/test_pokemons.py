import requests
import pytest
host = 'https://api.pokemonbattle.me:9104'
token = '7f98023761a246726db06eecb07cf32b'


def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1866})
    assert response.status_code ==200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1866})
   
    
    assert response.json()['trainer_name'] == 'Kostya'
