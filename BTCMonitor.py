# IMPORTS
import requests 
import os
import time
from datetime import datetime

# OTHER
##############################################################################################################################################################################

# USE CURRENCY CODE ON END OF LINK, E.G USD, GBP, EUR, SOME MAY NOT BE SUPPORTED BY COINBASE
btc_url = "https://api.coinbase.com/v2/prices/spot?currency=GBP"

# DISCORD WEBHOOK LINK HERE
# SEE https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks FOR MORE INFO
discord_webhook_url = ""

send_requests_safe = False

time_sent_at =  datetime.now()

##############################################################################################################################################################################

# PROCESS
##############################################################################################################################################################################

def time_manager():
    send_requests_safe = True

    #######################

    btc_request = requests.get(btc_url)

    btc_request_sanitised = str(btc_request.text).replace('{"data":{"base":"', '').replace('"', '').replace(',', ' ').replace('currency:', '').replace('amount:', '').replace('}}', '')

    # HERE, YOU WILL NEED TO REPLACE THE £ WITH THE CURRENCY SYMBOL WHICH IS THE SAME AS USED ON THE COINBASE LINK.
    # E.G, IF THE COINBASE LINK IS https://api.coinbase.com/v2/prices/spot?currency=EUR , .replace('EUR', '€') WOULD BE USED
    
    btc_request_beautify = btc_request_sanitised.replace('GBP', '£').split()

    btc_request_beautify_2 = (btc_request_beautify[1] + btc_request_beautify[2]).replace(' ', '') 

    btc_nice_string = "BTC-GBP [1 BTC] = " + btc_request_beautify_2 + " | As-Of: " + str(time_sent_at)

    #######################

    discord_btc_nice_string = "```" + "BTC-GBP [1 BTC] = " + btc_request_beautify_2  +  " | As-Of: " + str(time_sent_at) + "```"

    discord_webhook_content = {
        "content":""  + discord_btc_nice_string + ""
    }

    discord_webhook_post = requests.post(discord_webhook_url, data=discord_webhook_content)

    while True:
        print("[COINBASE REQUEST] " + btc_nice_string)
        print("[DISCORD REQUEST] " + str(discord_webhook_post.text))
        # CURRENT INTERVAL IS 1 HOUR (time.sleep() USES SECONDS), IT CAN BE CHANGED BY REPLACING THE 3600 BELOW
        time.sleep(3600)

##############################################################################################################################################################################

# INIT
##############################################################################################################################################################################

os.system("cls")

time_manager()

##############################################################################################################################################################################
