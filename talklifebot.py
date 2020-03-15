from webbot import Browser
import time

web = Browser()


#Logging in
web.go_to('https://web.talklife.co/login')
web.type("backd00r257@gmail.com", into="Email")
web.type("Talk11@11life", into="password")
web.click(text="Login", tag="input")

time.sleep(5)

#skipping beta notif

web.click(tag="img" , multiple=True, loose_match=True)
