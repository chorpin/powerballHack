gua_number_dict = {
    "坎": [1, 10, 11, 21],
    "坤": [2, 12, 20, 22],
    "震": [3, 13, 23, 30],
    "巽": [4, 14, 24],
    "中": [5, 15, 25],
    "乾": [6, 16, 26],
    "兑": [7, 17, 27],
    "艮": [8, 18, 28],
    "离": [9, 19, 29],
}

tian_gan_dict = {
    '甲': 6,
    '乙': 2,
    '丙': 8,
    '丁': 7,
    '戊': 1,
    '己': 9,
    '庚': 3,
    '辛': 4,
    '壬': 6,
    '癸': 2
}

di_zhi_dict = {
    '子': (1, 6),
    '丑': (5, 10),
    '寅': (3, 8),
    '卯': (3, 8),
    '辰': (5, 10),
    '巳': (2, 7),
    '午': (2, 7),
    '未': (5, 10),
    '申': (4, 9),
    '酉': (4, 9),
    '戌': (5, 10),
    '亥': (1, 6)
}


def ganzhi_to_bagua(ganzhi):
    all_nums = []
    tian_sum =0
    di_sum =0
    ganzhi = ganzhi.split(' ')
    
    for i in ganzhi:
        all_nums.append(tian_gan_dict[i[0]])
        all_nums.append(di_zhi_dict[i[1]][0])
        all_nums.append(di_zhi_dict[i[1]][1])
    for n in all_nums:
        if n%2 ==1:
            tian_sum = tian_sum + n
        if n%2 ==0:
            di_sum = di_sum + n
    if tian_sum > 25:
        tian_sum = tian_sum%25
    if di_sum >30:
        di_sum = di_sum % 30
    for key, values in gua_number_dict.items():
        if tian_sum in values:
            upper_gua = key
        if di_sum in values:
            baja_gua = key
    
    return [upper_gua,baja_gua]

print(ganzhi_to_bagua('己丑年 丁丑月 甲申日'),':',ganzhi_to_bagua('庚寅年 戊寅月 丁亥日'))

