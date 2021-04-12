import requests
import os
import time
from bs4 import BeautifulSoup
from keep_alive import keep_alive

webhook = os.getenv('WEBHOOK')
url = os.getenv('URL')


data = {
    "content" : "Likely taking patients!",
    "username" : "Doctor Bot-topus"
}

data["embeds"] = [
    {
        "description" : url,
        "title" : "Link to page"
    }
]

def pingDiscord():
	result = requests.post(webhook, json = data)
	try:
			result.raise_for_status()
	except requests.exceptions.HTTPError as err:
			print(err)
	else:
			print("Payload delivered successfully, code {}.".format(result.status_code))

def checkDoctor():
	html = requests.get(url).content
	soup = BeautifulSoup(html, features="html5lib")
	if "We are not accepting new patients at this time." not in soup.prettify():
		pingDiscord()

keep_alive()
while True:
	checkDoctor()
	time.sleep(60)