from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
link = BeautifulSoup(r.text, 'html.parser')
title = link.find_all('div', attrs={'class': 'entry-content'})[0]
# table = title.find_all('table')  #, xpath= '//*[@id="post-29587"]/div/div/table[1]')
header= ['Nr. crt', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03']
# print(table[0])
dataset = []
for tr_index in title.find_all('table'):
    for td_index in tr_index.find_all('tr'):
        td_list = []
        for index, td_value in enumerate(td_index.find_all('td')):
            if index < 3:
                td_list.append(td_value.get_text().strip().replace(',', '.') if td_value.get_text().strip() != '' else '')
        dataset.append(td_list)
print(dataset)
