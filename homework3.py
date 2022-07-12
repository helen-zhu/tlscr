import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

# beautiful soup has an attribute called source to tell you which line it is

# pathlib is a library for paths
# takes os.path + other libraries and make one module

# Explain servers, ports, and sockets
# Port 80 is for webservers (typical convention)
URL = "https://gvwilson.github.io/tlscr/species-index.html"

response = requests.get(URL)
print(f"status code: {response.status_code}")
print("text:")
print(response.text)

# Question 1: Print all the species
text = BeautifulSoup(response.text, "html.parser")
species = text.find_all("a", attrs={"class": "species"})
species_list = []
for animal in species:
    species_list.append(animal.contents[0].text)
    print(animal.contents[0].text)

# Question 2: Get species from the links
components = urlparse(URL)
for animal in species:
    short_link = '/tlscr/' + animal['href']
    animal_url = urlunparse((
        components.scheme,
        components.netloc,
        short_link,
        "",
        "",
        ""))
    animal_response = requests.get(animal_url)
    # print(f"status code: {animal_response.status_code}")
    if animal_response.status_code == 200:
        animal_text = BeautifulSoup(animal_response.text, "html.parser")
        animal_species = animal_text.find_all("p", attrs={"class": "scientific"})
        for this_species in animal_species:
            print(this_species.contents[0].text)
