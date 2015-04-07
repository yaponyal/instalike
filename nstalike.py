#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Fix the url3lib error
import requests
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

#JSON objects to work, time to sleep
import json
import time

#Main variables
token = '************TOKEN************'
tag = '************TAG************'
mediaURI = 'https://api.instagram.com/v1/tags/'+tag+'/media/recent'
access_tokenText = '?access_token='+token
access_token = {'access_token': token}

#Generate headers (check API)
import hmac
from hashlib import sha256
ips = requests.get('http://httpbin.org/ip').json()['origin']
secret = '27283c33200b400395b065f82c9a9eb9'
signature = hmac.new(secret, ips, sha256).hexdigest()
header = {'X-Insta-Forwarded-For':'|'.join([ips, signature])}

#Like photos
def likePhoto(item,f):
	media_id = item['id']
	likeURI = 'https://api.instagram.com/v1/media/'+media_id+'/likes'
	r = requests.post(likeURI, data=access_token, headers=header)
	if r.status_code == 429:
		print('Error 429: Too many requests. Waiting for 5 minutes and continue')
		time.sleep(300)
	elif r.status_code == 400:
		raise SystemExit('Error 400: Banned? Stopping the script')
	else:
		f.write('Liked: @'+item['user']['username']+' - '+item['link']+' at '+time.ctime()+'\n')
		print('Liked: @'+item['user']['username']+' - '+item['link'])

#Recursive function to repeat for the whole day
def startParty():
	f = open('Liked.txt','a') #Write liked photos to a file
	r = requests.get(mediaURI+access_tokenText, headers=header)
	JSONdata = r.json()['data']
	counter = 0
	while counter < len(JSONdata):
		item = JSONdata[counter]
		likePhoto(item,f)
		print('60 sec sleep: '+time.ctime()) #Sleep every minute not to be banned
		time.sleep(60)
		counter +=1
	f.close()
	startParty()

startParty()