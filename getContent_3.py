# _*_ coding : UTF-8 _*_
# @Time : 2022/10/16 16:05
# @Author : GYH
# @File : GetContent
# @Project : WebNotices
# https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=9&PAGENUM=1&urltype=tree.TreeTempUrl&wbtreeid=1013
# https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=9&PAGENUM=2&urltype=tree.TreeTempUrl&wbtreeid=1013
# https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=9&PAGENUM=3&urltype=tree.TreeTempUrl&wbtreeid=1013
# https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=9&PAGENUM=5&urltype=tree.TreeTempUrl&wbtreeid=1013
# url = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=9&PAGENUM=' + page + '&urltype=tree.TreeTempUrl&wbtreeid=' + 1013~1024

import urllib.request
from lxml import etree
import json
import time
import datetime


def create_request(_page, _noticeType):
    url = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=9&PAGENUM=' + str(_page) + '&urltype=tree.TreeTempUrl&wbtreeid=' + str(_noticeType)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    _request = urllib.request.Request(url=url, headers=headers)
    return _request


def get_content(_request):
    response = urllib.request.urlopen(_request)
    _content = response.read().decode('utf-8')
    print('网页源码获取成功！')
    return _content


def analysis_content(*para):
    res_list = []
    for page in range(para[1], para[2] + 1):
        # 创建请求标头
        request = create_request(page, para[0])
        # 获得网页源码
        content = get_content(request)
        tree = etree.HTML(content)
        title_list = tree.xpath('//div[@id="div_more_news"]/div[@class="leftNews3"]//a/@title')
        # print(len(title_list))
        time_list = tree.xpath('//div[@id="div_more_news"]/div[@class="leftNews3"]//div/text()')
        # print(len(time_list))
        url_list = tree.xpath('//div[@id="div_more_news"]/div[@class="leftNews3"]//a/@href')
        # print(len(url_list))
        i = 0
        while i < len(url_list):
            if url_list[i][:7] == 'content':
                url_list[i] = 'https://www.bkjx.sdu.edu.cn/' + url_list[i]
            i = i + 1
        # print(url_list)

        for j in range(0, len(title_list)):
            list = {}
            list['Time'] = time_list[j]
            list['Title'] = title_list[j]
            list['Url'] = url_list[j]
            res_list.append(list)
    print('源码解析成功！')
    return res_list


def down_load(_data_list, _noticeType):
    _data_list = json.dumps(_data_list, ensure_ascii=False)
    if noticeType == 1013:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '综合信息.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1014:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '教务管理.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1015:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '教学研究.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1016:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '实践教学.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1017:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '考试管理.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1018:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '交流管理.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1019:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '基地专业.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1020:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '泰山学堂.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1021:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '教师培训.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1022:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '课程建设.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1023:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '质量评估.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    elif noticeType == 1024:
        with open('E:\\python_learning\\Internet_worm_learning\\WebNotices\\' + '技术支持.json', 'w', encoding='utf-8') as fp:
            fp.write(_data_list)
            fp.close()
    print('下载成功！')


if __name__ == '__main__':
    year, month, day, hour, minute = map(int, input('请输入爬取时间（精确到分钟）：').split())
    second = 0
    # 定时任务
    # 设定一个标签，确保是完成定时任务以后，在修改时间
    # flag = 0
    # 设置启动时间
    sched_timer = datetime.datetime(year, month, day, hour, minute, second)
    while True:
        now = datetime.datetime.now()
        # datetime时间是毫秒级的，而我们自己设置的是秒级的，如果直接写sched_timer==now，成功率很低，所以给一个一秒误差
        if sched_timer < now < sched_timer + datetime.timedelta(seconds=1):
            time.sleep(1)
            noticeType = int(input('请输入通知类型（0表示综合信息，1表示教务管理，2表示教学研究，3表示实践教学，4表示考试管理，5表示交流管理，6表示基地专业，7表示泰山学堂，8表示教师培训，9表示课程建设，10表示质量评估，11表示技术支持）： ')) + 1013
            start_page = int(input('请输入起始页码： '))
            end_page = int(input('请输入结束页码： '))
            # 获得想要的数据
            data_list = analysis_content(noticeType, start_page, end_page)
            # 下载
            down_load(data_list, noticeType)
            break
            # flag = 1
        else:
            time.sleep(1)



