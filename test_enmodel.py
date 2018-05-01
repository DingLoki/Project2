# -*- coding: utf-8 -*-
# !/usr/bin/env python

from gensim.models import word2vec

# 加载模型
model = word2vec.Word2Vec.load("D:/Project/model/en_word2vec_model")
# model.train(more_sentences)

#=========以下测试文本及例子选取与网络========
#寻找指定词语最相似的词语
print model.most_similar('morning', topn=1)
#[(u’afternoon’, 0.8059341907501221)]

#得到指定词的词向量
print model['morning']

#词向量加减
print model.most_similar(positive=['man', 'son'], negative=['woman'], topn=4)
#[(u’lord’, 0.7308236360549927), (u’father’, 0.6855698227882385),
# (u’spirit’, 0.6771275997161865), (u’grace’, 0.6561732292175293)]

#计算两个词语相似度
print model.similarity('woman', 'man')
#0.756960729577

#计算两个句子相似度
list1 = ['the', 'cat', 'is', 'walking', 'in', 'the', 'bedroom']
list2 = ['the', 'dog', 'was', 'running', 'across', 'the', 'kitchen']
print model.n_similarity(list1, list2)
#0.811719864179
