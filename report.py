# -*- coding: cp936 -*-
title = '流量池v6'

'''记录每天一天工作内容与总结'''
new1 = 0
bug1 = new1
fix1 = 0
rate1 = round(fix1/bug1*100)
event1 = '准备流量池V7的用例，准备提测'
day1 = '周一新增缺陷:'+str(new1) + '个，' + \
       '累计缺陷:' + str(bug1) + '个。' + \
       '已处理缺陷:'+str(fix1)+'个。剩余待处理缺陷:'\
       + str(bug1-fix1) + '个。' + '处理率:' + str(rate1) + '%。' + '\n' \
       + event1 + '\n'

new2 = 0
bug2 = bug1-fix1+new2
fix2 = 0
rate2 = round(fix2/bug2*100)
event2 = '参加需求评审优化用例。JRZFB-6832-9999角色优化优化已提测，现根据需求字段写sql'
day2 = '周二新增缺陷:'+str(new2) + '个，' + \
       '累计缺陷:' + str(bug2) + '个。' + \
       '已处理缺陷:'+str(fix2)+'个。剩余待处理缺陷:'\
       + str(bug2-fix2) + '个。' + '处理率:' + str(rate2) + '%。' + '\n' \
       + event2 + '\n'

new3 = 13
bug3 = bug2-fix2+new3
fix3 = 20
rate3 = round(fix3/bug3*100)
event3 = '缺陷问题集中多为APP问题，APP统计直播时长统计维度不正确、app主播数据详情默认统计维度正确、' \
         'app客户申诉客源字段取错、客源带合同申诉流程逻辑不正确等'
day3 = '周三新增缺陷:'+str(new3) + '个，' + \
       '累计缺陷:' + str(bug3) + '个。' + \
       '已处理缺陷:'+str(fix3)+'个。剩余待处理缺陷:'\
       + str(bug3-fix3) + '个。' + '处理率:' + str(rate3) + '%。' + '\n' \
       + event3 + '\n'

new4 = 1
bug4 = bug3-fix3+new4
fix4 = 1
rate4 = round(fix4/bug4*100)
event4 = '缺陷问题集中为管家推送流量池消息，流量池没有收到'
day4 = '周四新增缺陷:'+str(new4) + '个，' + \
       '累计缺陷:' + str(bug4) + '个。' + \
       '已处理缺陷:'+str(fix4)+'个。剩余待处理缺陷:'\
       + str(bug4-fix4) + '个。' + '处理率:' + str(rate4) + '%。' + '\n' \
       + event4 + '\n'

new5 = 0
bug5 = bug3-fix3+new5
fix5 = 0
# rate5 = round(fix5/bug5*100)
event5 = '缺陷问题集中为客户二次业绩分成比例超过100未提示报错、管家财务不推流量池、组织架构多角色、离职展示问题、' \
         '流量池客户多角色客户业绩比例展示不正确等'
# day5 = '周五新增缺陷:'+str(new5) + '个，' + \
#        '累计缺陷:' + str(bug5) + '个。' + \
#        '已处理缺陷:'+str(fix5)+'个。剩余待处理缺陷:'\
#        + str(bug5-fix5) + '个。' + '处理率:' + str(rate5) + '%。' + '\n' \
#        + event5 + '\n'
day5 = ''

'''记录一周中需要报告的问题'''
event = '写目标管理的那个开发，完全不理解需求流程也开发过程中没有找产品沟通，以至于初测后需要完全重写。' \
        '当晚并没有主动留下加班，钉钉提醒后才姗姗来迟，捣鼓了一下总算是发布到uat了。幸亏是小功能，否则。。。' \


nextPlan = '流量池下期需求'

bugs = new1+new2+new3+new4+new5  # 一周共计产生bug
fixes = fix1+fix2+fix3+fix4+fix5  # 一周共计处理bug
rate = round(fixes/bugs*100)

content = '本周还是继续上周的一个测试思路，继续测试' + title + '的相关内容。本周具体测试内容如下:' + \
          '\n' + '\n' + day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5 + '\n' + \
          '过程中遇到的问题:' + event + '\n'+ '\n' + '共计产生缺陷' + str(bugs) + '个,' + '共计处理' + str(fixes)+'个,' + \
          '剩余待处理缺陷' + str(bugs-fixes) + '个,' + '处理率：' + str(rate) + '%。'


f = open('C:/Users/Administrator/Desktop/周报.txt', 'w')
f.write(title + '\n' + '\n' + '\n' + content + '\n' + '\n' + '\n'+nextPlan)





