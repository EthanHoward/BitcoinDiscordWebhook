import requests 
import os
import time
from datetime import datetime

# OTHER
##############################################################################################################################################################################

btc_url = "https://api.coinbase.com/v2/prices/spot?currency=GBP"

discord_webhook_url = "https://discord.com/api/webhooks/845422574959198218/azGFtor3OnruTJ3oa-erzrRBOtAY7qJ-K1tFqobT2zElaEF8GG96jFIIoibjw0lJ8dPM"

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
        time.sleep(3600)

##############################################################################################################################################################################

# INIT
##############################################################################################################################################################################

os.system("cls")

time_manager()

##############################################################################################################################################################################
