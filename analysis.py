game1_low = [['4228', '9969', '42554'],
['5019', '10993', '50750'],
['5660', '11833', '59730']]

game2_low = [['4868', '10770', '53921'],
['5881', '11822', '63881']]

game3_low = [['4506', '10529', '52414'],
['5485', '11474', '56715']]

game4_low = [['4929', '11167', '58965'],
['6018', '11850', '68787'],
['6749', '12761', '78262']]

game5_low = [['4628', '11493', '63139'],
['7065', '13541', '76978'],
['7637', '14096', '83972'],
['7633', '14083', '83901']]

#Intに変換
def convert_s2i(game):
    for i in range(len(game)):
        for j in range(3):
            game[i][j] = int(game[i][j])
    return game

game1 = convert_s2i(game1_low)
game2 = convert_s2i(game2_low)
game3 = convert_s2i(game3_low)
game4 = convert_s2i(game4_low)
game5 = convert_s2i(game5_low)

#試合別
def avg_views_per_games(game):
    result = []
    sum_KOU = 0
    sum_IB = 0
    sum_KUZ = 0
    for i in range(len(game)):
        sum_KOU += game[i][0]
        sum_IB += game[i][1]
        sum_KUZ += game[i][2]
    avg_KOU = sum_KOU / len(game)
    avg_IB = sum_IB / len(game)
    avg_KUZ = sum_KUZ / len(game)
    result.append(avg_KOU)
    result.append(avg_IB)
    result.append(avg_KUZ)
    return result

def fluctuation(game):
    result = []
    KOU = []
    IB = []
    KUZ = []
    for i in range(len(game)):
        KOU.append(game[i][0])
        IB.append(game[i][1])
        KUZ.append(game[i][2])
    result.append(KOU)
    result.append(IB)
    result.append(KUZ)
    return result

def display_avg(avg):
    print("卯月コウ：", avg[0])
    print("イブラヒム：", avg[1])
    print("葛葉：", avg[2])

def display_fluctuation(flactuation):
    print("卯月コウ：", end="")
    for i in range(len(flactuation[0])):
        if i != (len(flactuation[0])-1):
            print(flactuation[0][i], end='->')
        else:
            print(flactuation[0][i])
    print("イブラヒム：", end="")
    for i in range(len(flactuation[1])):
        if i != (len(flactuation[1])-1):
            print(flactuation[1][i], end='->')
        else:
            print(flactuation[1][i])
    print("葛葉：", end="")
    for i in range(len(flactuation[2])):
        if i != (len(flactuation[2])-1):
            print(flactuation[2][i], end='->')
        else:
            print(flactuation[2][i])

game1_avg = avg_views_per_games(game1)
display_avg(game1_avg)
game1_fluctuation = fluctuation(game1)
display_fluctuation(game1_fluctuation)
print("*" * 10)

game2_avg = avg_views_per_games(game2)
display_avg(game2_avg)
game2_fluctuation = fluctuation(game2)
display_fluctuation(game2_fluctuation)
print("*" * 10)

game3_avg = avg_views_per_games(game3)
display_avg(game3_avg)
game3_fluctuation = fluctuation(game3)
display_fluctuation(game3_fluctuation)
print("*" * 10)

game4_avg = avg_views_per_games(game4)
display_avg(game4_avg)
game4_fluctuation = fluctuation(game4)
display_fluctuation(game4_fluctuation)
print("*" * 10)

game5_avg = avg_views_per_games(game5)
display_avg(game5_avg)
game5_fluctuation = fluctuation(game5)
display_fluctuation(game5_fluctuation)
print("*" * 10)

#個人別
KOU = []
IB = []
KUZ = []

def personal(game_flactuation):
    KOU.append(game_flactuation[0])
    IB.append(game_flactuation[1])
    KUZ.append(game_flactuation[2])

personal(game1_fluctuation)
personal(game2_fluctuation)
personal(game3_fluctuation)
personal(game4_fluctuation)
personal(game5_fluctuation)

def result_personal(streamer):
    benri = []
    for i in range(len(streamer)):
        for j in range(len(streamer[i])):
            benri.append(streamer[i][j])
    print("最大：", max(benri), "最小：", min(benri), "平均：", sum(benri)/len(benri))

print("卯月コウ")
result_personal(KOU)
print("イブラヒム")
result_personal(IB)
print("葛葉")
result_personal(KUZ)

