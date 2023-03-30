import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.scrapethissite.com/pages/simple/'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

data = []

countries = soup.find_all('div', class_ = 'col-md-4 country')

for country in countries:
    name = country.find('h3').text.strip()
    capital = country.find('span', class_ = 'country-capital').text.strip()
    population = country.find('span', class_ = 'country-population').text.strip()
    area = country.find('span', class_ = 'country-area').text.strip()

    new_row = [name, capital, population, area]
    data.append(new_row)
        
df = pd.DataFrame(data, columns = ['Country', 'Capital', 'Population', 'Area'])
print(df)