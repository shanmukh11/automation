from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def play(element,notes):
	for note in notes:
		key = mapkey.get(note,"")
		if(not key):
			time.sleep(0.25)
		else:
			element.send_keys(key);
		time.sleep(0.25);

song = input("Choose your song.\nPress 1 for Jingle Bells\nPress 2 for Birthday song\n")
notes=""

if(song == '1'):
	notes = "eee eee egcde  fffffeeeeedded g eee eee egcde  fffffeeeeggfdc"


elif(song == '2'):
	notes = "GGAGcB GGAGdc GGgecBA ffecdc"

driver = webdriver.Chrome()


driver.get('https://www.onlinepianist.com/virtual-piano')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loadingB'][contains(@style, 'display: none')]")))


mapkey = {
	'G':'t',
	'A':'y',
	'B':'u',
	'c':'i',
	'd':'o',
	'e':'p',
	'f':'z',
	'g':'x',
	'a':'c',
	'b':'v',
	' ': ''
}


piano = driver.switch_to.active_element;

play(piano,notes)
