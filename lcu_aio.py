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
            raise Exception("Couldn't read lockfile!\nThis could mean that either the \
path is not the right or the League Client is not opened!")

    def check_exist(lockfile_path):
        return os.path.exists(lockfile_path)

    def readFile(lockfile_path):
        lockfile = open(lockfile_path, "r")
        data = lockfile.read().split(":")
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

    def get_current_summoner(lcu_data, target=False):
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
        if target != False and target in target_ok:
            if target == "levelPercentNext":
                return request_json["percentCompleteForNextLevel"]
            return request_json[target]
        elif target != False and target not in target_ok:
            return F"Target was wrongly specified: {target}"
        return request_json

    def get_current_summoner_jwt(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-summoner/v1/current-summoner/jwt"
        request = requests.get(url, headers=headers, verify=False)
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

    def post_current_summoner_background_skin(lcu_data, id: int):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        data = '{{"key": "backgroundSkinId", "value": {0}}}'.format(id)
        url = lcu_data["url"] + "/lol-summoner/v1/current-summoner/summoner-profile"
        request = requests.post(url, headers=headers, data=data, verify=False)
        return request.status_code

    def get_account_verified(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-account-verification/v1/is-verified"
        request = requests.get(url, headers=headers, verify=False)
        return request.json()["success"]

    def get_current_summoner_recently_played_champions_raw(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-acs/v2/recently-played-champions/current-summoner"
        request = requests.get(url, headers=headers, verify=False)
        return request.json()

    def get_current_summoner_recently_played_champions_ids(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-acs/v2/recently-played-champions/current-summoner"
        request = requests.get(url, headers=headers, verify=False)
        json_request = request.json()
        ids = []
        json_req = request.json()
        for x in list(json_request["champions"]):
            if x["championId"] in ids:
                pass
            else:
                ids.append(x["championId"])
        return ids

    def get_current_summoner_recently_played_champions_names(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-acs/v2/recently-played-champions/current-summoner"
        request = requests.get(url, headers=headers, verify=False)
        json_request = request.json()
        ids = []
        json_req = request.json()
        for x in list(json_request["champions"]):
            if x["championId"] in ids:
                pass
            else:
                ids.append(x["championId"])
        ids = xtra.get_champion_name_by_id_list(ids)
        return ids

    def get_recently_played_with_summoners_raw(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-match-history/v1/recently-played-summoners"
        request = requests.get(url, headers=headers, verify=False)
        return request.json()

    def get_recently_played_with_summoners_name(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-match-history/v1/recently-played-summoners"
        request = requests.get(url, headers=headers, verify=False)
        names = []
        for x in list(request.json()):
            names.append(x["summonerName"])
        return names

    def get_recently_played_with_summoners_name_champ(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-match-history/v1/recently-played-summoners"
        request = requests.get(url, headers=headers, verify=False)
        champ_and_names = {}
        for x in list(request.json()):
            champ_and_names[(x["summonerName"])] = xtra.get_champion_name_by_id(x["championId"])
        return champ_and_names

    def get_current_summoner_in_queue(lcu_data, rc=False):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        url = lcu_data["url"] + "/lol-matchmaking/v1/ready-check"
        request = requests.get(url, headers=headers, verify=False)
        request_json = request.json()
        if "state" in request_json:
            if request_json["state"] == "Invalid":
                return True
            elif request_json["state"] == "InProgress":
                if rc == True:
                    return 2
                return True
        elif request_json["httpStatus"] == 404:
            return False

    def get_current_summoner_ready_check(lcu_data, rc=False):
        is_in_q = lcu_api.get_current_summoner_in_queue(lcu_data,True)
        if is_in_q == 2:
            return True
        if is_in_q == True and is_in_q != 2 and rc == True:
            return 2
        return False

    def auto_accept_current_ready_check(lcu_data):
        ready_check = lcu_api.get_current_summoner_ready_check(lcu_data,True)
        if ready_check == True:
            auth = xtra.base64encode(lcu_data["auth"])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": F"Basic {auth}"
            }
            url = lcu_data["url"] + "/lol-matchmaking/v1/ready-check/accept"
            requests.post(url, headers=headers, verify=False)
            return "Accepted!"
        elif ready_check == 2:
            return "Waiting for ready check..."
        else:
            return "Not in queue!"

    def create_game_lobby_normal(lcu_data):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        data = '{"queueId":430}'
        url = lcu_data["url"] + "/lol-lobby/v2/lobby/"
        requests.post(url, headers=headers, data=data, verify=False)

    def create_game_lobby_ranked(lcu_data, r1=None, r2=None):
        valid_roles = ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "ULTILITY", "FILL", None]
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        data = '{"queueId":420}'
        url = lcu_data["url"] + "/lol-lobby/v2/lobby/"
        request = requests.post(url, headers=headers, data=data, verify=False)
        if r1.upper() in valid_roles and r2.upper() in valid_roles:
            if r1 != None and r2 != None:
                lcu_api.change_roles(lcu_data, r1, r2)
            elif r1 == None and r2 != None or r1 != None and r2 == None:
                raise ValueError("Please specify 2 roles.")
        else:
            raise ValueError("Roles has to be TOP, JUNGLE, MIDDLE, BOTTOM, ULTILITY or FILL")

    def change_roles(lcu_data, r1, r2):
        auth = xtra.base64encode(lcu_data["auth"])
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": F"Basic {auth}"
        }
        data = '{{"firstPreference": "{}", "secondPreference": "{}"}}'.format(r1.upper(), r2.upper())
        url = lcu_data["url"] + "/lol-lobby/v2/lobby/members/localMember/position-preferences"
        requests.put(url, headers=headers, data=data, verify=False)

class xtra:
    def get_champion_name_by_id(id):
        version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
        champion_id = {}
        champs_req = requests.get(F"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()
        for x in list(champs_req["data"]):
            champ_id = champs_req["data"][x]["key"]
            champion_id[champ_id] = x
        champ_name = champion_id[str(id)]
        return champ_name

    def get_champion_name_by_id_list(id_list):
        version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
        champion_id = {}
        champ_list = []
        champs_req = requests.get(F"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()
        for x in list(champs_req["data"]):
            champ_id = champs_req["data"][x]["key"]
            champion_id[champ_id] = x
        for x in id_list:
            champ_name = champion_id[str(x)]
            champ_list.append(champ_name)
        return champ_list

    def base64encode(text):
        text = base64.b64encode(text.encode("ascii")).decode("ascii")
        return text

    def jprint(json_parsed):
        print(json.dumps(json_parsed, indent=4, sort_keys=True))
