import requests
from typing import Tuple

def dictionary(word: str) -> Tuple[str, str]:
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    data = requests.get(url).json()
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    synonyms = data[0]['meanings'][0]['definitions'][0]['synonyms']
    return (definition, synonyms)