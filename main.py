import pytesseract
import cv2
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set browser to Firefox (requires geckodriver.exe in main Python executable folder
browser = webdriver.Firefox()
# set config for OCR
custom_config = r'-l eng --oem 3 --psm 6'

# resize all input images to factor for different screen resolutions
width = 1024
height = 576
dim = (width, height)

# cropping values
h = 110
w = 95
# column 1 (2 tags)
y1 = 275
x1 = 345
# column 2 (2 tags)
y2 = 275
x2 = 450
# column 3 (1 tag)
h3 = 55
w3 = 98
y3 = 275
x3 = 560


def gettags(file_name):
	img = cv2.imread(file_name)

	resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
	resized1 = resized[y1:y1 + h, x1:x1 + w]
	resized2 = resized[y2:y2 + h, x2:x2 + w]
	resized3 = resized[y3:y3 + h3, x3:x3 + w3]

	# pre-process images for better results
	resized1 = cv2.bitwise_not(resized1)
	resized2 = cv2.bitwise_not(resized2)
	resized3 = cv2.bitwise_not(resized3)

	# find tags by column and split them into lists of strings
	col1 = pytesseract.image_to_string(resized1, config=custom_config)
	col1 = col1.splitlines()
	col2 = pytesseract.image_to_string(resized2, config=custom_config)
	col2 = col2.splitlines()
	col3 = pytesseract.image_to_string(resized3, config=custom_config)
	col3 = col3.splitlines()

	# concatenate column into main tag list
	tag_list = col1 + col2 + col3
	# replace in-game 'Crowd-Control' tag to aceship 'Crowd Control' tag
	tag_list = [sub.replace('Crowd-Control', 'Crowd Control') for sub in tag_list]
	print("Tag List:", tag_list)
	return tag_list


if __name__ == "__main__":
	try:
		image_file = input("Enter screenshot filename: ")
		# get tags from screenshot
		tags = gettags(image_file)
		# browse to aceship recruitment calculator, switch server to EN
		browser.get('https://aceship.github.io/AN-EN-Tags/akhr.html')
		sleep(1)
		server = browser.find_element_by_id('navitemRegion')
		sleep(0.25)
		server.click()
		server_en = browser.find_element_by_link_text('English')
		sleep(0.25)
		server_en.click()

		# iterate over tag list and input tags
		tag_input = browser.find_element_by_id('fastInput')
		for i in range(len(tags)):
			sleep(0.25)
			tag_input.send_keys(tags[i])
			sleep(0.25)
			tag_input.send_keys(Keys.ENTER)
	except IOError:
		pass
