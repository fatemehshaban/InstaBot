from time import sleep
from selenium import webdriver

def sendmsg(driver,victim,message):
   driver.get('https://www.instagram.com/%s' % victim)
   sleep(2)
   try:
      driver.find_element_by_xpath('//h2[text()="Sorry, this page isn\'t available."]')
      driver.minimize_window()
      return 0
   except:
      try:
         #for private followed account
         driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div').click()
      except:
         try:
            #for public followed account
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div').click()
                                          
         except:
            #for unfollowed account
            driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(victim)
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div').click()
      sleep(2)
      print("sending message...")
      driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
      sleep(1)
      driver.find_element_by_xpath('//button[text()="Send"]').click()
      print("_______Message sent Successfully______")
      driver.minimize_window()
      return 1



def blast(driver,victim,message,x):
   driver.get('https://www.instagram.com/%s' % victim)
   sleep(2)
   try:
      driver.find_element_by_xpath('//h2[text()="Sorry, this page isn\'t available."]')
      driver.minimize_window()
      return 0
   except:
         try:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div').click()
         except:
            try:
               driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div').click()
            except:
               driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
               sleep(2)
               driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
               sleep(2)
               driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(victim)
               sleep(2)
               driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
               sleep(2)
               driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div').click()
         sleep(2)
         print("sending message...")
         for i in range(x):
            driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
            driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
         print("_______Message sent Successfully______")
         driver.minimize_window()
         return 1