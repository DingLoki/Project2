# -*- coding: utf-8 -*-
# !/usr/bin/env python

import jieba
import multiprocessing
from gensim.models import word2vec
import codecs
import sys

# 设置utf-8格式，预防中文输出乱码
reload(sys)
sys.setdefaultencoding('utf-8')

# 去除停用词方法一：创建clearSen（）函数并调用，去除部分符号，
# 但是仅限于只停用较少部分，否则代码不美观
# def clearSen(comment):
#     comment = comment.strip(' ')
#     comment = comment.replace('、', ' ')
#     comment = comment.replace('~', ' ')
#     comment = comment.replace('～', ' ')
#     comment = comment.replace('{"error_message": "EMPTY SENTENCE"}','')
#     comment = comment.replace('…', '')
#     comment = comment.replace('\r', '')
#     comment = comment.replace('\t', ' ')
#     comment = comment.replace('\f', ' ')
#     comment = comment.replace('/', ' ')
#     comment = comment.replace('、', ' ')
#     comment = comment.replace('/', ' ')
#     comment = comment.replace('_', '')
#     comment = comment.replace('?', '')
#     comment = comment.replace('？', '')
#     comment = comment.replace('➕', '')
#     comment = comment.replace('，', '')
#     comment = comment.replace(',', '')
#     comment = comment.replace('。', '')
#     comment = comment.replace('.', '')
#     comment = comment.replace('【', ' ')
#     comment = comment.replace('】', ' ')
#     comment = comment.replace('！', '')
#     comment = comment.replace('；', '')
#     comment = comment.replace(';', '')
#     comment = comment.replace('：', '')
#     comment = comment.replace(':', '')
#     comment = comment.replace('、', '')
#     comment = comment.replace('（', ' ')
#     comment = comment.replace('）', ' ')
#     comment = comment.replace('(', ' ')
#     comment = comment.replace(')', ' ')
#     comment = comment.replace('<', ' ')
#     comment = comment.replace('>', ' ')
#     comment = comment.replace('1', '')
#     comment = comment.replace('2', '')
#     comment = comment.replace('3', '')
#     comment = comment.replace('4', '')
#     comment = comment.replace('5', '')
#     comment = comment.replace('6', '')
#     comment = comment.replace('7', '')
#     comment = comment.replace('8', '')
#     comment = comment.replace('9', '')
#     comment = comment.replace('0', '')
#     return comment

# 用jieba进行分词，对象为专利总文本，一行一个专利信息
comment = open('D:/Project/data_patent/patent.txt').read()

# 方法一：clearSen（）函数去除停用词
# comment = clearSen(comment)

# 方法二：加载停用词
for stopWord in codecs.open('D:/getKeyWords/stopwords.txt', 'r', 'utf-8'):
    comment.append(stopWord.strip())

# 加载自定义词库
jieba.load_userdict('D:/Project/user/user.txt')
comment = ' '.join(jieba.cut(comment))

# 分完词的文件写到新的txt中去
fo = open("D:/Project/afterseg_data_patent/afterseg_patent.txt", "w")
fo.write(comment)
print("finished!")
fo.close()

sentences = word2vec.Text8Corpus(u'D:/Project/afterseg_data_patent/afterseg_patent.txt')
# 第一个参数是训练语料，第二个参数是词语的最低频度，默认值为5
# 第三个参数为语向量维度，第四个参数为词语上下午窗口大小，第五个是并行化训练使用CPU计算核心数量
model = word2vec.Word2Vec(sentences, min_count=1, size=300, window=5, workers=multiprocessing.cpu_count())

# 存储训练好的模型：
model.save('D:/Project/model/size300_model')