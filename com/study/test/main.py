# -*- coding: utf-8 -*-
import json
from pyicloud import PyiCloudService
import random
import os
import re
import time
from datetime import datetime


def get_info():
    data = {}
    senders = {}
    for files in os.walk('cities'):  # 当前目录路径root，当前路径下所有子目录dirs，当前路径下所有非目录子文件files
        for file in files[2]:

            # 根据日期筛选出当天的文件
            f_date = file[0:file.find('日') + 1].replace('年', '-').replace('月', '-').replace('日', '')
            file_date = datetime.strptime(f_date, '%Y-%m-%d').date()
            now_date = datetime.now().date()
            if file_date < now_date:
                continue

            # 将文件名称关键信息，转为发送信息
            city = file[file.find('日') + 1:file.find('【')]
            sender = file[file.find('【') + 1:file.find('】')]

            # 邮件数据清洗，并封装成待发送数据字典
            email_path = 'cities/{}'.format(file)
            res = open(email_path, 'r', encoding="utf-8")
            results = res.read().split()
            emails = []
            for r in results:
                if r == '':
                    continue
                try:
                    r = re.sub("\D", " ", r).strip()
                    email = r + '@qq.com'
                    emails.append(email)
                except:
                    continue
            data.update({city: emails})
            senders.update({city: sender})
            res.close()
    return senders, data


def check_key(obj, key):
    if key in obj.keys():
        return True
    return False


def get_account_log():
    """ 获取账号使用日志 """
    account_path = 'apple_accounts/accounts_checked_log.txt'
    # 验证文件是否存在
    if not os.path.exists(account_path):
        return {}
    results = open(account_path).read().split('\n')
    res = {}
    for r in results:
        if r == '':
            continue
        log = json.loads(r)
        if log['usage_time'] == time.strftime('%Y-%m-%d'):
            if check_key(res, log['email']):
                # 如果同一天同一个email有多个日志，去times最大的那一个
                cur_times = res[log['email']]['times']
                this_times = json.loads(r)['times']
                if this_times > cur_times:
                    res[log['email']] = json.loads(r)
            else:
                res[log['email']] = json.loads(r)
    return res


def write_account_log(result):
    """ 获取账号使用日志 """
    account_path = 'apple_accounts/accounts_checked_log.txt'
    file = open(account_path, "a+")
    file.write(str(result) + '\n')
    file.close()


def write_error_account(result):
    """ 账号登录失败使用日志 """
    account_path = 'apple_accounts/accounts_error_log.txt'
    file = open(account_path, "a+")
    file.write(str(result) + '\n')
    file.close()


def get_error_account():
    """ 获取无法登录的账号 """
    account_path = 'apple_accounts/accounts_error_log.txt'
    # 验证文件是否存在
    if not os.path.exists(account_path):
        return []
    results = open(account_path).read().split('\n')
    return results


def get_account_info():
    """ 获取账号信息"""
    account_path = 'apple_accounts/accounts.txt'
    results = open(account_path).read().split('\n')
    accounts = []
    for i in results:
        i = i.split('----')
        accounts.append((i[0], i[1], 0))
    return accounts


# 随机获得一个apple_cloud账号,并测试登陆，返回清洗可用的账号数据
def get_account(max_limit):
    accounts = get_account_info()
    account_logs = get_account_log()
    error_accounts = get_error_account()
    accounts_new = []
    for ac in accounts:
        if ac[0] in error_accounts:
            continue
        # 超过最大值进行过滤
        if check_key(account_logs, ac[0]):
            if account_logs[ac[0]]['times'] < max_limit:
                limit = account_logs[ac[0]]['times']
                accounts_new.append((ac[0], ac[1], limit))
            continue
        accounts_new.append(ac)
    return accounts_new


def get_title(sender):
    s0 = ['感受', '体验', '咨:询', '选…择', '静享', '享受', '为你定制', '', '', '', '', '']
    s1 = ['洗❤浴', '㊋桑❤拿', '休闲', '㊋养生', '㊋保=健', '水疗', '㊋SPA', 'spa', '泰国❤推油', '休=闲洗浴', '定制❤SPA', '男士休闲会馆',
          '水疗❥spa', '轻奢=养生馆', '休闲按❥摩', '足浴按❣摩', '水疗SPA', '日式指压按S❣PA', '韩式松骨按❣摩', '高端SPA', '高档SPA']
    s2 = ['╋扣', '=+q', '+Q', '╋抠', '+叩', '╋kou', '扣', '加=q', '加Q', '加抠', '加…叩', '加…kou']
    s3 = ['_', '·', '', '.', '', '']
    s4 = ['_', ';', ':', '·', '|', ' ']
    c = s0[random.randint(0, len(s0) - 1)]
    w = s1[random.randint(0, len(s1) - 1)]
    q = s2[random.randint(0, len(s2) - 1)]
    t = s3[random.randint(0, len(s3) - 1)]
    u = s4[random.randint(0, len(s4) - 1)]
    r = []
    for i in sender:
        r.append(i + t)
    title = c + w + q + u + ''.join(r)
    return title


def login(index, max_limit):
    """ 执行登陆"""
    accounts = get_account(max_limit)
    while True:
        if index > len(accounts) - 1:
            print('没有可用账号')
            return -1, None, 0
        email = accounts[index][0]
        pwd = accounts[index][1]
        try:
            service = PyiCloudService(email, pwd)
            print("{}新账号登陆成功~".format(accounts[index]))
            return index, service.reminders, accounts[index]
        except:
            print("{}登录失败,更换下一个~".format(accounts[index]))
            write_error_account(email)
            index += 1


def main(max_limit):
    senders, data = get_info()
    for c in senders.keys():
        sender = senders[c]
        i = 0
        # 所有email
        emails = data[c]
        # 登录状态
        reminders = None
        # 单个账号发送email的计数器
        send_counter = 0
        times = ()
        print("{} : {} emails need to be sent".format(c, len(emails)))
        while i < len(emails):

            # 第一次或者发送总数超过最高限额
            if reminders is None or send_counter > max_limit:
                account_index, reminders, times = login(0, max_limit)
                if account_index == -1:
                    break
                send_counter = times[2]

            n = random.randint(8, 15)
            send_mails = emails[i:i + n]
            i += len(send_mails)
            send_counter += len(send_mails)

            result = json.dumps(
                {'email': times[0], 'pwd': times[1], "usage_time": time.strftime('%Y-%m-%d'),
                 "times": send_counter})
            write_account_log(result)

            title = c + get_title(sender)
            description = '诚挚邀请！您的邀请序号【{}】'.format(random.randint(127, 998))

            # 创建主题post，并返回guid
            guid = reminders.postReminder(title=title, description=description)

            share = reminders.postShareEmail(guid=guid, emails=send_mails)
            print("Title{}".format(title))
            print('分享返回状态:', share, ':已经发送邮件: {}'.format(send_mails))

            time.sleep(random.randint(3, 5))
            de = reminders.deleteShareTitle(guid)
            print('删除返回状态:', de, ':已经删除提示 guid: {}'.format(guid))
            print("current email index:{}".format(i))


if __name__ == '__main__':
    main(250)

