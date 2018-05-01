# -*- coding: utf-8 -*-
# !/usr/bin/env python

import logging
import os
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    # 通过日志处理
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # 第一个参数是训练语料，第二个参数是词语的最低频度，默认值为5
    # 第三个参数为语向量维度，第四个参数为词语上下午窗口大小，第五个是并行化训练使用CPU计算核心数量
    model = Word2Vec(LineSentence('D:/Project/afterseg_data_patent/afterseg_patent.txt'), min_count=1, size=50, window=5 ,workers=multiprocessing.cpu_count())

    # 保存模型
    model.save('D:/A/50model.model')
