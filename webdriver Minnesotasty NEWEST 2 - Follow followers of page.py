import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# settings section#


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)  # Optional argument, if not specified will search path.
wait = WebDriverWait(driver, 10)


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
    login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   '#content > div > div > div.l-front-hero.l-inner-fullwidth > div > div > div.frontHero__signin > button.g-opacity-transition.frontHero__loginButton.g-button-transparent-inverted.sc-button.sc-button-medium.loginButton')))
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


def getmnlist(soundcloudpage):
    # url = input("enter url of page who's followers you would like to scrub")
    driver.get(soundcloudpage)
    time.sleep(2)  # Let the user actually see something!

    follower = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'userBadgeListItem')))
    # passclick = driver.find_element_by_name('pass')
    ###hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

    actions = ActionChains(driver)
    actions.move_to_element(follower)
    actions.click(follower)
    actions.perform()
    driver.get(soundcloudpage)
    follower = driver.find_element_by_class_name('userBadgeListItem')
    scroll()
    profileurls = []
    mnprofiles = []
    # profiles = driver.find_elements_by_class_name('userBadgeListItem')
    # url = profile.find_element_by_css_selector('a').get_attribute('href')
    # profiles = []
    # print(profiles)

    # To save a new file/ open new one#
    savestring = soundcloudpage.replace('/', '-')
    saveas = savestring[24:] + '.txt'
    print(saveas)
    path = "C:\\Python\\soundcloudlists\\"
    thefile = open(path + saveas, 'w+')
    bigname = os.path.join(path, saveas)
    print(bigname)

    # set all follower urls in list, compare list to old list, for new ones do stuff#
    for profile in driver.find_elements_by_class_name("userBadgeListItem"):
        url = profile.find_element_by_css_selector('a').get_attribute('href')
        profileurls.append(url)
    for i in profileurls:
        if i not in thefile.read():
            driver.get(i)
            src = driver.page_source
            # text_found = re.search('Minneapolis', src)
            # or "minnesota" or "MPLS" or "mpls" or "Minneapolis" or "minneapolis" or "St. Paul" or "Twin Cities"
            if "Minneapolis" or "Minnesota" or "St. Paul" in src:
                mnprofiles.append(i)
                print(mnprofiles)
                thefile.write("%s\n" % i)

                # findmn()
                # login()


                # yeet


getmnlist('https://soundcloud.com/swavymack-914705505/followers')

time.sleep(5)  # Let the user actually see something!
# driver.quit()
