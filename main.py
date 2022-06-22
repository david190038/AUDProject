import destination as destination
from django.contrib.sessions.backends import file
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image

# selenium 3
from webdriver_manager.chrome import ChromeDriverManager

global _URL
global _word
global _path
global _n_images
global _filename

_word = str(input('Wort: '))
#_word = 'auto'
_n_images = int(input('Number of Images: '))
#_n_images = 20
#_path = str(input('Temp Ordner:' ))
print('Temporären Pfad im Programm ändern!')
_path = 'D:/Vucak1Duranovic2Mayer3'
#RESIZED_FOLDER = str(input('Pfad für die optimierten Bilder: '))
print('Final Ordner im Programm Ändern')
RESIZED_FOLDER = 'D:/test'
_filename = str(input('Name vom File: '))
#_filename = 'ClassOne'


URL = 'https://www.google.com/search?site=&tbm=isch&source=hp&q='
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.fullscreen_window()

##driver.get('https://www.google.com/search?q=giraffe')
driver.get(URL + _word)

time.sleep(2)
driver.fullscreen_window()

## coockies
try:
    cookies_btn = driver.find_element_by_id('L2AGLb')
    cookies_btn.click()
except NoSuchElementException:  #spelling error making this code not work as expected
    pass

time.sleep(2)
driver.fullscreen_window()

try:
    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')

    first_time = True
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            ## end reached - last input is show more results cock

            all_inputs = driver.find_elements_by_tag_name("input")
            all_inputs.pop().click()

            time.sleep(3)
            if not first_time:
                break
            first_time = False

        last_height = new_height

except Exception:  #everything bc smart
    pass

for i in range(1, _n_images+9):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(_path + '/' + _filename+str(i)+'.jpg')
    except:
        pass

for count in range(9, _n_images):
    try:
        image = Image.open(_path + '/' + _filename+str(count)+'.jpg')
        if (image.width < image.height * 6):
            rgb_im = image.convert('RGB')
            rgb_im = rgb_im.resize((int(500), int(500)), Image.ANTIALIAS)
            rgb_im.save(RESIZED_FOLDER + "/" + _filename + str(count-9) + '.jpg')
    except:
        pass
