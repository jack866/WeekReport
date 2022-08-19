# -*- coding: cp936 -*-
title = '流量池v8'

'''记录每天一天工作内容与总结'''
lastWeek = 0
new1 = 0
bug1 = new1 + lastWeek
fix1 = 0
# rate1 = round(fix1/bug1*100)
rate1 = 0
event1 = '1.参加管家组织架构需求会，理解组织架构的调整掉流量池的影响'+'\n' \
         '2.参加流量池v8的需求会，理解下版本的内容'

day1 = '周一新增缺陷:'+str(new1) + '个，' + \
       '上周遗留缺陷:'+str(lastWeek)+'个，' + \
       '累计缺陷:' + str(bug1) + '个。' + \
       '已处理缺陷:'+str(fix1)+'个。剩余待处理缺陷:'\
       + str(bug1-fix1) + '个。' + '处理率:' + str(rate1) + '%。' + '\n' \
       + event1 + '\n'

new2 = 0
bug2 = bug1-fix1+new2
fix2 = 0
# rate2 = round(fix2/bug2*100)
rate2 = 0
event2 = '主要将流量池经纪人报表sql补齐，当时的产品还没有建立流量池v8的sprint,原型也还没有权限看。'

day2 = '周二新增缺陷:'+str(new2) + '个，' + \
       '累计缺陷:' + str(bug2) + '个。' + \
       '已处理缺陷:'+str(fix2)+'个。剩余待处理缺陷:'\
       + str(bug2-fix2) + '个。' + '处理率:' + str(rate2) + '%。' + '\n' \
       + event2 + '\n'

new3 = 1
bug3 = bug2-fix2+new3
fix3 = 0
rate3 = round(fix3/bug3*100)
event3 = '1.写流量池新版本需求用例'+'\n' + \
         '2.测试2个流量池刚提测的任务，经纪人管理添加是否云店字段、客户详情优化'+'\n' + \
         '经纪人管理添加是否云店字段需求已完成。'
day3 = '周三新增缺陷:'+str(new3) + '个，' + \
       '累计缺陷:' + str(bug3) + '个。' + \
       '已处理缺陷:'+str(fix3)+'个。剩余待处理缺陷:'\
       + str(bug3-fix3) + '个。' + '处理率:' + str(rate3) + '%。' + '\n' \
       + event3 + '\n'

new4 = 1
bug4 = bug3-fix3+new4
fix4 = 0
rate4 = round(fix4/bug4*100)
event4 = '1.追踪处理一些昨天遗留的bug ' + '\n' + \
         '2.参加用例评审和开发交流下需要注意的问题' + '\n' + \
         '3.测试客户详情剩余的内容' + '\n' + \
         '客户详情优化已测试完但开发未处理Bug。'
day4 = '周四新增缺陷:'+str(new4) + '个，' + \
       '累计缺陷:' + str(bug4) + '个。' + \
       '已处理缺陷:'+str(fix4)+'个。剩余待处理缺陷:'\
       + str(bug4-fix4) + '个。' + '处理率:' + str(rate4) + '%。' + '\n' \
       + event4 + '\n'

new5 = 8
bug5 = bug3-fix3+new5
fix5 = 6
rate5 = round(fix5/bug5*100)
event5 = '1.追踪处理一些昨天遗留的bug ' + '\n' + \
         '2.测试手机号、账号双重登录、用户账户管理优化内容' + '\n' + \
         '3.测试分配经纪人列表优化' + '\n' + \
         '账号手机号双重登录、用户管理账号优化需求已完成' \

day5 = '周五新增缺陷:'+str(new5) + '个，' + \
       '累计缺陷:' + str(bug5) + '个。' + \
       '已处理缺陷:'+str(fix5)+'个。剩余待处理缺陷:'\
       + str(bug5-fix5) + '个。' + '处理率:' + str(rate5) + '%。' + '\n' \
       + event5 + '\n'


'''记录一周中需要报告的问题'''
event = '暂无'


nextPlan = '流量池v8'

bugs = new1+new2+new3+new4+new5  # 一周共计产生bug
fixes = fix1+fix2+fix3+fix4+fix5  # 一周共计处理bug
rate = round(fixes/bugs*100)

content = '本周主要测试' + title + '的相关内容。本周具体测试内容如下:' + \
          '\n' + '\n' + day1 + '\n' + day2 + '\n' + day3 + '\n' + day4 + '\n' + day5 + '\n' + \
          '过程中遇到的问题:' + event + '\n'+ '\n' + '共计产生缺陷' + str(bugs) + '个,' + '共计处理' + str(fixes)+'个,' + \
          '剩余待处理缺陷' + str(bugs-fixes) + '个,' + '处理率：' + str(rate) + '%。'


f = open('C:/Users/Administrator/Desktop/周报.txt', 'w')
f.write(title + '\n' + '\n' + '\n' + content + '\n' + '\n' + '\n'+nextPlan)





