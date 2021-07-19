from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe") 
login_url = "https://www.ycs.or.kr/page/etc/login.php"
reservation_url = "https://www.ycs.or.kr/yeyak/fmcs/43?facilities_type=C&base_date=20210719&center=YCS04&type=1002&part=02&place="
complete_url = "https://www.ycs.or.kr/yeyak/fmcs/12"

# 로그인 페이지로 이동
driver.get(login_url)
time.sleep(1) # 1초

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
time.sleep(1) # 1초

# 로그인 완료 후 예약 페이지로 이동
driver.get(reservation_url + "1")
time.sleep(1) # 1초

res_date = driver.find_element_by_xpath("//*[@id='date-20210726']/span")
if res_date.text == "예약가능":
	res_date.click()
	time.sleep(0.3) # 0.3초
	
	res_time = driver.find_element_by_xpath("//*[@id='contents']/article/div/div/div[4]/div[2]/div/table/tbody/tr[9]/td[4]")
	
	if res_time.text == "예약가능":
		res_check1 = driver.find_element_by_xpath("//*[@id='checkbox_time_6']")
		res_check2 = driver.find_element_by_xpath("//*[@id='checkbox_time_7']")
		res_check1.click()
		res_check2.click()
		time.sleep(0.2) # 0.2초

		register_btn = driver.find_element_by_class_name("action_application")
		register_btn.click()
		
		team_nm = driver.find_element_by_name("team_nm")
		team_nm.send_keys("뜸부기")
		users = driver.find_element_by_name("users")
		users.send_keys("4")
		tel = driver.find_element_by_name("tel")
		tel.clear()
		tel.send_keys("010-4240-3094")
		title = driver.find_element_by_name("title")
		title.send_keys("제 1회 천하제일 벌레대전")
		purpose = driver.find_element_by_name("purpose")
		purpose.send_keys("벌레대전")		

		agree_use = driver.find_element_by_name("agree_use")
		agree_use.click()
		
		captcha_img = driver.find_element_by_id("captcha_string_image")
		captcha_img_png = captcha_img.screenshot_as_png
		with open("captcha.png", "wb") as file:
			file.write(captcha_img_png)

		# captcha 분석 필요

		# captcha = driver.find_element_by_name("captcha")
		# captcha.send_keys("142191")

		time.sleep(3) # 3초

		res_btn = driver.find_element_by_class_name("action_write")
		# res_btn.click()


# time.sleep(1.5) # 1.5초
# # 예약 완료 페이지로 이동
# driver.get(complete_url)


