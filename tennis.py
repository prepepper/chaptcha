from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe") 
login_url = "https://www.ycs.or.kr/page/etc/login.php"
reservation_url = "https://www.ycs.or.kr/yeyak/fmcs/43?facilities_type=C&base_date=20210719&center=YCS04&type=1002&part=02&place="

# 로그인 페이지로 이동
driver.get(login_url)
time.sleep(2) # 2초

# 아이디 입력
id_box = driver.find_element_by_name("id")
id_box.send_keys("swhoo")
time.sleep(0.5) # 0.5초

# 비밀번호 입력
pw_box = driver.find_element_by_name("pw")
pw_box.send_keys("!hsw30941245")
time.sleep(0.5) # 0.5초

# 로그인 시도
pw_box.submit()
time.sleep(2) # 2초

# 로그인 완료 후 예약 페이지로 이동
driver.get(reservation_url + "1")
time.sleep(2) # 2초










# # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
# element = driver.find_element_by_class_name("img")
# image_location = element.location
# image_size = element.size
# # driver.quit()
 
# # 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
# im = Image.open(BytesIO(png))
# left = image_location['x']
# top = image_location['y']
# right = image_location['x'] + image_size['width']
# bottom = image_location['y'] + image_size['height']
# im = im.crop((left, top, right, bottom))
# im.save('testsele.png')