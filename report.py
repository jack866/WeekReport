# -*- coding: cp936 -*-
title = '流量池v8'

'''记录每天一天工作内容与总结'''
lastWeek = 4
new1 = 7
bug1 = new1 + lastWeek
fix1 = 7
rate1 = round(fix1/bug1*100)
# rate1 = 0
event1 = '1.追踪并处理上周遗留bug'+'\n' \
         '2.重点测试分配经纪人新规则以及分配经纪人页面'+'\n' \
         '选择分配经纪人列表排序优化已完成'

day1 = '周一新增缺陷:'+str(new1) + '个，' + \
       '上周遗留缺陷:'+str(lastWeek)+'个，' + \
       '累计缺陷:' + str(bug1) + '个。' + \
       '已处理缺陷:'+str(fix1)+'个。剩余待处理缺陷:'\
       + str(bug1-fix1) + '个。' + '处理率:' + str(rate1) + '%。' + '\n' \
       + event1 + '\n'

new2 = 4
bug2 = bug1-fix1+new2
fix2 = 8
rate2 = round(fix2/bug2*100)
# rate2 = 0
event2 = '1.追踪并处理下昨日遗留bug'+'\n' \
         '2.重点测试还是分配规则，侧重点为分配规则的一些细节，例如分配间隔分配时间带小数'+'\n' \
         '【系统管理】增加【客户分配管理】，用于管理客户分配规则、【流量管理】-【客户管理】详情页面优化 已完成'

day2 = '周二新增缺陷:'+str(new2) + '个，' + \
       '累计缺陷:' + str(bug2) + '个。' + \
       '已处理缺陷:'+str(fix2)+'个。剩余待处理缺陷:'\
       + str(bug2-fix2) + '个。' + '处理率:' + str(rate2) + '%。' + '\n' \
       + event2 + '\n'

new3 = 7
bug3 = bug2-fix2+new3
fix3 = 2
rate3 = round(fix3/bug3*100)
event3 = '1.追踪并处理下昨日遗留bug'+'\n' + \
         '2.重点测试目标管理预览页面，直播时长、留资统计数据要求与主播报表上的数据保持一致'+'\n'

day3 = '周三新增缺陷:'+str(new3) + '个，' + \
       '累计缺陷:' + str(bug3) + '个。' + \
       '已处理缺陷:'+str(fix3)+'个。剩余待处理缺陷:'\
       + str(bug3-fix3) + '个。' + '处理率:' + str(rate3) + '%。' + '\n' \
       + event3 + '\n'

new4 = 1
bug4 = bug3-fix3+new4
fix4 = 6
rate4 = round(fix4/bug4*100)
event4 = '1.追踪并处理下昨日遗留bug ' + '\n' + \
         '2.因为主体都已经测完，主要是回归昨日剩下的bug' + '\n' + \
         '【目标管理】增加预览功能、【客户管理】分配规则优化，支持分配多名经纪人已完成'
day4 = '周四新增缺陷:'+str(new4) + '个，' + \
       '累计缺陷:' + str(bug4) + '个。' + \
       '已处理缺陷:'+str(fix4)+'个。剩余待处理缺陷:'\
       + str(bug4-fix4) + '个。' + '处理率:' + str(rate4) + '%。' + '\n' \
       + event4 + '\n'

new5 = 0
bug5 = bug4-fix4+new5
fix5 = 0
# rate5 = round(fix5/bug5*100)
rate5 = 0
event5 = '1.参加组织架构的进度汇总 ' + '\n' + \
         '2.整理下期计划' + '\n'


day5 = '周五新增缺陷:'+str(new5) + '个，' + \
       '累计缺陷:' + str(bug5) + '个。' + \
       '已处理缺陷:'+str(fix5)+'个。剩余待处理缺陷:'\
       + str(bug5-fix5) + '个。' + '处理率:' + str(rate5) + '%。' + '\n' \
       + event5 + '\n'


'''记录一周中需要报告的问题'''
event = '暂无'


nextPlan = '暂定流量池，若无新需求则管家新组织架构下的报表回归'

bugs = new1+new2+new3+new4+new5+lastWeek  # 一周共计产生bug
fixes = fix1+fix2+fix3+fix4+fix5  # 一周共计处理bug
rate = round(fixes/bugs*100)

content = '本周主要测试' + title + '的相关内容。本周具体测试内容如下:' + \
          '\n' + '\n' + day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5 + '\n' + \
          '过程中遇到的问题:' + event + '\n'+ '\n' + '共计产生缺陷' + str(bugs) + '个,' + '共计处理' + str(fixes)+'个,' + \
          '剩余待处理缺陷' + str(bugs-fixes) + '个,' + '处理率：' + str(rate) + '%。'


f = open('C:/Users/Administrator/Desktop/周报.txt', 'w')
f.write(title + '\n' + '\n' + '\n' + content + '\n' + '\n' + '\n'+nextPlan)





