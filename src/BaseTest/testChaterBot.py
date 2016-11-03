#coding=utf8
# 注意中文问题，传入的key编码要为unicode
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def baseTest():
    deepThought = ChatBot("deepThought")
    deepThought.set_trainer(ChatterBotCorpusTrainer)
    # 使用中文语料库训练它
    deepThought.train("chatterbot.corpus.chinese")  # 语料库
    print(deepThought.get_response(u"很高兴认识你"))
    print(deepThought.get_response(u"嗨，最近如何?"))
    print(deepThought.get_response(u"复杂优于晦涩")) #语出 The Zen of Python
    print(deepThought.get_response(u"面对模棱两可，拒绝猜测的诱惑."))
    print(deepThought.get_response(u"你叫什么名字?"))
    # print(deepThought.get_response("生命、宇宙以及世间万物的终极答案是什么?"))

def testAddTraining():
    from chatterbot.trainers import ListTrainer
    deepThought = ChatBot("Training demo")
    deepThought.set_trainer(ListTrainer)
    deepThought.train([
        u"嗳，渡边君，真喜欢我?",
        u"那还用说?",
        u"那么，可依得我两件事?",
        u"三件也依得",
    ])
    print(deepThought.get_response(u"嗳，渡边君，真喜欢我?")) #语出 The Zen of Python
    print(deepThought.get_response(u"那还用说?")) #语出 The Zen of Python

baseTest
testAddTraining
