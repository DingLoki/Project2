# -*- coding: utf-8 -*-
# !/usr/bin/env python
import codecs
import gensim
import jieba
import os
import sys

# 设置utf-8格式，预防中文输出乱码
reload(sys)
sys.setdefaultencoding('utf-8')

# # 去除停用词方法一：创建clearSen（）函数并调用，去除部分符号，
# # 但是仅限于只停用较少部分，否则代码不美观
# def clearSen(data):
#     data = data.strip(' ')
#     data = data.replace('、', ' ')
#     data = data.replace('~', ' ')
#     data = data.replace('～', ' ')
#     data = data.replace('{"error_message": "EMPTY SENTENCE"}', '')
#     data = data.replace('…', ' ')
#     data = data.replace('\r', ' ')
#     data = data.replace('\t', ' ')
#     data = data.replace('\f', ' ')
#     data = data.replace('/', ' ')
#     data = data.replace('、', ' ')
#     data = data.replace('/', ' ')
#     data = data.replace('_', ' ')
#     data = data.replace('?', ' ')
#     data = data.replace('？', ' ')
#     data = data.replace('➕', ' ')
#     data = data.replace('，', ' ')
#     data = data.replace(',', ' ')
#     data = data.replace('。', ' ')
#     data = data.replace('.', ' ')
#     data = data.replace('【', ' ')
#     data = data.replace('】', ' ')
#     data = data.replace('！', ' ')
#     data = data.replace('；', ' ')
#     data = data.replace(';', ' ')
#     data = data.replace(':', ' ')
#     data = data.replace('：', ' ')
#     data = data.replace('、', ' ')
#     data = data.replace('（', ' ')
#     data = data.replace('）', ' ')
#     data = data.replace('(', ' ')
#     data = data.replace(')', ' ')
#     data = data.replace('<', ' ')
#     data = data.replace('>', ' ')
#     data = data.replace('1', ' ')
#     data = data.replace('2', ' ')
#     data = data.replace('3', ' ')
#     data = data.replace('4', ' ')
#     data = data.replace('5', ' ')
#     data = data.replace('6', ' ')
#     data = data.replace('7', ' ')
#     data = data.replace('8', ' ')
#     data = data.replace('9', ' ')
#     data = data.replace('0', ' ')
#     return data

path = r'D:/Project/afterseg_data_patent'
dir_list = os.listdir(path)
# 加载模型
model = gensim.models.Word2Vec.load('D:/Project/model/size200_model')

# 若使用的是已经分好词的文本，则注释分词、加载停用词和自定义词库的步骤
for i in dir_list:
    # 用jieba进行分词
    data = open('D:/Project/afterseg_data_patent/'+i).read()

    # # 方法一：clearSen（）函数去除停用词
    # data = clearSen(data)

    # 方法二：加载停用词
    for stopWord in codecs.open('D:/getKeyWords/stopwords.txt', 'r', 'utf-8'):
        data.append(stopWord.strip())

    # 加载自定义词库
    jieba.load_userdict('D:/A/user_dict/userdict_food.txt')
    data = ' '.join(jieba.cut(data))

    # 分完词的文件写到新的文本中去
    fo = open("D:/TESTCUT/Q/" + i, "w")
    fo.write(data)
    print("finished!")
    fo.close()

    #获得向量值，写到新的文本中
    print('=====' + i + '=====')
    data = data.strip('\xef\xbb\xbf') #去除文本前面某些符号
    doc = open('D:/TESTNUM/Q/' + i, 'a+')
    for item in data.split():
        print item
        # 转码
        item2 = item.decode('utf-8')
        # 输出该模型下的向量值
        print model[item2]
        # 把向量值写入文本
        result = ('%s' % (model[item2]))
        doc.write(result)
        doc.write('\n')
    doc.close()


