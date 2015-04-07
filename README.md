# nstalike

This is a small script written in Python, that uses Instagram API to infinitely like photos found by #hashtag.

###Features:

* Infinitely like photos found by hashtag
* Save liked photos

###Needed Python modules:

* python get-pip.py
* sudo pip install requests
* sudo pip install pyopenssl ndg-httpsclient pyasn1

###Steps:
Don't forget to check [Instagram API](https://instagram.com/developer/).

1. Register your client: REDIRECT-URI is needed to obtain access **CODE** (use [Github Pages](http://pages.github.com)).
2. Obtain: CLIENT-ID, CLIENT-SECRET
3. Go to [https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code&scope=likes](https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code&scope=likes) and give access, you will be redirected.
4. http://REDIRECT-URI?code=CODE. Use it in Terminal.
5. curl -F 'client_id=CLIENT-ID' \
    -F 'client_secret=CLIENT-SECRET' \
    -F 'grant_type=authorization_code' \
    -F 'redirect_uri=REDIRECT-URI' \
    -F 'code=CODE' \
    https://api.instagram.com/oauth/access_token
6. You will get the **access_token**, paste it to the nstalike.py (*token* variable). Change the *tag*. Save.
7. Terminal: python nstalike.py