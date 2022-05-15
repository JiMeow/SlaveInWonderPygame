
def resetDictdata(data):
    for key in list(data.keys()):
        data.pop(key)


def setDictdata(dict, data):
    for key in list(data.keys()):
        dict[key] = data[key]


def getDataFromServer(network, player, data):
    newdata = network.send(player)
    resetDictdata(data)
    data["allplayer"] = newdata["allplayer"]


def setDataFromServer(data, allplayer):
    resetDictdata(allplayer)
    setDictdata(allplayer, data["allplayer"])


def countPlayerinRoom(allplayer, room):
    ans = 0
    for id, player in allplayer.items():
        if player.room == room:
            ans += 1
    return ans
