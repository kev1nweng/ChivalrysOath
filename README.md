
# 🗡 Chivalry's Oath

Chivalry's Oath（骑士誓言）：一个简单而有趣的逻辑游戏。

## 🎮 玩法

### 规则目录

1. 准备阶段
2. 宣言阶段
3. 战斗阶段
4. 结算阶段
5. 其他

### 1. 准备阶段

> “是你把我引上了这条道路，而现在……你却想置身事外，站在了我的对立面！最终当黑暗带走我时……我一无所有……”——引子

玩家个数为5个，此外有1人作为裁判。（电子游戏中可以自定义玩家人数——但玩家必须是奇数个。）

> “诸位骑士，昔日乃是帝国之精英，今日却沦落至奴隶之地，嗟乎嗟乎！”

每名玩家根据上一局的排名安排位次（第一局可以根据姓氏首字母），并依次秘密地和裁判选择自己的武器。

> “现在，你们必须做出生死决斗，无论是曾经的敌人还是朋友……哈哈哈哈……侍卫，拿武器来！”

武器的击杀率不同，分为：25%，45%，50%，65%，80%。

> “短剑、单手剑、长剑、骑枪与重锤……想想哪一件最趁手，最能让你的敌人发出骨头折断的清脆声……”

如果有2人及以上选择了同一件武器，这些玩家将被重新随机分配武器。

直到第一轮结束，裁判不能告诉玩家武器品质，以及何人武器被更换——这意味着即使一位玩家的武器被重新分配，他/她本人也不能在第一轮结束前得知。

> “武器不够？哦，我忠诚的刽子手、冷漠的执行官，收起你残存的怜悯，拿出你往日的高贵……让他们慢慢厮杀。”

玩家可以选择不选择武器，由裁判随机决定。这个场合，裁判随机完成后会立刻将结果公布给所有玩家。

> “恐惧命运，于是交给祝福之泉吗……也好……嘿嘿……骑士啊，命运为你选择了（武器名）！”

### 2. 宣言阶段

每位玩家自行宣布自己的武器品质，此时可以说实话或者欺骗他人。

规则上宣言顺序为位次顺序，但玩家可以拒绝宣言。

> “开诚布公，开诚布公，快些，快些。这是你们最后诉衷肠的机会咯。”

### 3. 战斗阶段

当一轮间无人出刀，全员宣告失败。

> “嘿，可怜的老牛们，如果你们在一轮之间过度慈悲，那么……一个都别想走出来！”

因此，玩家在攻击宣言时可以选择故意挥空武器。

> “惹人厌的臭虫，自以为是的慈悲……我要看到血流成河！”

玩家按照位次顺序逐个对其他玩家攻击宣言（或者空刀），死掉的玩家则跳过。

按照玩家选择的武器品质，使用1-100的随机函数计算，被攻击对象大于其概率数字则存活，小于等于其概率数字则死亡。

> “好啊，好啊，你做的好！我已经闻到血的味道了，简直是这世上最佳的愉悦！”

当一位玩家在受攻击后没有死亡，且对方随机出的数值小于等于（100-弹反率数字），能够触发弹反。此时，弹反者反攻攻击者，伤害规则适用上文的随机函数算法。

80%武器与65%武器弹反率为5%，50%武器弹反率为10%，45%武器弹反率为15%，25%武器弹反率为20%。

例如：45%武器攻击25%武器，伤害数字为92，100-92≤20，则触发弹反。弹反时，25%武器打出的伤害数字为17，则45%武器的持有者死亡；反之弹反失败，轮到下一位操作。

> “就像这样，垂死挣扎！真是太自觉了，无论哪边死亡都将带给我极大的愉悦。”

### 4. 结算阶段

每轮结束后进行结算，裁判重申在本轮中活下来的玩家。

第一轮结束后，裁判公布所有玩家各自的武器品质，其后的结算阶段可以玩家可以复核各位玩家的武器品质。

> “小心点……可别让你的尸体在这里腐烂咯……呵呵呵呵……”

### 5. 其他

- 每位玩家可以在战斗阶段为其他玩家分析逻辑，这对于各位玩家来说可能都是一种合适的礼节。
- 玩家之间可以结盟，但任意一方可以随时撕毁盟约。
- 遵守规则，愉快决斗，友谊第一，比赛第二！
