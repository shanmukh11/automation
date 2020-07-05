from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.youtube.com/');


searchBox = driver.find_element_by_xpath('//input[@id="search"]')
searchBox.send_keys('let it happen tame impala');


searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
driver.implicitly_wait(3)
searchButton.click();

video = driver.find_element_by_link_text('Tame Impala - Let It Happen (Official Video)')
video.click()