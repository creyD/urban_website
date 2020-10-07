# For communication with the Steam API
import urllib.request
import json
# For database handling (importing from Django Models)
from .models import S_Users, S_UserGames, S_Games
# For getting the STEAM_API_KEY
from django.conf import settings
# For storing the API call limit
import os
# For flagging the daily API call limit
from datetime import datetime


# GLOBAL VARIABLES - API URLS
API_START = 'http://api.steampowered.com/'
API_KEY = str(settings.STEAM_API_KEY)
API_END_SIN = '&steamid='
API_END_PLU = '&steamids='
API_END_URL = '&vanityurl='

API_COMMAND_PLAYER = 'ISteamUser/GetPlayerSummaries/v0002/?key='
API_COMMAND_FL = 'ISteamUser/GetFriendList/v0001/?key='
API_COMMAND_GAMES = 'IPlayerService/GetOwnedGames/v0001/?key='
API_COMMAND_GAMES_ALL = 'ISteamApps/GetAppList/v0002/?key='
API_COMMAND_RESOLVEURL = 'ISteamUser/ResolveVanityURL/v0001/?key='

API_QUERY_PLAYER = API_START + API_COMMAND_PLAYER + API_KEY + API_END_PLU
API_QUERY_FRIENDLIST = API_START + API_COMMAND_FL + API_KEY + API_END_SIN
API_QUERY_GAMES = API_START + API_COMMAND_GAMES + API_KEY + API_END_SIN
API_QUERY_ALL_GAMES = API_START + API_COMMAND_GAMES_ALL + API_KEY
API_QUERY_RESOLVEURL = API_START + API_COMMAND_RESOLVEURL + API_KEY + API_END_URL

# ------------------------------------------------------------
# ------------- HELPER FUNCTIONS -----------------------------
# -------(not called by anything except this library) --------
# ------------------------------------------------------------


# Writes the API_QUOTA variable in a file
def saveAPIquota():
    date = datetime.today().strftime('%Y-%m-%d')
    file = open(os.path.join(str(settings.BASE_DIR),
                             'API_QUOTA_' + str(date)), 'w+')
    file.write(str(API_QUOTA))
    file.close()
    return 0


# Checks the API quota and adds one if it's not over the limit yet
def checkAPIquota():
    global API_QUOTA

    if API_QUOTA < 100000:
        API_QUOTA += 1
        return 0
    else:
        saveAPIquota()
        exit()
        return 1


# Reads the current API quota for the day from a save file
def readAPIquota():
    date = datetime.today().strftime('%Y-%m-%d')
    try:
        file = open(os.path.join(
            str(settings.BASE_DIR), 'API_QUOTA_' + date), 'r')
        API_QUOTA = int(file.readline())
        file.close()
        if API_QUOTA > 100000:
            exit()
        return API_QUOTA
    except IOError:
        return 0


# Daily limit of API calls
API_QUOTA = readAPIquota()


# Returns a draft of a user without actually writing it to the database
def draftPlayer(player_object, mode):
    if mode == 1:
        return S_Users(steamID=player_object['steamid'])
    elif mode == 2:
        return S_Users(
            steamID=player_object['steamid'],
            s_profilestate=(
                True if 'profilestate' in player_object else False),
            s_loccountrycode=(
                player_object['loccountrycode'] if 'loccountrycode' in player_object else False),
            s_timecreated=(
                player_object['timecreated'] if 'timecreated' in player_object else False),
            s_primaryclanid=(
                player_object['primaryclanid'] if 'primaryclanid' in player_object else False),
            s_personaname=(
                player_object['personaname'] if 'personaname' in player_object else False),
            s_profileurl=(player_object['profileurl']
                          if 'profileurl' in player_object else False)
        )
    return 0


