import pd as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from tqdm import tqdm
data = []
# header = {
    #Сюда помещаем наш user-agent
    # 'User_Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'}
browser = Chrome('C:\\Users\\ADMIN\\Desktop\\chromedriver\\chromedriver_win32\\chromedriver.exe')
url = 'https://bus.gov.ru/registry'
browser.get(url)
# browser.find_element_by_tag_name('input').get_attribute('href')
# browser.find_element_by_xpath('/html/body/div[2]/ui-view/form/div[1]/div[1]/label/input')

input_tab = browser.find_element_by_xpath('/html/body/div[2]/ui-view/form/div[1]/div[1]/label/input')
input_tab.send_keys('онкологический диспансер')
# button = browser.find_element_by_xpath('//button[@type="submit"]')
# button.click()
input_tab.send_keys(Keys.ENTER)

sleep(10)
for p in range(10):

    soup = BeautifulSoup(browser.page_source, 'lxml')

    orgs = soup.findAll('div', class_='result')

    for org in orgs:
        try:
             name = org.find('a', class_='result__title').text.strip()
        except:
            name = org.find('div', class_='result__common_title').text.strip()

        link = 'https://bus.gov.ru/registry'+org.find('a', class_='result__button_registry').get('href')
        data.append([name, link])

    print(len(data))
    try:
        browser.find_element_by_class_name('pagination__next').click()
    except:
        break
    sleep(2)

header = ['name', 'link']
df = pd.DataFrame(data, columns=header)
df.to_csv('hospitals_data.csv', sep=':', encoding='utf8')


