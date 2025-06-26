import requests

API_KEY = "bMGJesFjI7d2IT0UKSI97A==EqOnGneKRwRohsjC"
ANIMALS_URL = "https://api.api-ninjas.com/v1/animals"

def get_data_with_api_key(API_KEY, ANIMALS_URL, user_animal):
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{ANIMALS_URL}?name={user_animal}", headers=headers)
    return response.json()


def serialize_animals(animal_item):
    output = ''
    name = animal_item["name"]
    diet = animal_item["characteristics"]["diet"]
    location = animal_item["locations"][0]
    try:
        animal_type = animal_item["characteristics"]["type"]
    except KeyError:
        animal_type = None

    output += '<li class="cards__item">'
    output += f'<div class="card__title">{name}</div>\n'
    output += f'<div class="card__text">\n'
    output += f'<ul>\n<li><strong>Diet:</strong> {diet}</li>\n'
    output += f'<li><strong>Location:</strong> {location}</li>\n'
    if animal_type is not None:
        output += f'<li><strong>Type:</strong> {animal_type}</li>\n'
    else:
        output += f""
    output += '</ul>\n</div>\n</li>\n'

    return output

def generate_html():
    animals_data = get_data_with_api_key(API_KEY, ANIMALS_URL, 'Fox')
    output = ''
    for animal in animals_data:
        output += serialize_animals(animal)

    with open("animals_template.html", "r") as template:
            template = template.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as animals_html:
        animals_html.write(template)

def main():
   generate_html()


if __name__ == "__main__":
    main()