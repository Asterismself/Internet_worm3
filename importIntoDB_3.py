# _*_ coding : UTF-8 _*_
# @Time : 2022/10/16 20:18
# @Author : GYH
# @File : ImportIntoDB
# @Project : WebNotices
import pymysql
import json


DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = 'gyh17856973504'
DBNAME = 'WebNotices'
DBPORT = 3306
DBCHARSET = 'utf8'


noticeType = int(input('请输入通知类型（0表示综合信息，1表示教务管理，2表示教学研究，3表示实践教学，4表示考试管理，5表示交流管理，6表示基地专业，7表示泰山学堂，8表示教师培训，9表示课程建设，10表示质量评估，11表示技术支持）： '))
if noticeType == 0:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\综合信息.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
        # print('A')
    result = json.loads(content)
elif noticeType == 1:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\教务管理.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 2:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\教学研究.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 3:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\实践教学.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 4:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\考试管理.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 5:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\交流管理.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 6:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\基地专业.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 7:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\泰山学堂.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 8:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\教师培训.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 9:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\课程建设.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 10:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\质量评估.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif noticeType == 11:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\WebNotices\\jsonInfo\\技术支持.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)

try:
    # 连接数据库
    DB = pymysql.connect(user=DBUSER, password=DBPASS, host=DBHOST, database=DBNAME, port=DBPORT, charset=DBCHARSET)
    print('数据库连接成功！')
    # 创建表格
    cur = DB.cursor()
    if noticeType == 0:
        cur.execute('DROP TABLE IF EXISTS CI')
        sql = 'CREATE TABLE CI(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 1:
        cur.execute('DROP TABLE IF EXISTS EA')
        sql = 'CREATE TABLE EA(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 2:
        cur.execute('DROP TABLE IF EXISTS TR')
        sql = 'CREATE TABLE TR(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 3:
        cur.execute('DROP TABLE IF EXISTS PT')
        sql = 'CREATE TABLE PT(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 4:
        cur.execute('DROP TABLE IF EXISTS EM')
        sql = 'CREATE TABLE EM(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 5:
        cur.execute('DROP TABLE IF EXISTS CM')
        sql = 'CREATE TABLE CM(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 6:
        cur.execute('DROP TABLE IF EXISTS BP')
        sql = 'CREATE TABLE BP(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 7:
        cur.execute('DROP TABLE IF EXISTS MTS')
        sql = 'CREATE TABLE MTS(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 8:
        cur.execute('DROP TABLE IF EXISTS TT')
        sql = 'CREATE TABLE TT(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 9:
        cur.execute('DROP TABLE IF EXISTS CC')
        sql = 'CREATE TABLE CC(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 10:
        cur.execute('DROP TABLE IF EXISTS QA')
        sql = 'CREATE TABLE QA(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    elif noticeType == 11:
        cur.execute('DROP TABLE IF EXISTS TS')
        sql = 'CREATE TABLE TS(reTime CHAR(15),Title CHAR(70),Url CHAR(130))'
        cur.execute(sql)
        print('表格创建成功！')
    # 插入数据：
    i = 0
    while i < len(result):
        if noticeType == 0:
            sql = 'INSERT INTO CI(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 1:
            sql = 'INSERT INTO EA(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 2:
            sql = 'INSERT INTO TR(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 3:
            sql = 'INSERT INTO PT(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 4:
            sql = 'INSERT INTO EM(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 5:
            sql = 'INSERT INTO CM(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 6:
            sql = 'INSERT INTO BP(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 7:
            sql = 'INSERT INTO MTS(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 8:
            sql = 'INSERT INTO TT(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 9:
            sql = 'INSERT INTO CC(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 10:
            sql = 'INSERT INTO QA(reTime, Title, Url) values(%s, %s, %s)'
        elif noticeType == 11:
            sql = 'INSERT INTO TS(reTime, Title, Url) values(%s, %s, %s)'
        values = (result[i]['Time'], result[i]['Title'], result[i]['Url'])
        cur.execute(sql, values)
        DB.commit()
        print('数据插入成功！')
        i = i + 1
except pymysql.Error as error:
    print('数据库连接失败或表格创建不成功：' + str(error))
    DB.rollback()
