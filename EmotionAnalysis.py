# EmotionAnalysis.py
'''依赖模块
pip install snownlp, pyecharts
'''
from snownlp import SnowNLP
from pyecharts import options as opts
from pyecharts.charts import Pie


def emotionAnalysis(path):
    with open(path, encoding='utf-8') as f:
        text = [line.split(',')[-1] for line in f.readlines()[1:]]

    emotions = {
        'positive': 0,
        'negative': 0,
        'neutral': 0
    }
    for item in text:
        if SnowNLP(item).sentiments > 0.6:
            emotions['positive'] += 1
        elif SnowNLP(item).sentiments < 0.4:
            emotions['negative'] += 1
        else:
            emotions['neutral'] += 1
    print(emotions)

    c = (
        Pie()
            .add("", list(emotions.items()))
            .set_colors(["blue", "purple", "orange"])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
            .render("F:\毕业设计\Photos\emotionAnalysis.html")
    )


if __name__ == "__main__":
    path = 'F:\毕业设计\Data\\126654047弹幕文件.csv'
    emotionAnalysis(path)