# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import random
import time
from datetime import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def getlist(channel_list, authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        for channel_id in channel_list:

            url = "https://discord.com/api/v9/channels/{}/messages?limit=10".format(channel_id)
            try:
                res = requests.get(url=url, headers=header)
                json_results = json.loads(res.text)
                num_array = len(json_results)
                for i in range(0, num_array):
                    try:
                        # 3. update the lottery keyword here, eg. **GIVEAWAY**
                        if "put the lottery keyword here" in json_results[i]["content"]:
                            msg_id = json_results[i]["id"]
                            print("date", datetime.now())
                            print("id", json_results[i]["id"])
                            print("content", json_results[i]["content"])
                            print("--")
                            url = "https://discord.com/api/v9/channels/{}/messages/{}/reactions/%F0%9F%8E%89/%40me".format(
                                channel_id, msg_id)
                            requests.put(url=url, headers=header)
                            time.sleep(1)
                            continue

                    except:
                        pass
                    continue


            except:
                pass
            continue


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
