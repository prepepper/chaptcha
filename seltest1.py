from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe") 
url = "https://www.google.com" 
driver.get(url)

time.sleep(0.5) ## 0.5초

# search_box = driver.find_element_by_name('q')
search_box = driver.find_element_by_class_name('gLFyf')
search_box.send_keys("펭수")
# search_box.submit()

search_box.get_attribute("value")
search_box.send_keys("펭수22")

send_btn = driver.find_element_by_class_name('gNO89b')
# send_btn.send_keys(Keys.ENTER)
driver.execute_script("arguments[0].click();", send_btn)

# driver.implicitly_wait(time_to_wait=3) # 3초 대기
# driver.close() # 창 닫기