# -*- coding: utf-8 -*-
# !/usr/bin/env python

import jieba
import jieba.analyse
from jieba.analyse import *

# 打开指定文本
with open('D:/Project/data_patent/DataCN201721122747.X.txt') as f:
    text = f.read()
fenci_text = jieba.cut(text)

# tf-idf算法提取关键词
for keyword, weight in extract_tags(text, topK=5, withWeight=True):
    print('%s %s' % (keyword, weight))

print('=========')

# textrank算法提取关键词
for keyword, weight in textrank(text, topK=5, withWeight=True):
    print('%s %s' % (keyword, weight))

# 指定词性，使用textrank算法提取关键词
print('=========')
for keyword, weight in textrank(text, topK=5, withWeight=True, allowPOS=('n', 'vn')):
    print('%s %s' % (keyword, weight))
