# LCU Python Wrapper
I am currently working on a LCU API wrapper for Python it is far from good or complete just started working on it!
As soon as I made some real progress I will add a documantation. If anyone has a request send me an email here: nobotsforshit@gmail.com

Following functions are already implemented:

lcu_data means u have to put in the lcu data dictionary what comes from calling lcuconnector.connect(lockfilepath)

target is for the get_current_summoner function
# Valid targets:
```
levelPercentNext = percent to next level up
accountId = current user account id
displayName = Current users displayed name
profileIconId = Gets the id of the profile icon
puuid = returns Player Universally Unique Identifiers for ur account
rerollPoints = Gets current rerollPoints
summonerId = Gets users summonerId
summonerLevel = Get current summoner level
xpSinceLastLevel = Get the amount of xp gotten since last levelup
xpUntilNextLevel = Get the amount of xp needed for next level up
```

# Valid roles:
It isn't important if u make it upper or lower case.
```text
TOP
JUNGLE
MIDDLE
BOTTOM
ULTILITY
FILL
```

# Current functions:

```python
help(lcu_data)
get_current_summoner(lcu_data, target)
get_current_summoner_jwt(lcu_data) # Gets the current summoner JSON Web token
get_current_summoner_background_skin_id(lcu_data) # Gets current summoner background id
get_account_verified(lcu_data) # checks if account is verified
get_current_summoner_recently_played_champions_raw(lcu_data) # gets the "raw" json data for the recently played champions
get_current_summoner_recently_played_champions_ids(lcu_data) # gets the ids of the recently played champs
get_current_summoner_recently_played_champions_names(lcu_data) # gets the names of the recently played champs
get_recently_played_with_summoners_raw(lcu_data) # gets the raw data about the summoners you recently played with
get_recently_played_with_summoners_name(lcu_data) # gets the names of the players you recently played with
get_recently_played_with_summoners_name_champ(lcu_data) # gets the players you played with recently names and champions 
get_current_summoner_in_queue(lcu_data) # gets if current summoner is in queue
get_current_summoner_ready_check(lcu_data) # gets if current summoner is in ready check
auto_accept_current_ready_check(lcu_data) # post the command to accept request if summoner is in ready check
create_game_lobby_ranked(lcu_data, role1, role2)
change_roles(lcu_data, role1, role2)
```
