from database import db, Account

import time
import requests

def send_discord(webhook_url, text):
    return requests.post(webhook_url, {"content" : text})

def check_active_accounts(infinite = True, expire_time = 15, check_time = 10):
    while True:
        current_time = int(time.time())
        now_inactive_accounts = []

        active_accounts = Account.query.filter_by(active=True).all()
        for account in active_accounts:
            if (account.time < (current_time - expire_time)):
                now_inactive_accounts.append(account.name)
                account.active = False

        if (len(now_inactive_accounts) > 0):
            print("The following accounts will now be set to inactive: " + str(now_inactive_accounts))
            for inactive in now_inactive_accounts:
                send_discord('https://discordapp.com/api/webhooks/442903124555071488/Q0tkPSQI_QGCH7h6WKH5p83B7_yg7kVXXl7ZaN-MK_auaC2L7BXq07I8Pfrr7JvzM6KJ', inactive + ' is now inactive')
        db.session.commit()

        if not infinite:
            break

        time.sleep(check_time)

check_active_accounts()