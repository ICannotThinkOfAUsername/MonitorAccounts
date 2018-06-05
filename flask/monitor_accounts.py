from database import db, Account
from config import pa_username, webhook_url, expire_after, check_every

import time
import requests

def send_discord(webhook_url, text):
    return requests.post(webhook_url, {"content" : text})

def check_active_accounts(infinite = True):
    while True:
        current_time = int(time.time())
        now_inactive_accounts = []

        active_accounts = Account.query.filter_by(active=True).all()
        for account in active_accounts:
            if (account.time < (current_time - expire_after)):
                now_inactive_accounts.append(account.name)
                account.active = False

        if (len(now_inactive_accounts) > 0):
            print("The following accounts will now be set to inactive: " + str(now_inactive_accounts))
            for inactive in now_inactive_accounts:
                send_discord(webhook_url, inactive + ' is now inactive')
        db.session.commit()

        if not infinite:
            break

        time_file = open('/home/'+pa_username+'/mysite/time.txt', 'w')
        time_file.write(str(current_time))
        time_file.close()

        time.sleep(check_every)

check_active_accounts()