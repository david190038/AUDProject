from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# selenium 3
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.fullscreen_window()

##driver.get('https://www.google.com/search?q=giraffe')
driver.get('https://www.google.com/search?site=&tbm=isch&source=hp&q=giraffe')

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

for i in range(1, 270):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('D:\\test\\giraffe ('+str(i)+').jpg')
    except:
        pass