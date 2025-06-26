import requests
API_KEY = "bMGJesFjI7d2IT0UKSI97A==EqOnGneKRwRohsjC"
ANIMALS_URL = "https://api.api-ninjas.com/v1/animals"


def get_data_with_api_key(user_animal):
    """Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:"""
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{ANIMALS_URL}?name={user_animal}", headers=headers)
    return response.json()

def main():
    pass

if __name__ == "__main__":
    main()