# Creates a player in the database from a player_object, if they don't already exist
def createPlayer(player_object, mode):
    if mode == 1:
        S_Users.objects.get_or_create(steamID=player_object['steamid'])
    elif mode == 2:
        S_Users.objects.get_or_create(
            steamID=player_object['steamid'],
            s_profilestate=(
                True if 'profilestate' in player_object else False),
            s_loccountrycode=(
                player_object['loccountrycode'] if 'loccountrycode' in player_object else False),
            s_timecreated=(
                player_object['timecreated'] if 'timecreated' in player_object else False),
            s_primaryclanid=(
                player_object['primaryclanid'] if 'primaryclanid' in player_object else False),
            s_personaname=(
                player_object['personaname'] if 'personaname' in player_object else False),
            s_profileurl=(player_object['profileurl']
                          if 'profileurl' in player_object else False)
        )
    return 0


# Updates player in the database to new information (Get -> Update -> Save)
def updatePlayer(player_object):
    if 'steamid' in player_object:
        player = S_Users.objects.get(steamID=player_object['steamid'])

        player.s_profilestate = (
            True if 'profilestate' in player_object else False)
        player.s_loccountrycode = (
            player_object['loccountrycode'] if 'loccountrycode' in player_object else False)
        player.s_timecreated = (
            player_object['timecreated'] if 'timecreated' in player_object else False)
        player.s_primaryclanid = (
            player_object['primaryclanid'] if 'primaryclanid' in player_object else False)
        player.s_personaname = (
            player_object['personaname'] if 'personaname' in player_object else False)
        player.s_profileurl = (
            player_object['profileurl'] if 'profileurl' in player_object else False)

        player.save(update_fields=['s_profileurl', 's_personaname',
                                   's_primaryclanid', 's_timecreated', 's_loccountrycode', 's_profilestate'])
    return 0


# Get the information from the Steam API for a certain steamid
def getPlayer(steamid, mode):
    if mode == 1:
        createPlayer({'steamid': steamid}, mode)
    elif mode == 2:
        if 0 == checkAPIquota():
            try:
                player_object = json.load(urllib.request.urlopen(
                    API_QUERY_PLAYER + str(steamid)))
                createPlayer(player_object['response']['players'][0], mode)
            except urllib.error.HTTPError:
                return 1
    return 0


# Imports a list of steamids to the database, uses bulk creation if possible
def getPlayers(steamid_list, mode):
    # For better performance and stability only keep unique values in this list
    steamid_list = set(steamid_list)
    player_cache = []

    if mode == 1:
        # For simple mode getPlayers just takes the steamids and creates the players in the database
        for steamid in steamid_list:
            player_cache.append(
                draftPlayer(
                    {'steamid': steamid},
                    mode
                )
            )

    elif mode == 2:
        # For extended mode getPlayers creates a query for the Steam API to get the playerobjects for all the steamids
        if 0 == checkAPIquota():
            try:
                query = API_QUERY_PLAYER + \
                    ','.join(str(steamid) for steamid in steamid_list)
                players_object = json.load(urllib.request.urlopen(query))

                for player_object in players_object['response']['players']:
                    player_cache.append(
                        draftPlayer(player_object, mode)
                    )

            except urllib.error.HTTPError:
                # If there are errors with as little as one steamID in the list then check them seperately (slower, but only the problem will be left out)
                for steamid in steamid_list:
                    getPlayer(steamid, mode)
                return 0

    S_Users.objects.bulk_create(player_cache, ignore_conflicts=True)
    return 0


# Gets the friendlist of a certain player
def getFriends(steamid, mode):
    try:
        if 0 == checkAPIquota():
            # For both modes this just creates a query for the friendlist of a steamid and from that it checks the friends into the database
            checklist, friendlist = [], json.load(urllib.request.urlopen(
                API_QUERY_FRIENDLIST + str(steamid) + '&relationship=friend'))

            for friend in friendlist['friendslist']['friends']:
                checklist.append(str(friend['steamid']))
            getPlayers(checklist, mode)

            if mode == 5:
                return checklist

    except urllib.error.HTTPError:
        return 1
    return 0


