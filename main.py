#Hit As Why 鸡游戏 1.2，ReHitssb 1.0
#所有代码都是覃菜一个人写的
#这是由绵羊制作的重写版
import random
import os
from time import sleep

print("正在开始 Hit As Why（$$B）鸡游戏")
player_blood = 100
SYG_blood = 100
print("此游戏需要数字来攻击对手")
killing_SYG_list = ["挑衅", "跳科目三", "Level !", "JJBoom", "咩", "14524", "SB"]
Beat_list = [5, 3, 10, 12, 5, 8, 10, 0]
Score_list = [100, 100, 100, 100, 100, 200]
a = 0
b = 1
score = 0
ascore = 0
while True:
    print("---------回合%d----------" % b)
    for i in Beat_list:
        print("输入%d发射%s必杀技,攻击力%d,使用后$$b血量%d" % (a, killing_SYG_list[a], i, SYG_blood - Beat_list[a]))
        a = a + 1
    Boom = int(input("请输入你要发射的必杀技的编号"))
    ascore += Score_list[Boom]
    score += Score_list[Boom]
    a = Beat_list[Boom] + random.randint(1, 10)
    SYG_blood -= a
    if SYG_blood <= 0:
        print("恭喜你,你打败了SYG!")
        input("按Enter键继续")
        break
    print("<我方行动>你打出了%d格的攻击" % a)
    if score >= 300:
        sleep(1)
        score = 0
        beat = random.choice(Beat_list[0:5])
        print("<我方行动>你发动了追击,打出了%d格伤害" % beat)
        SYG_blood -= beat
    sleep(1)
    a = random.randint(1, 10) + 10
    player_blood -= a
    print("<对方行动>$$B进行了反击并打出了%d格攻击" % a)
    if player_blood <= 0:
        print("真遗憾,你被SYG打败了!")
        input("按Enter键继续")
        break
    back = random.randint(1, 3)
    if back == 3:
        sleep(1)
        backa = random.choice(Beat_list[0:5])
        print("<对方行动>SYG生气了并发动了追击,打出了%d格伤害" % backa)
    sleep(1)
    print("$$B的剩余血量为%d滴" % SYG_blood)
    print("你的剩余血量为%d滴" % player_blood)
    print("你的分数为%d,总分数为%d" % (score, ascore))
    sleep(1)
    a = 0
    b = b + 1

