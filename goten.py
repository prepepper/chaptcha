from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe") 
login_url = "https://www.ycs.or.kr/page/etc/login.php"
reservation_url = "https://www.ycs.or.kr/yeyak/fmcs/43?facilities_type=C&base_date=20210719&center=YCS04&type=1002&part=02&place="

# 로그인 페이지로 이동
driver.get(login_url)
time.sleep(1.5) # 2초

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
time.sleep(1.5) # 2초

# 로그인 완료 후 예약 페이지로 이동
driver.get(reservation_url + "1")
time.sleep(1.5) # 1.5초

res_date = driver.find_element_by_xpath("//*[@id='date-20210724']/span")
if res_date.text == "예약가능":
	res_date.click()
	time.sleep(0.3) # 0.3초
	
	res_time = driver.find_element_by_xpath("//*[@id='contents']/article/div/div/div[4]/div[2]/div/table/tbody/tr[7]/td[4]")
	
	if res_time.text == "예약가능":
		res_check = driver.find_element_by_xpath("//*[@id='checkbox_time_6']")
		res_check.click()
		time.sleep(0.2) # 0.2초

		register_btn = driver.find_element_by_class_name("action_application")
		register_btn.click()
		


# time.sleep(3) # 3초