# Get the games for a certain steamid and save them in the S_UserGames database
# Hint: s_gameCount can have 3 status: -1: No API response, 0: Empty API response, any number: number of games
def getGames(player):
    try:
        if 0 == checkAPIquota():
            library = json.load(urllib.request.urlopen(
                API_QUERY_GAMES + str(player.steamID) + '&format=json'))

            # If the user doesn't share their library then the response is empty
            if 'game_count' in library['response']:
                # Update Game Count for the player
                player.s_gameCount, gamesArray = library['response']['game_count'], [
                ]
                for entry in library['response']['games']:
                    game = S_Games.objects.get_or_create(gameID=entry['appid'])
                    # Create User - Game Relation
                    gamesArray.append(
                        S_UserGames(
                            user=player,
                            game=game[0],
                            hours=entry['playtime_forever']
                        )
                    )
                S_UserGames.objects.bulk_create(
                    gamesArray, ignore_conflicts=True)
            else:
                player.s_gameCount = 0
    except urllib.error.HTTPError:
        player.s_gameCount = -1

    player.save(update_fields=['s_gameCount'])
    return 0


# Checks if a given variable is an int or not
def checkInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Checks a custom steam url and returns the steamID or False
def checkCustomURL(url):
    if 0 == checkAPIquota():
        try:
            name = json.load(urllib.request.urlopen(
                API_QUERY_RESOLVEURL + str(url)))
            return (name['response']['steamid'] if name['response']['success'] == 1 else False)
        except urllib.error.HTTPError:
            return False
    else:
        return False


# Converts a given input to a valid steam ID or False
def getSteamID(input_value):
    # i. e. 76561198090620481
    if checkInt(input_value):
        return input_value

    # i. e. https://steamcommunity.com/id/creyD or https://steamcommunity.com/profiles/76561198090620481/
    elif (input_value.startswith('http') or input_value.startswith('steam')):
        # https://steamcommunity.com/profiles/76561198090620481/
        if 'profiles' in input_value:
            # https://steamcommunity.com/profiles/76561198090620481/
            if input_value.endswith('/'):
                return input_value[-18:-1]
            # https://steamcommunity.com/profiles/76561198090620481
            else:
                return input_value[-17:]
        # https://steamcommunity.com/id/creyD
        if 'id' in input_value:
            # https://steamcommunity.com/id/creyD/
            temp_split = input_value.split('/')
            if input_value.endswith('/'):
                return checkCustomURL(temp_split[-2])
            # https://steamcommunity.com/id/creyD
            else:
                return checkCustomURL(temp_split[-1])
        return False

    # i. e. creyd
    else:
        return checkCustomURL(input_value)
    return False


# ------------------------------------------------------------
# ------------- PUBLIC FUNCTIONS -----------------------------
# -------(called by anything except this library) ------------
# ------------------------------------------------------------

# Updates all player info in the database (if no data is filled in for the player)
# Note: .count() doensn't work here as it seems to count live and influences the length of the range() therefore
def updateAllPlayers(pipe):
    userlist = S_Users.objects.filter(
        s_profileurl__isnull=True).values_list('steamID', flat=True)
    for i in range(int(len(userlist) / 100) + 1):
        if 0 == checkAPIquota():
            query = API_QUERY_PLAYER + \
                ','.join(str(user)
                         for user in userlist[int(i * 100):int((i + 1) * 100 - 1)])
            players_object = json.load(urllib.request.urlopen(query))

            for player in players_object['response']['players']:
                updatePlayer(player)

    saveAPIquota()
    pipe.nextStep()
    return 0


# Gets the games for each person in the S_Users table which doesn't already have a gamecount
def updateGames(pipe):
    userlist = S_Users.objects.filter(s_gameCount__isnull=True)
    for user in userlist:
        getGames(user)

    saveAPIquota()
    pipe.nextStep()
    return 0


