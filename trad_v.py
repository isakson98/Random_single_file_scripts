from Config import tr_view_passw, tr_view_user
from splinter import Browser
from time import sleep
import requests
import urllib

##  Overview of the script
# vist traderview
# log in 
# click on charts
# click on layout (clicks on the first layout)
# click on manage drawings
# delete all drawings
# save the changes

#if you click on anything in the browser and disrupt the deletion process, 
#it'll break the loop and save changes


def visit_and_log_and_delete():
    browser.visit('https://www.tradingview.com/#signin')

    browser.find_by_xpath("//input[@name='username']").fill(tr_view_user) ## enter username
    browser.find_by_xpath("//input[@name='password']").fill(tr_view_passw)## enter password
    browser.find_by_xpath("//button[@type='submit']").click()
    browser.click_link_by_href('/chart/')

    #moving the mouse
    browser.find_by_xpath("//div[@class='button-263WXsg- isTransparent-sRmateFl']")

    #scrolling down the side menu
    browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    browser.find_by_id("drawing-toolbar-object-tree").click()
    
    #clicking on the lay out button
    sleep(1)
    browser.find_by_id("drawing-toolbar-object-tree").click()

    sleep(1)
    browser.find_by_xpath("//div[@class='tv-tabs__tab']").click()



    #iterating though every ticker to delete drawings until there is an error clicking, which means there is nothing left to click
    while True:
        try:
            #deletes every 50 milliseconds
            sleep(0.05)
            browser.find_by_xpath("//div[@class='tv-objects-tree-item__control-buttons tv-objects-tree-item__control-buttons--left']").first.click()
            browser.find_by_xpath("//span[@title='Delete all drawing for this symbol']").click()
        except:
            break

    
    #saving the changes
    browser.find_by_xpath("//div[@class='menu-yTeik9rB']").click()
    browser.find_by_xpath("//div[@class='saveLayoutMenuItem-5UXym92P item-2xPVYue0 item-1dXqixrD']").click()
   


executable_path = {'executable_path' : r'C:\Users\isaks\Desktop\chromedriver_win32\chromedriver'}
browser = Browser('chrome', **executable_path, headless = False )
visit_and_log_and_delete()
