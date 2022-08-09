# -*- coding: cp936 -*-
title = '流量池v7'

'''记录每天一天工作内容与总结'''
lastWeek = 3
new1 = 7
bug1 = new1 + lastWeek
fix1 = 6
rate1 = round(fix1/bug1*100)
# rate1 = 0
event1 = '处理上周遗留的bug然后主要测试首次客源拨打隐私号，需注意管家端与流量池端不同的测试点以及APP端也需要注意。'
day1 = '周一新增缺陷:'+str(new1) + '个，' + \
       '累计缺陷:' + str(bug1) + '个。' + \
       '已处理缺陷:'+str(fix1)+'个。剩余待处理缺陷:'\
       + str(bug1-fix1) + '个。' + '处理率:' + str(rate1) + '%。' + '\n' \
       + event1 + '\n'

new2 = 0
bug2 = bug1-fix1+new2
fix2 = 0
# rate2 = round(fix2/bug2*100)
rate2=0
event2 = '参加需求评审优化用例。JRZFB-6832-9999角色优化优化已提测，现根据需求字段写sql'
day2 = '周二新增缺陷:'+str(new2) + '个，' + \
       '累计缺陷:' + str(bug2) + '个。' + \
       '已处理缺陷:'+str(fix2)+'个。剩余待处理缺陷:'\
       + str(bug2-fix2) + '个。' + '处理率:' + str(rate2) + '%。' + '\n' \
       + event2 + '\n'

new3 = 4
bug3 = bug2-fix2+new3
fix3 = 1
rate3 = round(fix3/bug3*100)
event3 = '缺陷问题集中为除直播总时长sql写的有问题以外，其余全部为安排app问题。主要为数据报' \
         '表主播头像不显示、主播数据报表详情数据没有排序、数据报表详情没有展示主播"角色类型"'

day3 = '周三新增缺陷:'+str(new3) + '个，' + \
       '累计缺陷:' + str(bug3) + '个。' + \
       '已处理缺陷:'+str(fix3)+'个。剩余待处理缺陷:'\
       + str(bug3-fix3) + '个。' + '处理率:' + str(rate3) + '%。' + '\n' \
       + event3 + '\n'

new4 = 0
bug4 = bug3-fix3+new4
fix4 = 0
rate4 = round(fix4/bug4*100)
event4 = 'appBug还没有改好，主要是在写数据报表优化的sql，预计明天才可以提测'
day4 = '周四新增缺陷:'+str(new4) + '个，' + \
       '累计缺陷:' + str(bug4) + '个。' + \
       '已处理缺陷:'+str(fix4)+'个。剩余待处理缺陷:'\
       + str(bug4-fix4) + '个。' + '处理率:' + str(rate4) + '%。' + '\n' \
       + event4 + '\n'

new5 = 1
bug5 = bug3-fix3+new5
fix5 = 1
rate5 = round(fix5/bug5*100)
event5 = '流量池主播报表sql已经写好。目前客源隐私号已经可以提测（仅限web,app还没开始）,' \
         '除此以外排班管理、渠道配置也可以测了。其中，设备管理开始产品说可以测了，发现问题后' \
         '与开发沟通，开发表示还没有达到提测所以就先不看了。'
day5 = '周五新增缺陷:'+str(new5) + '个，' + \
       '累计缺陷:' + str(bug5) + '个。' + \
       '已处理缺陷:'+str(fix5)+'个。剩余待处理缺陷:'\
       + str(bug5-fix5) + '个。' + '处理率:' + str(rate5) + '%。' + '\n' \
       + event5 + '\n'


'''记录一周中需要报告的问题'''
event = '暂无'


nextPlan = '流量池v7测试'

bugs = new1+new2+new3+new4+new5  # 一周共计产生bug
fixes = fix1+fix2+fix3+fix4+fix5  # 一周共计处理bug
rate = round(fixes/bugs*100)

content = '本周还是继续上周的一个测试思路，继续测试' + title + '的相关内容。本周具体测试内容如下:' + \
          '\n' + '\n' + day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5 + '\n' + \
          '过程中遇到的问题:' + event + '\n'+ '\n' + '共计产生缺陷' + str(bugs) + '个,' + '共计处理' + str(fixes)+'个,' + \
          '剩余待处理缺陷' + str(bugs-fixes) + '个,' + '处理率：' + str(rate) + '%。'


f = open('C:/Users/Administrator/Desktop/周报.txt', 'w')
f.write(title + '\n' + '\n' + '\n' + content + '\n' + '\n' + '\n'+nextPlan)





