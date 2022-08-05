from bs4 import BeautifulSoup
import requests
import pandas as pd


wiki_url = 'https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives'

table_id = 'votingmembers'


response = requests.get(wiki_url)

soup = BeautifulSoup(response.text, 'html.parser')


congress_table =soup.find('table', attrs={'id' : table_id})


df = pd.read_html(str(congress_table))


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 500)
pd.set_option('display.min_rows', 500)
pd.set_option('display.max_colwidth', 150)
pd.set_option('expand.frame_repr', True)

print(df)





