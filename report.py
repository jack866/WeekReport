# -*- coding: cp936 -*-
import random
import json
title = '������v6'

day1 = '1'
day2 = '2'
day3 = '3'
day4 = '4'
day5 = '5'
event = '����'
nextPlan = '��������������'
bugs = '1'
remains = '0'

content = '���ܻ��Ǽ������ܵ�һ������˼·����������' + title + '��������ݡ����ܾ������ݲ�������:' + \
            '\n' + day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5 + '\n' + \
            '����������������:' + event + '\n' + '���Ʋ���ȱ��' + bugs + '������'

f = open('C:/Users/Administrator/Desktop/�ܱ�.txt', 'w')
f.write(title + '\n' + '\n' + '\n' + content + '\n' + '\n' + '\n'+nextPlan)





