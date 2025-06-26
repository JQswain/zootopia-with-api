import data_fetcher

def serialize_animals(animal_item):
    """Serialises the data into the format required from the animals_template.html,
    for use of adding it to the animals.html file"""
    output = ''
    name = animal_item["name"]
    diet = animal_item["characteristics"]["diet"]
    try:
        location = animal_item["locations"][0]
    except IndexError:
        location = ''
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

def generate_html(animals_data, user_animal):
    """Generates a new html file with the data collected, and a user, inputted animal,
    if there are errors it will print that onto the animals.html"""
    output = ''
    if animals_data == []:
        output += f'<h2 style="color: darkblue">Unfortunately, <em style="color:red">{user_animal}</em> was not found.</h2>'
    for animal in animals_data:
        output += serialize_animals(animal)

    with open("animals_template.html", "r") as template:
            template = template.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as animals_html:
        animals_html.write(template)

def main():
    user_animal = input("Enter the name of an animal: ")
    animals_data = data_fetcher.get_data_with_api_key(user_animal)
    generate_html(animals_data, user_animal)
    print(f"Website was successfully generated to the file animals.html")



if __name__ == "__main__":
    main()