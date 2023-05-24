import pymysql
import pandas as pd
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

def generate_hexagram_name(gua1, gua2):
    ba_gua = ['乾', '兑', '离', '震', '巽', '坎', '艮', '坤','中']
    
    if gua1 not in ba_gua or gua2 not in ba_gua:
        raise ValueError("Invalid input, please provide valid base gua from 八卦")

    def gua_to_binary(gua):
        binary_mapping = {
            '乾': '111',
            '兑': '110',
            '离': '101',
            '震': '100',
            '巽': '011',
            '坎': '010',
            '艮': '001',
            '坤': '000',
            '中': 'xxx'
        }
        return binary_mapping[gua]

    binary_gua1 = gua_to_binary(gua1)
    binary_gua2 = gua_to_binary(gua2)

    hexagram_binary = binary_gua1 + binary_gua2
    '''

    hexagram_name_mapping = {
        '111111': '乾为天',
        '111110': '天泽履',
        '111101': '天火同人',
        '111100': '天雷无妄',
        '111011': '天风姤',
        '111010': '天水讼',
        '111001': '天山遁',
        '111000': '天地否',
        '110111': '泽天夬',
        '110110': '兑为泽',
        '110101': '泽火革',
        '110100': '泽雷随',
        '110011': '泽风大过',
        '110010': '泽水困',
        '110001': '泽山咸',
        '110000': '泽地萃',
        '101111': '火天大有',
        '101110': '火泽睽',
        '101101': '离为火',
        '101100': '火雷噬嗑',
        '101011': '火风鼎',
        '101010': '火水未济',
        '101001': '火山旅',
        '101000': '火地晋',
        '100111': '雷天大壮',
        '100110': '雷泽归妹',
        '100101': '雷火丰',
        '100100': '震为雷',
        '100011': '雷风恒',
        '100010': '雷水解',
        '100001': '雷山小过',
        '100000': '雷地豫',
        '011111': '风天小畜',
        '011110': '风泽中孚',
        '011101': '风火家人',
        '011100': '风雷益',
        '011011': '巽为风',
        '011010': '风水涣',
        '011001': '风山渐',
        '011000': '风地观',
        '010111': '水天需',
        '010110': '水泽节',
        '010101': '水火既济',
        '010100': '水雷屯',
        '010011': '水风井',
        '010010': '坎为水',
        '010001': '水山蹇',
        '010000': '水地比',
        '001111': '山天大畜',
        '001110': '山泽损',
        '001101': '山火贲',
        '001100': '山雷颐',
        '001011': '山风蛊',
        '001010': '山水蒙',
        '001001': '艮为山',
        '001000': '山地剥',
        '000111': '地天泰',
        '000110': '地泽临',
        '000101': '地火明夷',
        '000100': '地雷复',
        '000011': '地风升',
        '000010': '地水师',
        '000001': '地山谦',
        '000000': '坤为地'
        }
    '''
    
    
    return hexagram_binary

#print(generate_hexagram_name('乾','兑'),'should be 履')

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
    
    return generate_hexagram_name(upper_gua,baja_gua)



# 连接到MySQL数据库


conn = pymysql.connect(host='localhost', user='root', password='zaq753XSW42', database='powerball', charset='utf8')

# 创建一个游标
cursor = conn.cursor()


# 从数据库中获取所有ganzhi值
cursor.execute("SELECT id, ganzhi FROM data_table;")
rows = cursor.fetchall()

# 遍历每一行，计算64gua值，并更新到数据库中
for row in rows:
    id, ganzhi = row
    gua = ganzhi_to_bagua(ganzhi)
    update_query = f"UPDATE data_table SET gua = '{gua}' WHERE id = '{id}'"
    cursor.execute(update_query)


# 提交更改并关闭连接
conn.commit()
conn.close()
#print(ganzhi_to_bagua('己丑年 丁丑月 甲申日'))