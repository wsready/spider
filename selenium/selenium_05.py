from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(options=options)

wait = WebDriverWait(browser, 10)

login_url = 'http://www.tcmip.cn/TCMIP/index.php/Home/Login/login.html'
data_url = 'http://www.tcmip.cn/TCMIP/index.php/Home/Index/yc_details.html?id={}'


def login(username, password):
    browser.get(login_url)
    wait.until(EC.presence_of_element_located((By.ID, 'username1')))
    username_tag = browser.find_element(By.ID, 'username1')
    password_tag = browser.find_element(By.ID, 'password1')
    username_tag.send_keys(username)
    password_tag.send_keys(password)
    login_btn = browser.find_element(By.XPATH, '//*[@id="signupForm1"]/div[3]/div/button')
    login_btn.click()
    wait.until(EC.url_changes(login_url))


def get_data(id):
    browser.get(data_url.format(id))
    name = browser.find_element(By.XPATH, '//*[@id="table"]/tbody/tr[1]/td[2]/div').text
    rows = browser.find_elements(By.XPATH, '//*[@id="comta"]/tbody/tr[position()>1]')
    data = []
    for row in rows:
        source = row.find_element(By.XPATH, './td[1]/a').text
        recipe = row.find_element(By.XPATH, './td[2]').text
        data.append([name, source, recipe])
        print(data)
    return data


def save_to_excel(data):
    df = pd.DataFrame(data, columns=['herb', 'Chemical Component', 'Candidate Target genes'])
    df.to_excel('中药数据库part2.xlsx', index=False)


if __name__ == '__main__':
    login('test4', '123456')
    data = []
    for id in range(1, 403):
        print(f"正在爬取第{id}个页面的数据...")
        data += get_data(id)
    save_to_excel(data)
    browser.quit()
