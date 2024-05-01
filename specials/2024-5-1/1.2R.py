#Hit As Why 鸡游戏 1.4，ReHitssb 1.2R
#所有代码都是覃菜一个人写的
#这是由绵羊制作的重写版
#这个版本包含商店
import random
from time import sleep

print("正在开始 Hit As Why（$$B）鸡游戏")
player_blood = random.randint(100,200)
SYG_blood = random.randint(100,200)
print("此游戏需要数字来攻击对手")
killing_SYG_list = ["挑衅", "跳科目三", "Level !", "JJBoom", "咩", "14524", "SB", "打开商店"]
Beat_list = [random.randint(3,8), random.randint(3,8), random.randint(8,13), random.randint(8,15), random.randint(3,8), random.randint(5,10), random.randint(4,10), 0]
Score_list = [random.randint(100,200), random.randint(100,200), random.randint(100,200), random.randint(100,200), random.randint(100,200), random.randint(200,250), 0]
Buy_list = ["双倍攻击","盾牌(被攻击时血量+5)","我也是有底线的(追击时在进行3格攻击)","回血药水"]
Need_score_list = [random.randint(250,350),random.randint(100,200),random.randint(100,200),random.randint(100,200)]
a = 0
b = 1
score = 0
ascore = 0
doubleKill = False
dunpai = False
dx = False
while True:
    a = 0
    print("---------回合%d----------" % b)
    for i in Beat_list:
        print("输入%d发射%s必杀技,攻击力%d,使用后$$b血量%d" % (a, killing_SYG_list[a], i, SYG_blood - Beat_list[a]))
        a = a + 1
    Boom = int(input("请输入你要发射的必杀技的编号"))
    if Boom == 7:
        print("----------商店---------")
        a = 0
        for i in Buy_list:
            print("输入%d购买%s商品,需要%d分" % (a, i, Need_score_list[a]))
            a += 1
        aaa = int(input("请输入你要购买的商品,999取消"))
        if aaa == 999:
            continue
        ascore -= Need_score_list[aaa]
        if aaa == 0:
            print("购买成功!剩余%d分" % ascore)
            doubleKill = True
            continue
        if aaa == 1:
            print("购买成功!剩余%d分" % ascore)
            dunpai = True
            continue
        if aaa == 2:
            print("购买成功!剩余%d分" % ascore)
            dx = True
            continue
        if aaa == 3:
            print("购买成功!剩余%d分" % ascore)
            print("血量已增加3")
            continue
    ascore += Score_list[Boom]
    score += Score_list[Boom]
    a = Beat_list[Boom] + random.randint(1, 10)
    SYG_blood -= a
    if SYG_blood <= 0:
        print("恭喜你,你打败了SYG!")
        input("按Enter键继续")
        break
    print("<我方行动>你打出了%d格的攻击" % a)
    if doubleKill == True:
        sleep(1)
        print("<行动加成>你购买了双倍攻击,所以攻击翻倍!")
        SYG_blood -= a
    if score >= 300:
        sleep(1)
        score = 0
        beat = random.choice(Beat_list[0:5])
        print("<我方行动>你发动了追击,打出了%d格伤害" % beat)
        if dx == True:
            sleep(1)
            print("<行动加成>你发动了额外追击，打出了3格伤害，共%d格伤害" % beat + 3)
        SYG_blood -= beat
    sleep(1)
    a = random.randint(1, 10) + 10
    player_blood -= a
    print("<对方行动>$$B进行了反击并打出了%d格攻击" % a)
    if dunpai == True:
        sleep(1)
        print("<我方防御>$$B对你的伤害-5!")
        player_blood += 5
    if player_blood <= 0:
        print("真遗憾,你被SYG打败了!")
        input("按Enter键继续")
        break
    back = random.randint(1, 3)
    if back == 3:
        sleep(1)
        backa = random.choice(Beat_list[0:5])
        print("<对方行动>SYG生气了并发动了追击,打出了%d格伤害" % backa)
        if dunpai == True:
            sleep(1)
            print("<我方防御>真遗憾，盾牌对此次反击无效!")
    sleep(1)
    print("$$B的剩余血量为%d滴" % SYG_blood)
    print("你的剩余血量为%d滴" % player_blood)
    print("你的分数为%d,总分数为%d" % (score, ascore))
    sleep(1)
    a = 0
    b = b + 1
