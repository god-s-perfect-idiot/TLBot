from webbot import Browser
import datetime
import time
from essential_generators import DocumentGenerator

web = Browser()
gen = DocumentGenerator()

def comments(c_url):
	web.go_to(c_url)
	time.sleep(10)
	k = 0
	web.type("Hello fellow TL-in mates. This is Anti-Hawk. Mark 2. Not developed for personalised replies, yet. I'll make sure to carry this post.",tag='textarea',classname='dark',xpath="/html/body/div/div/div[4]/div/div[2]/ul/li[1]/form/textarea")
	time.sleep(2)
	web.click(tag='button', classname='border',xpath="/html/body/div/div/div[4]/div/div[2]/ul/li[1]/form/button",text="Post")
	time.sleep(5)
	for i in range(10000000):
			para = gen.sentence()
			web.type(para,tag='textarea',classname='dark',xpath="/html/body/div/div/div[4]/div/div[2]/ul/li[1]/form/textarea")
			time.sleep(2)
			web.click(tag='button', classname='border',xpath="/html/body/div/div/div[4]/div/div[2]/ul/li[1]/form/button",text="Post")
			time.sleep(5)

web.go_to('https://web.talklife.co/login')

web.type('ctf.hestia@gmail.com','Email')
web.type('Ctf11@11hof','Password')
web.click(text='Login',classname="green")

time.sleep(2)


comments("https://web.talklife.co/post/13784729#cyan2")
#web.click(text='Next', tag='button', classname='black')
