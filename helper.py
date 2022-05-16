
def resetDictdata(data):
    """
    It takes a dictionary as input and removes all the keys from it

    :param data: The dictionary that you want to reset
    """
    for key in list(data.keys()):
        data.pop(key)


def setDictdata(dict, data):
    """
    It takes a dictionary and a dictionary of data and sets the values of the first dictionary to the
    values of the second dictionary

    :param dict: The dictionary to be updated
    :param data: The data to be added to the dictionary
    """
    for key in list(data.keys()):
        dict[key] = data[key]


def getDataFromServer(network, player, gamestart, data):
    """
    It sends a request to the server, and then it resets the data dictionary and then it sets the data
    dictionary to the new data

    :param network: the network object
    :param player: The player's name
    :param gamestart: a boolean that tells the client if the game has started
    :param data: a dictionary that contains all the data that the server sends to the client
    """
    newdata = network.send({
        "player": player,
        "gamestart": gamestart,
    })
    resetDictdata(data)
    data["allplayer"] = newdata["allplayer"]
    data["gamestart"] = newdata["gamestart"]


def setDataFromServer(data, allplayer):
    """
    It takes a dictionary of dictionaries, and a dictionary of dictionaries, and it sets the values of
    the second dictionary to the values of the first dictionary

    :param data: a dictionary
    :param allplayer: a dictionary of dictionaries
    """
    resetDictdata(allplayer)
    setDictdata(allplayer, data["allplayer"])


def getDataFromServerGame(network, player, gamestart, table, data):
    newdata = network.send({
        "player": player,
        "gamestart": gamestart,
        "table": table,
    })
    resetDictdata(data)
    data["allplayer"] = newdata["allplayer"]
    data["gamestart"] = newdata["gamestart"]
    data["table"] = newdata["table"]
    data["turn"] = newdata["turn"]


def setDataFromServerGame(data, allplayer, table):
    resetDictdata(allplayer)
    setDictdata(allplayer, data["allplayer"])
    setClassTable(table, data["table"])


def setClassTable(table, data):
    if table.value < data.value:
        table.val = data.val
        table.value = data.value
        table.cardtype = data.cardtype
        table.cardcount = data.cardcount
        table.keepcard = data.keepcard
        table.movecordinate = data.movecordinate


def countPlayerinRoom(allplayer, room):
    ans = 0
    for id, player in allplayer.items():
        if player.room == room:
            ans += 1
    return ans