# Gets the names for all games in S_Games table
def getAllGames(pipe):
    if 0 == checkAPIquota():
        # Getting the official list of all steam games
        gamelist = json.load(urllib.request.urlopen(API_QUERY_ALL_GAMES))

        # If initial games crawing we can use bulk creation bcs of no duplicates
        if S_Games.objects.count() == 0:
            games_cache = []
            for game in gamelist['applist']['apps']:
                games_cache.append(
                    S_Games(gameID=game['appid'], gameName=game['name']))
            S_Games.objects.bulk_create(games_cache, ignore_conflicts=True)
        else:
            for game in gamelist['applist']['apps']:
                S_Games.objects.get_or_create(
                    gameID=game['appid'], gameName=game['name'])

    saveAPIquota()
    pipe.nextStep()
    return 0


def crawl(startID, depth, pipe, mode):
    # 1 - Simple Crawl, 2 - Extensive Crawl, 3 - Crawl one level (simple), 4 - Crawl one level (extensive)
    CURRENT = list(S_Users.objects.all().values_list('steamID', flat=True))

    if (mode == 1 or mode == 2):
        # Mode 1 is a basic snowball crawler: for each step in depth it goes over the users in the database and gets their friends
        # Mode 2 is an extensive mode similar to the first mode

        getPlayer(str(startID), mode)
        for __ in range(depth):
            snapshot = S_Users.objects.all().values_list('steamID', flat=True)
            for userid in snapshot:
                if userid not in CURRENT:
                    getFriends(userid, mode)
                    CURRENT.append(userid)
            pipe.nextStep()

    elif (mode == 3 or mode == 4):
        # Mode 3 + 4 crawl one level with either extensive or simple mode on
        pipe.pipe_steps = 1
        pipe.save(update_fields=['pipe_steps'])

        for userid in CURRENT:
            getFriends(userid, mode - 2)
        pipe.nextStep()

    elif (mode == 5):
        idList = []
        failsafecounter = 0
        visitedIDs = []
        currentID = startID
        for __ in range(depth):
            newFriends = getFriends(currentID, 5)
            visitedIDs.append(currentID)
            if newFriends != 1:
                for item in newFriends:
                    if item not in idList:
                        idList.append(item)
            currentID = idList[-1]

            if currentID in visitedIDs:
                currentID = idList[1 + failsafecounter]
                failsafecounter = failsafecounter + 1

        for item in idList:
            createPlayer({'steamid': item}, 1)

        pipe.nextStep()
    saveAPIquota()
    return 0


# Gets Steam Accounts for a string of semicolon separated names
def getSteamIDs(string):
    error, players, steam64IDarray = False, string.split(';'), []

    for player in players:
        extractedSteamID = getSteamID(player)
        if extractedSteamID:
            steam64IDarray.append(extractedSteamID)
        else:
            error = True

    return steam64IDarray, error


# Returns an array of appids of games any given list of players has in common
# Hint: Input format "123456 123456 123456", all Steam64IDs
def getCommonGames(steamid_list):
    error = False
    steamIDlist, error = getSteamIDs(steamid_list)
    getPlayers(steamIDlist, 1)

    guys = [S_Users.objects.get(steamID=player) for player in steamIDlist]
    commonGames = []

    for player in guys:
        getGames(player)

    for player in guys:
        if len(commonGames) > 0:
            commonGames = commonGames.intersection(
                S_UserGames.objects.filter(user=player).values_list('game', flat=True))
        else:
            commonGames = S_UserGames.objects.filter(
                user=player).values_list('game', flat=True)

    gameInfoArray = []
    for game in commonGames:
        gameInfoArray.append([S_Games.objects.get(
            gameID=game).gameName, S_Games.objects.get(gameID=game).gameID])

    return gameInfoArray, error, guys
