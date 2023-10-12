from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas

option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
header= ['Nr. crt', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03']
dictionar = {i: [] for i in header}
covid_table_len = driver.find_element(by=By.XPATH, value='//*[@id="post-29587"]/div/div/table[1]')
covid_table = covid_table_len.text.split('\n')
print(covid_table)
# //*[@id="post-29587"]/div/div/table[1]/tbody/tr[1]/td[3]/strong
# //*[@id="post-29587"]/div/div/table[1]/tbody/tr/td[3]
# for i,v in enumerate(covid_table):
#     if i == 0:
#         continue
#     element = v.split(" ")
#     dictionar['Nr. crt'].append(element[0])
#     dictionar['Judet'].append(element[1])
#     dictionar['01.03'].append(element[2])
# driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/')
# covid_table_len = driver.find_element(by=By.XPATH, value='//*[@id="post-29627"]/div/div/table[1]/tbody')
# covid_table = covid_table_len.text.split('\n')
# for i,v in enumerate(covid_table):
#     if i == 0:
#         continue
#     element = v.split(" ")
#     dictionar['02.03'].append(element[2])
# driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/')
# covid_table_len = driver.find_element(by=By.XPATH, value='//*[@id="post-29664"]/div/div/table[1]/tbody')
# covid_table = covid_table_len.text.split('\n')
# for i,v in enumerate(covid_table):
#     if i == 0:
#         continue
#     element = v.split(" ")
#     dictionar['03.03'].append(element[2])
# driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/')
# covid_table_len = driver.find_element(by=By.XPATH, value='//*[@id="post-25709"]/div/div/table[1]/tbody')
# covid_table = covid_table_len.text.split('\n')
# for i, v in enumerate(covid_table):
#     if i == 0:
#         continue
#     element = v.split(" ")
#     dictionar['04.03'].append(element[2])
# driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/')
# covid_table_len = driver.find_element(by=By.XPATH, value='//*[@id="post-29726"]/div/div/table[1]/tbody')
# covid_table = covid_table_len.text.split('\n')
# for i, v in enumerate(covid_table):
#     if i == 0:
#         continue
#     element = v.split(" ")
#     dictionar['05.03'].append(element[2])
# print(dictionar)
# df = pandas.DataFrame(dictionar)
# df.to_csv('tema_covid_table.csv', index = False)

