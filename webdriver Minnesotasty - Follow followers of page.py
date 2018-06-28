import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

##settings section##


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)# Optional argument, if not specified will search path.
wait = WebDriverWait(driver, 10)


def scrollbottom():
    # define initial page height for 'while' loop
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        else:
            last_height = new_height
def scroll():
    SCROLL_PAUSE_TIME = 0.9
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
    # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def login():
    actions = ActionChains(driver)
    driver.get("https://soundcloud.com/")
    time.sleep(5)
    login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div > div.l-front-hero.l-inner-fullwidth > div > div > div.frontHero__signin > button.g-opacity-transition.frontHero__loginButton.g-button-transparent-inverted.sc-button.sc-button-medium.loginButton')))
    actions.move_to_element(login)
    actions.click(login)
    actions.perform()
    username = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='formControl']")))
    actions.move_to_element(username)
    actions.click(username)
    actions.perform()
    actions.send_keys('minnesotasty@gmail.com')
    actions.send_keys(Keys.RETURN)
    print(driver.window_handles)

def findmn():
    for i in profileurls:
        driver.get(i)    
        src = driver.get(i)
        text_found = re.search(r'Minneapolis', src)
        self.assertNotEqual(text_found, None)


             
def main():
    #url = input("enter url of page who's followers you would like to scrub")
    driver.get("https://soundcloud.com/freewifi-music/followers");
    time.sleep(2)# Let the user actually see something!
    
    follower = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'userBadgeListItem')))
    #passclick = driver.find_element_by_name('pass')
    ###hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
    
    actions = ActionChains(driver)
    actions.move_to_element(follower)
    actions.click(follower)
    actions.perform()
    driver.get("https://soundcloud.com/freewifi-music/followers");
    follower = driver.find_element_by_class_name('userBadgeListItem')
    scroll()
    profileurls = []
    mnprofiles = []
    #profiles = driver.find_elements_by_class_name('userBadgeListItem')
    #url = profile.find_element_by_css_selector('a').get_attribute('href')
    #profiles = []
    #print(profiles)
    for profile in driver.find_elements_by_class_name("userBadgeListItem"):
        url = profile.find_element_by_css_selector('a').get_attribute('href')
        profileurls.append(url)
    for i in profileurls:
        driver.get(i)    
        src = driver.page_source
        #text_found = re.search('Minneapolis', src)
        if "Minnesota" or "minnesota" or "MPLS" or "mpls" or "Minneapolis" or "minneapolis" or "St. Paul" or "Twin Cities" in src:
            mnprofiles.append(i)
            print(mnprofiles)

            
    #findmn()
    #login()

    
    #yeet
    
    
    #while driver.find_element_by_class_name("yt-uix-button") is not False:
     #   for title in driver.find_elements_by_class_name("yt-uix-tile-link"):
      #      print(title.text)
    #actions.send_keys('', infoemail)
    #actions.move_to_element(passclick)
    #actions.click(passclick)
    #actions.send_keys('', pword)
    #button = driver.find_element_by_xpath('//*[@id="u_0_0"]')
    #actions.move_to_element(button)
    #actions.click(button)
    
    
    #settingsbutton = wait.until(EC.element_to_be_clickable((By.ID, 'userNavigationLabel')))
    
    

main()


def otherfunction():
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5) # Let the user actually see something!
#driver.quit()
