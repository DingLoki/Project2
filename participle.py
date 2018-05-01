# -*- coding: utf-8 -*-
# !/usr/bin/env python

import jieba.analyse
from jieba import analyse
import os
import jieba
import multiprocessing
import codecs
import sys

# 设置utf-8格式，预防中文输出乱码
reload(sys)
sys.setdefaultencoding('utf-8')

# # 去除停用词方法一：创建clearSen（）函数并调用，去除部分符号，
# # 但是仅限于只停用较少部分，否则代码不美观
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

dir_list = os.listdir(r'D:/Project/data_patent')
content = []  # 用content存储合并结果

for i in dir_list:
    with open('\\'.join(['D:/Project/data_patent', i])) as f:  # windows下路径用"\\"分隔；
        data = f.read()

        # 方法一：clearSen（）函数去除停用词
        # data = clearSen(data)

        # 方法二：加载停用词
        for stopWord in codecs.open('D:/getKeyWords/stopwords.txt', 'r', 'utf-8'):
            data.append(stopWord.strip())

        # 加载自定义词库
        jieba.load_userdict('D:/Project/user/user.txt')
        data = ' '.join(jieba.cut(data))

        # 分完词的文件写到新的txt中去
        fo = open("D:/Project/afterseg_data_patent/" + i, 'wb')
        fo.write(data)
        print("finished!")
        fo.close()



