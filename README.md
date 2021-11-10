# Bilibili-danmu-Reptile-visualization
这是一个基于python的弹幕爬取+可视化分析的项目。

# 前言
上篇我们说到了有数量限制弹幕抓取
> 链接：https://blog.csdn.net/hats_miku/article/details/121234922

# 无数量限制弹幕抓取
打开一个视频，我们要拿到的是弹幕数据，就可以先分析一下网站，既然是分析网站，自然是F12或右键查看源码了。下面要进行抓包，我们先清空network下面的所有。
![1](https://user-images.githubusercontent.com/93989649/141073059-db07b92f-1daf-4a51-8191-cfd81023d849.png)

我们点击b站弹幕列表下面的查看历史弹幕。上面有个日历可以选，我就随便选一天了，我们观察会出现什么。
![2](https://user-images.githubusercontent.com/93989649/141073113-fd639a64-6086-46b1-996b-0614032c01f3.png)

你有没有注意到这样一段'seg.so?type=1&oid=126654047&date=2021-11-02',我再分析一下可以看到b站又提供了一个接口，后面是一个日期格式的参数。那我一定会想到，只要我按照这样的格式，我可以指定任意一天。
![3](https://user-images.githubusercontent.com/93989649/141073961-5a5aed6e-11a2-4d28-af5b-15df6ce0bad7.png)

接下来我们只需要通过遍历日期便可获得更多的弹幕。需要注意的是，这个接口需要登陆，因此在请求的时候必须得加入cookies

# 代码实现
## 1.获得cid
```
def get_oid(url):
    res = requests.get(url)
    oid = re.findall(r'"cid":(.*?),', res.text)[1]
    print(oid)
    return oid
def get_times(url):
```

## 2.生成开始和结束时间
```
def get_times(url):
start_time = input('请输入时间: ')
today_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print(today_time)
    date = [x for x in pd.date_range(start_time, today_time).strftime('%Y-%m-%d')]
    print(date)
return date
```

## 3.请求网页并使用正则，匹配中文
```
def get_danmuku(oid, date_list):
    danmuku = []
    for date in trange(len(date_list)):
    	url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={oid}&date={date}'
  	  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
   	     'cookie': ''
 		   }
   	 response = requests.get(url, headers=headers)
   	 response.encoding ='utf-8'
    	response =response.text
Danmu = re.findall("[\u4e00-\u9fa5]+",response)  
   	danmuku = danmuku + Danmu
return danmuku
```

## 4.存储数据
```
def save_data(danmuku):
with open('danmus.csv', 'w', encoding='utf_8_sig') as f:
    f.writelines([line+'\n' for line in danmuku])
```

# 成果展示
## 词云图
![5331af1defa54e2db349f29595926734](https://user-images.githubusercontent.com/93989649/141075801-f02adcfc-6f3a-43b0-ac4b-1d1fb13d6b10.png)

## 饼状图
![3fa2e0fc4bdd4cf0965f456016c1c98e](https://user-images.githubusercontent.com/93989649/141076202-279f3260-5637-4ecf-a1bf-451186afb4b0.png)

## 折线图
![d5f14076a4104904a8670080d717344a](https://user-images.githubusercontent.com/93989649/141075957-5d185e08-c881-4793-ab24-07185dd3de2e.png)
