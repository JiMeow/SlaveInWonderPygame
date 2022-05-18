
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


def getDataFromServerGame1(network, player, gamestart, table, data):
    """
    It sends a request to the server, and then it receives a response from the server

    :param network: the network object
    :param player: The player's name
    :param gamestart: boolean, if the game has started
    :param table: the table of the game
    :param data: a dictionary that contains all the data that the server sends to the client
    """
    newdata = network.send({
        "player": player,
        "gamestart": gamestart,
        "table": table,
        "gamestate": "phrase1",
    })

    resetDictdata(data)
    data["allplayer"] = newdata["allplayer"]
    data["gamestart"] = newdata["gamestart"]
    data["table"] = newdata["table"]
    data["turn"] = newdata["turn"]


def setDataFromServerGame1(data, allplayer, table):
    """
    It takes a dictionary of dictionaries, and a dictionary of classes, and copies the data from the
    dictionary of dictionaries into the dictionary of classes

    :param data: a dictionary of all the data from the server
    :param allplayer: a dictionary of all players in the game
    :param table: a class that contains all the data for the table
    """
    resetDictdata(allplayer)
    setDictdata(allplayer, data["allplayer"])
    setClassTable(table, data["table"])


def getDataFromServerGame2(network, player, gamestart, table, data):
    """
    It sends a request to the server, and then it receives a response from the server

    :param network: the network object
    :param player: The player's name
    :param gamestart: boolean, if the game has started
    :param table: the table of the game
    :param data: a dictionary that contains all the data that the server sends to the client
    """
    newdata = network.send({
        "player": player,
        "gamestart": gamestart,
        "table": table,
        "gamestate": "phrase2",
    })

    resetDictdata(data)
    data["allplayer"] = newdata["allplayer"]
    data["gamestart"] = newdata["gamestart"]
    data["table"] = newdata["table"]
    data["turn"] = newdata["turn"]
    data["winner"] = newdata["winner"]


def setDataFromServerGame2(data, allplayer, table, winnerfromlastgame):
    """
    It takes a dictionary of dictionaries, and a dictionary of classes, and copies the data from the
    dictionary of dictionaries into the dictionary of classes

    :param data: a dictionary of all the data from the server
    :param allplayer: a dictionary of all players in the game
    :param table: a class that contains all the data for the table
    """
    resetDictdata(allplayer)
    setDictdata(allplayer, data["allplayer"])
    setClassTable(table, data["table"])
    setListdata(winnerfromlastgame, data["winner"])


def setClassTable(table, data):
    """
    If the value of the table is less than the value of the data, then set the value of the table to the
    value of the data

    :param table: The table that the data is being set to
    :param data: The data that is being passed in
    """
    if table.cardcount <= data.cardcount:
        table.val = data.val
        table.value = data.value
        table.cardtype = data.cardtype
        table.cardcount = data.cardcount
        table.keepcard = data.keepcard
        table.movecordinate = data.movecordinate
        table.whopass = data.whopass


def setListdata(list, data):
    """
    It takes a list and a dictionary of dictionaries, and it sets the values of the list to the values
    of the dictionary

    :param list: a list
    :param data: a dictionary of dictionaries
    """
    while(len(list) > 0):
        list.pop(0)
    for i in range(len(data)):
        list.append(data[i])


def countPlayerinRoom(allplayer, room):
    """
    It counts the number of players in a room

    :param allplayer: a dictionary of all players in the game
    :param room: the room you want to count the players in
    :return: The number of players in a room.
    """
    ans = 0
    for id, player in allplayer.items():
        if player.room == room:
            ans += 1
    return ans
