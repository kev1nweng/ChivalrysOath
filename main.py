from time import sleep
from os import system as run
import random

version = "2.0.0"


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
counterAttackArray = [80, 85, 90, 95, 95]

msgHandler.banner("Chivalry's Oath - 开始")
msgHandler.title("Chivalry's Oath - " + version)
msgHandler.info("Never compromise with your enemies.")

while True:
    try:
        playerCount = int(input("请输入玩家数量\n>> "))
        if playerCount < 2 or playerCount % 2 == 0:
            raise Exception("用学者的话来说：玩家数量过少或输入非奇数")
        break
    except Exception as e:
        msgHandler.warn(str(e))
        continue

msgHandler.banner("Chivalry's Oath - 玩家设置")

playerArray.append([0, "裁判", 0, 0])
for i in range(playerCount):
    while True:
        try:
            msgHandler.banner("Chivalry's Oath - 玩家设置")
            playerArray.append([0, "", 0, 0])
            currentPlayer = playerArray[i + 1]
            currentPlayer[0] = i + 1  # 玩家ID
            currentPlayer[1] = input("\n请输入玩家" + str(i + 1) + "的名字\n>> ")  # 玩家名称
            if currentPlayer[1] == "":
                raise Exception("玩家名字为空…… 这是最后记住他们名字的机会了。")
            currentPlayer[2] = input(
                "\n请输入玩家 " + str(i + 1) + " 选择的剑\n选择范围：25/45/50/65/80/random\n>> "
            )
            if currentPlayer[2] == "random":
                currentPlayer[2] = random.choice(swordsArray)
                print("选出的剑：" + str(currentPlayer[2]))
            currentPlayer[2] = int(currentPlayer[2])
            if not currentPlayer[2] in [25, 45, 50, 65, 80]:
                raise Exception("不合法的剑：看来你的选择犹如你的人生一样不够明智")
            for selectedSword in swordsArray:
                if currentPlayer[2] == selectedSword:
                    currentPlayer[3] = counterAttackArray[i]
            break
        except Exception as e:
            msgHandler.warn(str(e))
            playerArray.remove(currentPlayer)  # 清理错误产生的无效玩家
            continue

playerSwordArray = []
for k in range(len(playerArray)):
    playerSwordArray.append(playerArray[k][2])

if len(playerSwordArray) != len(set(playerSwordArray)):
    msgHandler.banner("Chivalry's Oath - 重复的剑")
    msgHandler.info("注意，注意！有玩家选择了重复的剑！让我们看看祝福之泉会赋予他们什么宝物：")
    for x in range(len(playerSwordArray)):
        for y in range(x + 1, len(playerSwordArray)):
            if playerSwordArray[x] == playerSwordArray[y]:
                playerSwordArray[y] = random.choice(swordsArray)
    for t in range(len(playerSwordArray)):
        playerArray[t][2] = playerSwordArray[t]
    print("\n", playerArray)
    input("\n按下 Enter 确认并开始游戏\n>>")


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
                    raise Exception("自杀是不被允许的……")
                if playerLocated == False:
                    raise Exception("无效的玩家编号，你确定你的眼神还好吗？")
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
                f"{attackResult} - 攻击成功：{playerOnStage[1]} 让 {targetPlayer[1]} 鲜血满地！"
            )
            targetPlayer[0] = "x"
            input("按下 Enter 开启下一回合\n>>")
        else:
            msgHandler.info(
                f"{attackResult} - 攻击失败：{playerOnStage[1]} 尝试杀死 {targetPlayer[1]} 时挥空了！"
            )
            sleep(0.2)
            if attackResult >= targetPlayer[3]:
                msgHandler.info(
                    f"转折点：{playerOnStage[1]} 尝试杀死 {targetPlayer[1]} 时触发了 TA 的求生本能，现在是，反击时间！"
                )
                sleep(0.5)
                counterAttackResult = random.randint(0, 100)
                if targetPlayer[2] < counterAttackResult:
                    msgHandler.info(
                        f"{playerOnStage[1]} 居然被 {targetPlayer[1]} 反杀…… 有趣啊……"
                    )
                    playerOnStage[0] = "x"
                else:
                    msgHandler.info(
                        f"{playerOnStage[1]} 安然无恙…… 暂时的。不知道 {targetPlayer[1]} 是否会伺机寻仇呢？"
                    )
            input("按下 Enter 开启下一回合\n>>")
            roundCount -= -1
    if gameOver:
        break

msgHandler.banner("Chivalry's Oath - 游戏结束")
msgHandler.info(f"游戏结束！浴血的那位赢家是：({winner[0]}): {winner[1]} - {winner[2]}！")

input("按下 Enter 退出游戏。…… 你真的退出了…… 吗？\n>>")
