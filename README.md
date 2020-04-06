# Arknights Recruitment Tags OCR Tool
The arknights recruitment tags optical character recognition tool uses Optical Character Recognition (OCR) to automatically transcribe recruitment tags from a screenshot and enter them into the [Arknights Recruitment Calculator](https://aceship.github.io/AN-EN-Tags/akhr.html).

# Installation
Prerequisites
 - Requires Python 3.6+
 - [Tesseract](https://github.com/tesseract-ocr/tesseract)
 - [Python-tesseract](https://pypi.org/project/pytesseract/)
 - [OpenCV](https://pypi.org/project/opencv-python/)
 - [Selenium](https://pypi.org/project/selenium/)
   - The geckodriver webdriver must be installed and added to PATH

# Usage
Run the script by typing `python main.py` into your terminal. A prompt will appear asking the user to input the filename of the screenshot. The screenshot must be placed in the root folder of the script.
