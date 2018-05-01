# -*- coding: utf-8 -*-
# !/usr/bin/env python

import gensim
import sys

# 设置utf-8格式，预防中文输出乱码
reload(sys)
sys.setdefaultencoding('utf-8')

# 加载模型
model = gensim.models.Word2Vec.load('D:/Project/model/size300_model')

# 测试
# 输出某个词的向量值
y1 = model[u"刀具"]
print(y1)
# 计算两个词之间的余弦距离
y2 = model.similarity(u"夹住", u"夹装")
print(y2)

# 计算余弦距离最接近的10个词
item = model.most_similar(u"刀具", topn =10)
for i in item:
    print i[0],
    print i[1]