# -*- coding: utf-8 -*-
# !/usr/bin/env python

import jieba.analyse
from jieba import analyse
from jieba.analyse import *
import os
import sys

def read_dir_all(path):
    # 设置utf-8格式，预防中文输出乱码
    reload(sys)
    sys.setdefaultencoding('utf-8')
    dir_list = os.listdir(path)
    content = []  # 用content存储合并结果

    for i in dir_list:
        # 循环打开某文件夹下的文件
        with open('\\'.join([path, i])) as f:  # windows下路径用"\\"分隔；
            data = f.read()
            print('====='+i+'=====')
            # 指定关键词保存文件路径,并创建
            doc = open('D:/Project/data_keywords/' + i, 'wb')

            # 情况一:没有指定词的词性
            for keyword, weight in textrank(data, topK=20, withWeight=True):

            # 情况二:指定词性为名词和动名词
            # for keyword, weight in textrank(data, topK=20, withWeight=True, allowPOS=('n', 'vn')):

                # 控制台输出关键词和权重
                print('%s %s' % (keyword, weight))
                result = ('%s ' % (keyword))

                # 仅把关键词写入文本
                doc.write(result)
                doc.write('\n')
            doc.close()

if __name__ == '__main__' :
    # 指定寻找关键词文本的路径
    path = r'D:/Project/data_TRIZ/principle9_10_11'
    read_dir_all(path)
