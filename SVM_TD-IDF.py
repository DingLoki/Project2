# -*- coding: utf-8 -*-
# !/usr/bin/env python
# coding=utf-8

import time
import re
import codecs
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":

    # 第一步 计算TFIDF

    # 文档预料 空格连接
    corpus = []

    # 读取预料 一行预料为一个文档
    for line in open('D:/Project/afterseg_data_patent/afterseg_patent.txt', 'r').readlines():
        print line
        corpus.append(line.strip())
        # print corpus
    # time.sleep(1)

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()

    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()

    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()

    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

    # 打印特征向量文本内容
    print 'Features length: ' + str(len(word))
    resName = "D:/restxt.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')

    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        print u"-------这里处理第", i, u"个文本的词语tf-idf权重------"
        for j in range(len(word)):
            print weight[i][j],
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')

    result.close()

    # 聚类Kmeans
    print 'Start Kmeans:'
    from sklearn.cluster import KMeans

    clf = KMeans(n_clusters=21)
    s = clf.fit(weight)
    print s
    res = clf.fit_predict(weight)
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