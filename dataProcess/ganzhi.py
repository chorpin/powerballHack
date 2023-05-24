# 导入时间库
import datetime
import requests
from bs4 import BeautifulSoup

import mysql.connector

# 假设这是您的 get_all_info 函数




# 天干和地支的名称
gan = "甲乙丙丁戊己庚辛壬癸"
zhi = "子丑寅卯辰巳午未申酉戌亥"


# 计算年柱，成功
def get_nian_zhu(year):
    # 获取甲子年
    jiazi = datetime.datetime(1984, 2, 4)
    # 计算年数差
    diff = year - jiazi.year
    # 计算天干和地支的序号
    gan_index = (year-3) % 10
    zhi_index = (year-3) % 12
    # 返回天干地支的名称
    return gan[gan_index-1]+zhi[zhi_index-1]


def ganzhi_filter(tag):
    return tag.name == "p" and tag.find("span", string="干支日期：") is not None

#目前而言我们用的是日柱年柱那些，而且直接调用的是这个函数，因为数据量少，数据类型小。所以目前还是可以的
def get_all_info(month, day, year):
    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "charset": "UTF-8"
    }
    # 访问网页
    url = f"https://rili.ximizi.com/wannianli/{year}/{year}-{month}-{day}.html"

    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        content = str(response.content, 'utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        # 使用 find 方法查找符合条件的 <p> 标签
        target_p_tag = soup.find(ganzhi_filter).get_text().replace("干支日期：", "").strip()

        # 输出找到的 <p> 标签
        # print('target_p_tag',target_p_tag,type(target_p_tag))
        return(target_p_tag)
            
    else:
        print("请求失败，错误代码：", response.status_code)


def get_chromStamp_info(year,month,day):
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "charset": "UTF-8"
    }
    
    url = f"https://rili.ximizi.com/wannianli/{year}/{year}-{month}-{day}.html"

    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
        content = str(response.content, 'utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        example_elems = soup.find_all(class_="hc3_text")

        main_info = example_elems[0]

        child_tags = main_info.find_all(recursive=False)

        for (index, el) in child_tags:
            #print(index, 'index.contents:',index.contents,type(index),'--->', type(el),el)
            if(index.contents[0] == '干支日期：'):
                print(el.split())

    else:
        print("Sth goes wrong：", response.status_code)


def update_ganzhi_values():
    # 用你自己的 MySQL 数据库连接信息替换这些占位符
    config = {
        "user": "root",
        "password": "zaq753XSW42",
        "host": "localhost",
        "database": "powerball"
    }

    # 连接到 MySQL 数据库
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # 从 data_table 表中获取 Month, Day, Year 数据
    query = "SELECT id, Month, Day, Year FROM data_table"
    cursor.execute(query)
    data = cursor.fetchall()

    # 遍历数据并更新 ganzhi 列的值
    for row in data:
        Cid, month, day, year = row
        #print(type(month),month,day,year)
        ganzhi = get_all_info(str(month), str(day), str(year))
        #print("ganzhi",ganzhi)

        # 更新数据表中的 ganzhi 列
        update_query = f"UPDATE data_table SET ganzhi = '{ganzhi}' WHERE id = {Cid}"
        cursor.execute(update_query)

    # 提交更改并关闭数据库连接
    connection.commit()
    cursor.close()
    connection.close()

# 调用函数
update_ganzhi_values()

#get_all_info()
#get_chromStamp_info(2023,4,1)
