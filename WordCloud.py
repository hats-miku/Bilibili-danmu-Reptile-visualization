# WordCloud.py
'''依赖模块
pip install jieba, pyecharts
'''
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import jieba


def wordcloud(path):
    with open(path, encoding='utf-8') as f:
        text = " ".join([line.split(',')[-1] for line in f.readlines()])

    words = jieba.cut(text)
    _dict = {}
    #对切割的词汇进行排序
    for word in words:
        if len(word) >= 2:
            _dict[word] = _dict.get(word, 0) + 1
    #将字典转化为列表
    items = list(_dict.items())
    #将字典按照键值排序
    items.sort(key=lambda x: x[1], reverse=True)

    WordCloudPicture = (
        WordCloud()
            .add( "",items,word_size_range=[20, 120],
                  textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
        )
            .render("F:\毕业设计\Photos\wordcloud.html")
    )


if __name__ == "__main__":
   path = 'F:\毕业设计\Data\\126654047弹幕文件.csv'
   wordcloud(path)