
import http.client, urllib, os

# Send the push/message to all devices connected to Pushbullet
# use from mypushover import * in main program
def pushover(title,message,sound='pushover'):
    env_var = os.environ
    myuser, mytoken =  os.environ['PUSHOVER'].split(',')
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": mytoken,
            "user": myuser,
            "title":title,
            "message":message,
            "sound":sound
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()