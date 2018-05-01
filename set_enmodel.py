# -*- coding: utf-8 -*-
# !/usr/bin/env python

from sklearn.datasets import fetch_20newsgroups
from gensim.models import word2vec
from bs4 import BeautifulSoup
import re
import nltk
import time

#下载nltk
#nltk.download()
#测试下载情况
# from nltk.book import *
# text1.concordance("monstrous")

start = time.time()

news = fetch_20newsgroups(subset='all')
X, y = news.data, news.target

def news_to_sentences(news):
    # 下载最新新闻文本作为训练语料
    news_text = BeautifulSoup(news).get_text()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(news_text)
    sentences = []
    for sent in raw_sentences:
        sentences.append(re.sub('[^a-zA-Z]', ' ', sent.lower().strip()).split())
    return sentences

# 句子词语列表化
sentences = []
for x in X:
    sentences.extend(news_to_sentences(x))

# 设置词语向量维度
num_featrues = 300
# 保证被考虑词语的最低频度
min_word_count = 20
# 设置并行化训练使用CPU计算核心数量
num_workers = 2
# 设置词语上下午窗口大小
context = 5

# 向量化
model = word2vec.Word2Vec(sentences, workers=num_workers, size=num_featrues, min_count=min_word_count, window=context)

model.init_sims(replace=True)

# 输入一个路径，保存训练好的模型
model.save("D:/Project/model/en_word2vec_model")