from os import system as run

version = "1.2.0"


def clearScn():
    run("cls")
    run("clear")
    print("\033c")


class msgHandler:
    def info(msg):
        print("\n[i] " + msg + "\n")

    def warn(msg):
        print("\n[!] " + msg + "\n")

    def banner(msg):
        clearScn()
        print("\n======== " + msg + " ========")

    def title(msg):
        run("title " + msg)


playerArray = []

msgHandler.banner("Chivary's Oath")
msgHandler.title("Chivary's Oath - " + version)

while True:
    try:
        playerCount = int(input("\n请输入玩家数量\n>> "))
        if playerCount < 2 or playerCount % 2 == 0:
            raise ValueError
        break
    except ValueError:
        msgHandler.warn("非法输入值（玩家数量过少或输入非奇数）")
        continue

msgHandler.banner("Chivary's Oath")

playerArray.append([0, "裁判"])
for i in range(playerCount):
    while True:
        try:
            playerArray.append([0, ""])
            playerArray[i + 1][0] = i + 1
            playerArray[i + 1][1] = input("\n请输入玩家" + str(i + 1) + "的名字\n>> ")
            if playerArray[i + 1][1] == "":
                raise ValueError
            break
        except ValueError:
            msgHandler.warn("非法输入值（玩家名字为空）")
            continue

msgHandler.banner("Chivary's Oath")

print("\n玩家名单\n", playerArray, sep="")

# TODO: 游戏主要逻辑