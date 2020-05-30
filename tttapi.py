from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random_word import RandomWords
import time

r = RandomWords()
web = webdriver.Chrome()

seed = r.get_random_word()

web.get('https://talktotransformer.com/')

time.sleep(2)
wordbox = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[3]/div/div/div/textarea[1]')
wordbox.send_keys(seed)

submit = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[4]/button')
submit.click()

i=0
while(True):
    i+=1

web.close()
