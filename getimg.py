from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe") 
driver.get("https://play.google.com/store/apps/details?id=com.apro.cereal&hl=ko&gl=US")
 
# # 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.
# page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
# page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
# driver.set_window_size(page_width, page_height)
# png = driver.get_screenshot_as_png()
 
# # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
# element = driver.find_element_by_xpath("//*[@id='fcxH9b']/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[1]/div/img")
# image_location = element.location
# image_size = element.size
 
# # 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
# im = Image.open(BytesIO(png))
# left = image_location['x']
# top = image_location['y']
# right = image_location['x'] + image_size['width']
# bottom = image_location['y'] + image_size['height']
# im = im.crop((left, top, right, bottom))

# im.save('test12341.png')



element = driver.find_element_by_xpath("//*[@id='fcxH9b']/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[1]/div/img")
element_png = element.screenshot_as_png 
with open("test1.png", "wb") as file: 
	file.write(element_png)
