import numpy as np
from wordcloud import WordCloud, ImageColorGenerator  # , STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import jieba  # cutting Chinese sentences into words


def plt_imshow(x, ax=None, show=True):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(x)
    ax.axis("off")
    if show: plt.show()
    return ax


def count_frequencies(word_list):
    freq = dict()
    for w in word_list:
        if w not in freq.keys():
            freq[w] = 1
        else:
            freq[w] += 1
    return freq


if __name__ == '__main__':
    # setting paths

    fname_stop = 'stopwords/hit_stopwords.txt'
    fname_mask = 'pictures/r.png'#'pictures/owl.jpeg'
    fname_font = 'SourceHanSerifK-Light.otf'

    import pymysql
    from dbutils.pooled_db import PooledDB
    # -*- coding= utf-8 -*-
    import jieba  # 分词
    from matplotlib import pyplot as plt  # 绘图，数据可视化
    from wordcloud import WordCloud
    from PIL import Image  # 处理图像，python自带
    import numpy as np  # 矩阵运算

    POOL = PooledDB(
        creator=pymysql,
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',  # 输入数据库密码
        database='test',  # 数据库名
        charset='utf8'
    )
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = """ SELECT title FROM wechat_article
        """
    # sql = """SELECT  tname,tread,zan,see FROM official_accounts
    #          limit 100
    # """
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    text = ""
    for item in result:
        # print(item[0])
        text = text + item['title']


    print(text)
    cursor.close()
    conn.close()
    # read in texts (an article)

    # Chinese stop words
    STOPWORDS_CH = open(fname_stop, encoding='utf8').read().split()

    # processing texts: cutting words, removing stop-words and single-charactors
    word_list = [
        w for w in jieba.cut(text)
        if w not in set(STOPWORDS_CH) and len(w) > 1
    ]
    freq = count_frequencies(word_list)

    # processing image
    im_mask = np.array(Image.open(fname_mask))
    im_colors = ImageColorGenerator(im_mask)

    # generate word cloud
    wcd = WordCloud(font_path=fname_font,  # font for Chinese charactors
                    background_color='white',
                    mode="RGBA",
                    mask=im_mask,
                    )
    # wcd.generate(text) # for English words
    wcd.generate_from_frequencies(freq)
    wcd.recolor(color_func=im_colors)

    # visualization
    ax = plt_imshow(wcd, )
    ax.figure.savefig(f'single_wcd.png', bbox_inches='tight', dpi=150)

    fig, axs = plt.subplots(1, 2)
    plt_imshow(im_mask, axs[0], show=False)
    plt_imshow(wcd, axs[1])
    fig.savefig(f'conbined_wcd.png', bbox_inches='tight', dpi=150)

