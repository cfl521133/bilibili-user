# -*-coding:utf8-*-

import requests
import json
import mysql.connector as mariadb
from multiprocessing.dummy import Pool as ThreadPool
import sys
import datetime
import time

def datetime_to_timestamp_in_milliseconds(d):
    current_milli_time = lambda: int(round(time.time() * 1000))
    return current_milli_time()


reload(sys)

sys.setdefaultencoding('utf-8')

urls = []

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/873981/',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

time1 = time.time()
# 873982
for i in range(2, 200000):
    url = 'http://space.bilibili.com/ajax/member/GetInfo?mid=' + str(i)
    urls.append(url)

# s = requests.Session()

proxies = {
        # 'http': '120.198.231.87:84',
        #'https': 'http://219.133.31.120:8888',
}


def getsource(url):
    payload = {
        '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
        'mid': url.replace('http://space.bilibili.com/ajax/member/GetInfo?mid=', '')
    }

    print payload

    jscontent = requests.post('http://space.bilibili.com/ajax/member/GetInfo', headers=head,  data=payload).content

    print(jscontent)

    time2 = time.time()
    jsDict = json.loads(jscontent)
    if jsDict['status'] == True:
        jsData = jsDict['data']

        approve = jsData['approve']
        article = jsData['article']
        attention = jsData['attention']
        attentions = jsData['attentions']
        birthday = jsData['birthday']
        coins = jsData['coins']
        description = jsData['description']
        exp = jsData['level_info']['current_exp']
        face = jsData['face']
        fans = jsData['fans']
        friend = jsData['friend']
        im9_sign = jsData['im9_sign']
        level = jsData['level_info']['current_level']
        mid = jsData['mid']
        name = jsData['name']
        official_verify = jsData['official_verify']['type']
        place = jsData['place']
        playNum = jsData['playNum']
        rank = jsData['rank']
        regtime = jsData['regtime']
        sex = jsData['sex']
        sign = jsData['sign']
        spacesta = jsData['spacesta']


        regtime_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(regtime))
        print "Succeed: " + mid + "\t" + str(time2 - time1)
        try:
            conn = mariadb.connect(host='localhost', user='root', password='', database='bilibili', port=3306, charset='utf8')
            cur = conn.cursor()
            # cur.execute('create database if not exists python')
            cur.execute('INSERT INTO bilibili_user_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        [mid, mid, name, sex, face, coins, regtime_format, spacesta, birthday, place, description,
                         article, fans, friend, attention, sign, str(attentions), level, exp, approve, im9_sign,
                         official_verify, playNum, rank])
        except mariadb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    else:
        print "Error: " + url


pool = ThreadPool(1)
try:
    results = pool.map(getsource, urls)
except Exception:
    print 'ConnectionError'
    time.sleep(300)
    results = pool.map(getsource, urls)

pool.close()
pool.join()
