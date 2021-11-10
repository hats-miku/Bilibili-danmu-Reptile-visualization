# -!- coding: utf-8 -!-
# CrawlWebPages.py
'''依赖模块
pip install requests
'''

import requests
import re
from tqdm import tqdm

def get_data(oid):
    # 分析网页，并获取网页文件
    # 请求头：模拟浏览器对服务器发送请求
    # User-Agent: 浏览器信息
    # cookie: 用户身份信息，常用于检测是否有登录账号
    # response：获取网页文本数据

    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={oid}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'cookie':'buvid3=609D48C2-0B20-4279-AE63-46CFD7796AB053940infoc; DedeUserID=166559060; DedeUserID__ckMd5=c612cbd211cd7798; rpdid=|(ummmu|)k|J0J\'ulmu~l)mRR; LIVE_BUVID=AUTO3115917732036847; _ga=GA1.2.1303042136.1593182209; fingerprint3=76abb7d317593b50a83f24289bcdd7e9; buivd_fp=609D48C2-0B20-4279-AE63-46CFD7796AB053940infoc; buvid_fp=609D48C2-0B20-4279-AE63-46CFD7796AB053940infoc; fingerprint_s=dafda6d6488b5e2e7f3e08b4f0fb254f; buvid_fp_plain=609D48C2-0B20-4279-AE63-46CFD7796AB053940infoc; _uuid=7A72A4A8-D1A3-706E-33A2-5C2F0DDDCCF383586infoc; sid=71br5n3f; fingerprint=0da3f3c8d789d69e42f37de3627d07b9; SESSDATA=6dc93c51%2C1640442015%2C1da16*61; bili_jct=ef84e1e3e89aac4fd61468fd22051c26; blackside_state=1; CURRENT_BLACKGAP=1; bp_t_offset_166559060=576489373971600228; PVID=1; CURRENT_QUALITY=32; CURRENT_FNVAL=976; bp_video_offset_166559060=576931794258045375; innersign=0',
    }
    response = requests.get(url, headers=headers).content.decode('utf-8')
    #print(response) #在控制台打印网页内容
    print('成功获取网页')
    return response


def parse_html(response):
    # 解读网页文件，获取关键信息
    # .*? 通配符 可以匹配任意字符, ()表示精确匹配
    # 正则表达式提取出来的内容 是一个列表

    pattern = re.compile('<d p="(.*?)">(.*?)</d>')
    comments_list = re.findall(pattern, response)
    #print(comments_list) #在控制台打印所匹配的内容
    print('成功获取弹幕信息')
    return comments_list


def save_data(danmuku, oid):
    # 保存数据
    oid = str(oid)
    name = oid + '弹幕文件.csv'
    path = 'F:\毕业设计\Data\{}'.format(name)
    danmus = [','.join(item) for item in danmuku]
    headers = ['stime', 'mode', 'size', 'color', 'date', 'pool',
               'author','dbid', 'page','text']
    headers = ','.join(headers)
    danmus.insert(0, headers)
    print('数据处理完成')
    with open(path, 'w', encoding='utf_8_sig') as f:
        f.writelines([line + '\n' for line in tqdm(danmus)])
    print('数据存储完成')


if __name__ == "__main__":
    url = input('请输入B站视频链接: ')
    res = requests.get(url)
    oid = re.findall(r'"cid":(.*?),', res.text)[1]
    response = get_data(oid)
    danmuku = parse_html(response)
    save_data(danmuku, oid)