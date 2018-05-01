# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
import gensim
import numpy
from numpy import *
import numpy as np

# 设置utf-8格式，预防中文输出乱码
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    # 加载模型
    model = gensim.models.Word2Vec.load('D:/Project/model/size100_model')

    # 文档预料 空格连接
    corpus = []

    x = []
    # 读取预料 一行语料为一个文档
    for line in open('D:/Project/data_keywords_new/patentkey.txt', 'r').readlines():
        print len(line.decode('utf-8').split())
        a = len(line.decode('utf-8').split())
        data = line.strip('\xef\xbb\xbf')  # 去除文本前面某些符号
        k = 0
        z = []
        c = []
        # 获取本行语料的向量化值
        for item in data.split():
            item2 = item.decode('utf-8')
            # 获取向量化值
            print model[item2]
            if k < a:
                z.extend(model[item2])
                c.append(model[item2])
                k = k + 1
        x.append(c)

        corpus.append(line.strip())

    # 聚类Kmeans
    print 'Start Kmeans:'
    from sklearn.cluster import KMeans

    clf = KMeans(n_clusters=21)
    print (clf)

    res = clf.fit_predict(x)
    print res
    print('---')

    # 中心点
    print(clf.cluster_centers_)
    print('===')

    # 每个样本所属的簇
    print(clf.labels_)
    print('+++')
    i = 1
    while i <= len(clf.labels_):
        print i, clf.labels_[i - 1]
        i = i + 1

    # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    print('===')
    print(clf.inertia_)