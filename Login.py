from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

def loggin(driver,username,password):
	print("chrome opened")
	driver.get("https://www.instagram.com/accounts/login/?next=/")
	sleep(10)
	try:
		driver.find_element_by_xpath('//*[@name="username"]').send_keys(username)
		driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
		sleep(2000)
		driver.find_element_by_xpath('//button[@type="submit"]').click()
		element=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
		element.click()
		sleep(4)
		driver.find_element_by_xpath('//button[text()="Not Now"]').click()
		sleep(1)
		print("Logged in Successfully")
		return 1
	except Exception as es:
		print(es)
		#driver.quit()
		return 1

def chk_login(driver,username,password):
	print("chrome opened")
	driver.get("https://www.instagram.com/accounts/login/?next=/")
	sleep(10)
	try:
		driver.find_element_by_xpath('//*[@name="username"]').send_keys(username)
		driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
		sleep(2000)
		driver.find_element_by_xpath('//button[@type="submit"]').click()
		element=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
		element.click()
		sleep(4)
		driver.find_element_by_xpath('//button[text()="Not Now"]').click()
		sleep(1)
		driver.minimize_window()
		print("Logged in Successfully")
		return 1
	except Exception as es:
		print(es)
		#driver.quit()
		return 1

if __name__ == "__main__":
    print("Please run home_page.py")