# Buatan Kenzawaa A.K.A Babwa
#Jangan recode:v
from random_user_agent.user_agent import UserAgent
import requests
import random, sys
# -----------------------------------

s = requests.Session()
xsrf = (random.random())*10**16
s.headers.update({
"Cookie": "_xsrf="+str(xsrf),
"X-XSRFToken": str(xsrf),
"User-Agent": UserAgent().get_random_user_agent()
})

def pendekinUrl(url):
    BASEURL = 'https://bitly.com/data/anon_shorten'
    BASEURL1 = 'https://snip.ly/pub/snip'
    data = {
        "url": url
    }
    res = s.post(BASEURL, data).json()
    if res['status_txt'] != 'OK':
        if res['status_txt'] == 'RATE_LIMIT_EXCEEDED':
            data['button_url'] = 'https://sniply.io/pricing/'
            data['cta_message'] = "Sign up and customize the CTA!"
            try: return requests.post('https://snip.ly/pub/snip', data).json()['snip_url']
            except: return url+' (bit.ly limit)'
        return 'Error: ' + res['status_txt']
    else:
        return res['data']['link']

def main(url):
    if 'Err' not in pendekinUrl(url):
        print('Your shortlink is: '+pendekinUrl(url))
        
if __name__ == '__main__':
    try: main(sys.argv[1]) 
    except: print('Use: python file.py [link]')