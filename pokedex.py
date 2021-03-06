from urllib.request import urlopen
from bs4 import BeautifulSoup


def pokemon_name():
    pokemon = urlopen("https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon")
    html = BeautifulSoup(pokemon, 'html.parser')
    table = html.table.tbody
    return html

def format_dex(p_name):
    pokedex = urlopen(f"https://www.pokemon.com/uk/pokedex/{p_name}")
    html = BeautifulSoup(pokedex, 'html.parser')
    pokemon_name = html.find("div", class_="pokedex-pokemon-pagination-title").div.find(text=True)
    pokemon_information = html.find("p", class_="version-y").string
    print("\n"+"\t" + "\t" + pokemon_name.strip() + "\n")
    print(pokemon_information.strip()+"\n")

format_dex(input("Enter Pokèmon Name: "))
