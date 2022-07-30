# -*- coding: cp936 -*-
import random
import json
title = '流量池v6'

day1 = '1'
day2 = '2'
day3 = '3'
day4 = '4'
day5 = '5'
event = '暂无'
nextPlan = '流量池下期需求'
bugs = '1'
remains = '0'

content = '本周还是继续上周的一个测试思路，继续测试' + title + '的相关内容。上周具体内容测试如下:' + \
            '\n' + day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5 + '\n' + \
            '过程中遇到的问题:' + event + '\n' + '共计产生缺陷' + bugs + '待处理'

f = open('C:/Users/Administrator/Desktop/周报.txt', 'w')
f.write(title + '\n' + '\n' + '\n' + content + '\n' + '\n' + '\n'+nextPlan)





