import urllib2 as urllib
import oauth2 as oauth
import json
import pymongo


# Application authintication parameters

api_key = 'XVvEKkU8p1f2iiLTzZHKp4KV7'
api_secret = 'aTMRT4mbuFAYUAN6lrmgdAELiU9MfiOGxZvpwffmzo6XP831Pj'
access_token = '2793461214-P0icEAGaQC85wvXKPpaIKOPxpM6SIYZOMtQYf7c'
access_token_secret = 'pdaHJ0GdQeHpbxZeVHvIxbtTZyzhNpc9clFtv8rhoygHt'

url = 'https://stream.twitter.com/1.1/statuses/filter.json?'


_debug=0

oauth_token = oauth.Token(key=access_token, secret=access_token_secret)
oauth_consumer= oauth.Consumer(key=api_key, secret=api_secret)

signature_method = oauth.SignatureMethod_HMAC_SHA1()

http_method ='GET'

http_handler = urllib.HTTPHandler(debuglevel = _debug)
https_handler = urllib.HTTPSHandler(debuglevel = _debug)

# Construct twitter request

def twitterReq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer, token=oauth_token, http_method=http_method,http_url=str(url),parameters=parameters)
    
    req.sign_request(signature_method, oauth_consumer, oauth_token)
    headers = req.to_header()
    
    if http_method =="POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()
    
    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    
    response = opener.open(url, encoded_post_data)
    return response

def tweetData():
    url = "https://stream.twitter.com/1.1/statuses/filter.json?track=AAP BJP"
    parameters = []

    response = twitterReq(url, "GET", parameters)


    for tweet in response: 
        print tweet
        

if __name__ == '__main__':
    tweetData()
