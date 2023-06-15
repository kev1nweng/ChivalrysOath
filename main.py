from os import system as run
import random

version = "1.3.0"


def clearScn():
    run("cls")
    run("clear")
    print("\033c")


# 消息处理
class msgHandler:
    def info(msg):
        print("\n[i] " + msg + "\n")

    def warn(msg):
        print("\n[!] " + msg + "\n")

    def banner(msg):
        clearScn()
        print("\n======== " + msg + " ========\n")

    def title(msg):
        run("title " + msg)


# 初始化玩家列表
playerArray = []
swordsArray = [25, 45, 50, 65, 80]

msgHandler.banner("Chivalry's Oath - 开始")
msgHandler.title("Chivalry's Oath - " + version)

while True:
    try:
        playerCount = int(input("请输入玩家数量\n>> "))
        if playerCount < 2 or playerCount % 2 == 0:
            raise Exception("玩家数量过少或输入非奇数")
        break
    except Exception as e:
        msgHandler.warn(str(e))
        continue

msgHandler.banner("Chivalry's Oath - 玩家设置")

playerArray.append([0, "裁判", 0])
for i in range(playerCount):
    while True:
        try:
            playerArray.append([0, "", 0])
            currentPlayer = playerArray[i + 1]
            currentPlayer[0] = i + 1  # 玩家ID
            currentPlayer[1] = input("\n请输入玩家" + str(i + 1) + "的名字\n>> ")  # 玩家名称
            if currentPlayer[1] == "":
                raise Exception("玩家名字为空")
            currentPlayer[2] = input(
                "\n请输入玩家 " + str(i + 1) + " 选择的剑\n选择范围：25/45/50/65/80/random\n>> "
            )
            if currentPlayer[2] == "random":
                currentPlayer[2] = random.choice(swordsArray)
                print("选出的剑：" + str(currentPlayer[2]))
            currentPlayer[2] = int(currentPlayer[2])
            if not currentPlayer[2] in [25, 45, 50, 65, 80]:
                raise Exception("不合法的剑：超出选择范围")
            # TODO: 重复武器重新分配
            break
        except Exception as e:
            msgHandler.warn(str(e))
            playerArray.remove(currentPlayer)  # 清理错误产生的无效玩家
            continue

msgHandler.banner("Chivalry's Oath")

# 初始化游戏数据
roundCount = 1
deadPlayerCount = 0
gameOver = False

# 主循环
while True:
    for playerOnStage in playerArray:
        roundPass = False
        if playerOnStage[0] == "x" or playerOnStage[0] == 0:
            continue  # 检查玩家是否是裁判或是否死亡，若死亡则选择下一个玩家。
        msgHandler.banner("Chivalry's Oath - 游戏中")
        deadPlayerCount = 0
        for i in range(len(playerArray)):  # 遍历玩家列表，检查游戏是否结束
            if playerArray[i][0] == "x":
                deadPlayerCount -= -1
        if deadPlayerCount >= len(playerArray) - 2:
            winner = playerOnStage
            gameOver = True
            break
        print(f"回合数：{roundCount}")
        print(f"玩家列表：{playerArray}")
        print(f"活动玩家：({playerOnStage[0]}): {playerOnStage[1]} - {playerOnStage[2]}%")
        while True:
            targetPlayerRaw = input("\n请输入要攻击的玩家编号\n(输入 pass 空刀) >> ")
            if targetPlayerRaw == "pass":
                roundPass = True
                break
            try:
                targetPlayerRaw = int(targetPlayerRaw)
                for i in range(len(playerArray)):  # 遍历玩家列表，定位玩家
                    playerLocated = False
                    if playerArray[i][0] == targetPlayerRaw:
                        targetPlayer = playerArray[i]
                        playerLocated = True
                        break
                if targetPlayer[0] == playerOnStage[0]:
                    raise Exception("你不能攻击自己！")
                if playerLocated == False:
                    raise Exception("无效的玩家编号")
                break
            except Exception as e:
                msgHandler.warn(str(e))
                continue
        if roundPass:
            roundCount -= -1
            continue
        attackResult = random.randint(0, 100)
        if playerOnStage[2] > attackResult:
            msgHandler.info(
                f"{attackResult} - 攻击成功：{playerOnStage[1]} 杀死了 {targetPlayer[1]}！"
            )
            targetPlayer[0] = "x"
            input("按下 Enter 开启下一回合\n>>")
        else:
            msgHandler.info(
                f"{attackResult} - 攻击失败：{playerOnStage[1]} 尝试杀死 {targetPlayer[1]} 时挥空了！"
            )
            input("按下 Enter 开启下一回合\n>>")
            roundCount -= -1
    if gameOver:
        break

msgHandler.banner("Chivalry's Oath - 游戏结束")
msgHandler.info(f"游戏结束！赢家是：({winner[0]}): {winner[1]} - {winner[2]}！")

input("按下 Enter 退出游戏。\n>>")

# TODO: 弹反机制
