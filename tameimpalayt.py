from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.youtube.com/');


searchBox = driver.find_element_by_xpath('//input[@id="search"]')
searchBox.send_keys('let it happen tame impala');

driver.implicitly_wait(3)
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click();

video = driver.find_element_by_xpath('//*[@id="video-title"]')
video.click()