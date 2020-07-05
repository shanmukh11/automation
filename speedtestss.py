from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.speedtest.net/')

gobutton = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
gobutton.click()

try:
	WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "overall-progress"), 'Your speed test has completed.'))
	driver.implicitly_wait(10)
except:
	print("Took too long")

ele = driver.find_element_by_class_name('speedtest-container')

ele.screenshot("screenshot.png")