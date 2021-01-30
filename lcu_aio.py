# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import requests
import base64
import json
import pprint
import urllib3

urllib3.disable_warnings()

class lcuconnector:
    def connect(lockfile_path="default"):
        if lockfile_path == "default":
            lockfile_path = "C:\\Riot Games\\League of Legends\\lockfile"
        if lcuconnector.check_exist(lockfile_path):
            return lcuconnector.readFile(lockfile_path)
        else:
            return "Couldn't read lockfile!\nThis could mean that either the \
            path is not the right or the League Client is not opened!"

    def check_exist(lockfile_path):
        return os.path.exists(lockfile_path)

    def readFile(lockfile_path):
        lockfile = open(lockfile_path, "r")
        data = lockfile.read()
        data = data.split(":")
        data_dict = {
            "port": data[2],
            "url": "https://127.0.0.1:{}".format(data[2]),
            "auth": "riot:{}".format(data[3]),
            "connection_method": data[4]
        }
        return data_dict

class lcu_api:
    def help(lcu_data, p=False):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/Help"
        request = requests.post(url, headers=headers, verify=False)
        request_json = request.json()
        if p == True:
            xtra.jprint(request_json)
        return request_json

    def get_current_summoner(lcu_data, p=False, target=False):
        target_ok = ["levelPercentNext", "accountId", "displayName", "internalName",
                     "nameChangeFlag", "profileIconId", "puuid", "rerollPoints",
                     "summonerId", "summonerLevel", "unnamed", "xpSinceLastLevel",
                     "xpUntilNextLevel"]
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-summoner/v1/current-summoner"
        request = requests.get(url, headers=headers, verify=False)
        request_json = request.json()
        if p == True:
            xtra.jprint(request_json)
        if target != False and target in target_ok:
            if target == "levelPercentNext":
                return request_json["percentCompleteForNextLevel"]
            return request_json[target]
        elif target != False and target not in target_ok:
            return F"Target was wrongly specified: {target}"
        return request_json

    def get_current_summoner_jwt(lcu_data, p=False):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-summoner/v1/current-summoner/jwt"
        request = requests.get(url, headers=headers, verify=False)
        if p == True:
            print(request.text.strip('"'))
        return request.text.strip('"')

    def get_current_summoner_background_skin_id(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-summoner/v1/current-summoner/summoner-profile"
        request = requests.get(url, headers=headers, verify=False)
        return request.json()["backgroundSkinId"]



class xtra:
    def base64encode(text):
        text = base64.b64encode(text.encode("ascii")).decode("ascii")
        return text

    def jprint(json_parsed):
        print(json.dumps(json_parsed, indent=4, sort_keys=True))

lcu = lcuconnector.connect(
        "D:\\Riot Games\\League of Legends\\lockfile"
      )

# lcu_api.help(lcu)
# lcu_api.get_current_summoner(lcu, target="summonerId")
# lcu_api.get_current_summoner_jwt(lcu)
print(lcu_api.get_current_summoner_background_skin_id(lcu))
