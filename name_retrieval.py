import requests
from bs4 import BeautifulSoup
import string

def get_values_from_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        values = soup.find_all('a', {'class': 'new'})

        return [value.text for value in values]
    else:
        print(f"Failed to retrieve the page {url}. Error:", response.status_code)
        return []

alphabet_array = list(string.ascii_lowercase)
output_file = 'romanian_names.txt'

with open(output_file, 'w', encoding='utf-8') as file:
    for letter in alphabet_array:
        url = "https://ro.wikipedia.org/wiki/List%C4%83_de_nume_rom%C3%A2ne%C8%99ti_-_litera_" + letter.upper()
        values = get_values_from_wikipedia(url)
        for value in values:
            file.write(f"{value}\n")
        file.write('\n')

print(f"Headings have been saved to {output_file}.")
