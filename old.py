#Hit As Why 鸡游戏 1.0
#所有代码都是覃菜一个人写的
import random

print("正在开始 Hit As Why（$$B）鸡游戏")
player_blood = 100
SYG_blood = 100
print("此游戏需要数字来攻击对手")
killing_SYG_list = ["挑衅", "跳科目三", "Level !", "JJBoom", "咩", "14524", "SB"]
Beat_list = [10, 10, 10, 10, 10, 10, 50]
a = 0
for i in Beat_list:
    print("输入%d发射%s必杀技,攻击力%d" % (a, killing_SYG_list[a], i))
    a = a + 1
while True:
    Boom = int(input("请输入你要发射的必杀技的编号"))
    a = Beat_list[Boom] + random.randint(1, 10)
    SYG_blood -= a
    if SYG_blood <= 0:
        print("恭喜你,你打败了SYG!")
        input("按Enter键继续")
        break
    print("你打出了%d格的攻击,$$B的剩余血量为%d滴" % (a, SYG_blood))
    a = random.randint(1, 10) + 10
    player_blood -= a
    if player_blood <= 0:
        print("真遗憾,你被SYG打败了!")
        input("按Enter键继续")
        break
    print("SYG发动了%d格反击,你的剩余血量为%d滴" % (a, player_blood))
