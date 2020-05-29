from webbot import Browser
import datetime
import time
import gen as g
from essential_generators import DocumentGenerator

web = Browser(showWindow=False)
gen = DocumentGenerator()

def comments(c_url):
	web.go_to(c_url)
	k = 0
	for i in range(1000):
			para = gen.sentence()
			web.type(para,tag='textarea',classname='dark',xpath="/html/body/div/div/div[4]/div/div[2]/ul/li[1]/form/textarea")
			time.sleep(1)
			web.click(tag='button', classname='border',xpath="/html/body/div/div/div[4]/div/div[2]/ul/li[1]/form/button",text="Post")
			time.sleep(5)

web.go_to('https://web.talklife.co/login')

web.type('backd00r257@gmail.com','Email')
web.type('Talk11@11life','Password')
web.click(text='Login',classname="green")

time.sleep(2)

def post():
	web.go_to('https://web.talklife.co/post/new')
	web.click(tag='button', classname='black')
	stamp = datetime.datetime.now()
	wsd = g.gen()

	post = "W I S D O M:  "+wsd+"\n--------------------------------\nStamp: "+str(datetime.datetime.now())+"\n--------------------------------\n\n\n"+gen.sentence()

	time.sleep(2)
	web.type(post, into="Write your post", multiple=False, tag = 'textarea',xpath="/html/body/div/div/div[4]/div/div/textarea", loose_match=True)

	web.click(tag='button', classname='next', xpath="/html/body/div/div/div[4]/div/div/div/button[2]",multiple=False)
	web.click(tag='img', xpath="/html/body/div/div/div[3]/div/div/ul/li[5]/div[1]/img")
	time.sleep(2)
	web.click(tag="button", classname="black", xpath="/html/body/div/div/div[3]/div/div/div/button[2]",text="Post")

def run():
	time.sleep(2)
	post()
	time.sleep(2)
	web.click(tag='img',xpath="/html/body/div/div/div[3]/div/div/div/div/div/img")
	time.sleep(1)
	web.click(tag='img',xpath="/html/body/div/div/div[3]/div/div/div/div/div/img[2]")
	time.sleep(1)
	web.click(tag='img',xpath="/html/body/div/div/div[3]/div/div/div/div/div/img[2]")
	time.sleep(1)
	web.click(tag='img',xpath="/html/body/div/div/div[3]/div/div/div/div/div/img[2]")
	time.sleep(1)
	web.click(tag='img',xpath="/html/body/div/div/div[3]/div/div/div/div/div/img[2]")
	time.sleep(1)
	web.click(tag='button',xpath="/html/body/div/div/div[3]/div/div/div/div/p/button")

	time.sleep(1)
	web.click(tag='img',xpath='/html/body/div/div/div[6]/div/div[5]/img')
	time.sleep(1)
	web.click(tag='img',xpath='/html/body/div/div/div[2]/div[1]/a/img')

	time.sleep(2)
	web.click(tag='a',xpath='/html/body/div/div/div[4]/div[4]/div/div[3]/ul/li[1]/div/div[2]/a')

while(True):
	try:
		run()
	except:
		pass
	time.sleep(180)


#address = web.get_current_url()
#comments(address)
#comments("https://web.talklife.co/post/13822470#purple")
#web.click(text='Next', tag='button', classname='black')
