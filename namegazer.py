# coding:utf-8

import twitter as tw
import urllib
import time


namegazer_list = [
    u'popularimi'
]


old_name={
    u'popularimi':u''
}


now_name={
    u'popularimi':u''
}


def get_name(id):
    url = u'https://mobile.twitter.com/' + id
    resp = urllib.request.urlopen(url).read(1024) # 1024 is kimeuchi
    data = resp.decode()
    tpos = data.find(u'<title>')
    namebuf = data[(tpos + 7):(tpos + 100)]
    spcpos = namebuf.find(' ')
    return namebuf[0:spcpos]


for item in namegazer_list:
    while 1:
        try:
            old_name[item] = get_name(item)
        except:
            print(u'err1')
            continue
        break

while 1:
    for item in namegazer_list:
        try:
            now_name[item] = get_name(item)
        except:
            print(u'err1')
            continue

        if now_name[item] != old_name[item]:
            try:
                t = tw.Twitter(  auth=tw.OAuth(
                                    token=u'',
                                    token_secret=u'',
                                    consumer_key=u'',
                                    consumer_secret=u''))
            except:
                print('err2')
                continue
            try:
                t.statuses.update(status=u'Twitterアカウント「{a}」の名前は「{b}」に変わりました！'.format(a = old_name[item], b = now_name[item]))
            except:
                print('err3')
                continue
            old_name[item] = now_name[item]
        time.sleep(60)
