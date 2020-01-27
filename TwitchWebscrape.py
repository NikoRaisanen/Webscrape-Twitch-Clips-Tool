#!/usr/bin/env python

from selenium import webdriver
import time
import sys
import pyautogui

main_url = input("Paste the url of the channel or game page that you want to download clips from: ")
list_of_clips = []
list = []

driver = webdriver.Firefox()
driver.get(main_url)
time.sleep(10)
elements_found = driver.find_elements_by_css_selector(
    '[class="tw-interactive tw-link tw-link--hover-underline-none tw-link--inherit"]')

for element in elements_found:
    list_of_clips.append(element.get_attribute('href'))

File_object = open(r"ClipsList.txt", 'w')

#  Append the links into a list and to a local file
for link in list_of_clips:
    if 'clip' in link:
        list.append(link)
        File_object.write(link + '\n')
print(list)
print(len(list))
driver.quit()

# Automating clip download process
print("\n\nWould you like to begin downloading the files? (Y/n)")
user_response = input()
if user_response == 'Y':
    profile = webdriver.FirefoxProfile("/home/niko/.mozilla/firefox/mudmu5st.default-release")

    driver = webdriver.Firefox(profile)
    driver.get('https://clipr.xyz/')
    time.sleep(10)

    for i in range(len(list)):
        url_enter = driver.find_element_by_xpath('//*[@id="clip_url"]')
        url_enter.click()
        pyautogui.typewrite(list[i], interval=0.01)
        get_dl_link = driver.find_element_by_xpath('//*[@id="app"]/main/div[1]/div/div/div/div/form/button')
        get_dl_link.click()
        time.sleep(2)
        dl_button = driver.find_element_by_xpath('//*[@id="app"]/main/div[1]/div/div/div/div/div[2]/div[2]/div[1]/a[2]')
        dl_button.click()
        time.sleep(2)
        driver.get('https://clipr.xyz/')
        time.sleep(5)
        print('Clip number %s downloaded...' % str(i+1))

else:
    sys.exit(0)
driver.quit()
