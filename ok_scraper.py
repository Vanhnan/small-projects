import requests
from selenium.webdriver import Chrome
import time

driver = Chrome()
driver.get('https://ok.ru')
driver.find_element_by_css_selector("#field_email").send_keys("+99611111111")
driver.find_element_by_css_selector("#field_password").send_keys("password")
driver.find_element_by_css_selector("#anonymPageContent > div.anonym_login_w.clearfix.anonym_login_w_redesign > div.anonym_login.h-mod > div:nth-child(3) > form > div.form-actions > div.mt-5x > input").click()

driver.execute_script("window.open('https://ok.ru/profile/562038570725/photos');")
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)

links = []
els = driver.find_elements_by_class_name("photo-card_cnt")
for i in els:
    links.append(i.get_attribute("href"))

for i in range(len(links)):
    driver.get(links[i])
    img = driver.find_element_by_id("__plpcte_target")
    res = requests.get(img.get_attribute("src"))
    with open(r"C:\Users\v4h4\Desktop\photos\photo#%s.jpg"%(i),"wb") as f:
        for x in res.iter_content(100000):
            f.write(x)

