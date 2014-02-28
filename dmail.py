#-*- coding:utf-8 -*-
#!/usr/bin/python
#coding=utf-8
'''####-*-encoding:utf-8-*-'''
#import email
import poplib
import cStringIO
import email
import email.Header
import base64,os
import time

def SaveAttach(mailhost,port,addr,_pass):
    os.chdir('d:/')
    #POP3取信
    M = poplib.POP3_SSL(mailhost,port)
    M.user(addr)
    M.pass_(_pass)

    today=time.strftime('%Y/%m/%d',time.localtime())
    sub="Fwd: %s - D10 - Daily Details Report & Statement" % (today)

    #打印有多少封信
    num = len(M.list()[1])
    print 'num of messages', num
    if num >= 6:
            num1 = 0#num-6
    else:
            num1 = 0

    #for i in range(numMessages):
    for i in range(num,num1,-1):  #从大到小，每次减1.
        #m = M.retr(i+1)
        m = M.retr(i)

        buf = cStringIO.StringIO()
        for j in m[1]:
            print >>buf, j
        buf.seek(0)
        #解析信件内容
        msg = email.message_from_file(buf)
        subject = msg.get("subject") # 取信件头里的subject,　也就是主题
        # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
        h = email.Header.Header(subject)
        dh = email.Header.decode_header(h)
        subject = dh[0][0]
        print "subject:", subject
        if subject == 'test':
            # 循环信件中的每一个mime的数据块
            for par in msg.walk():
                try:
                    contenttype = par.get_content_type() 
                    if not par.is_multipart(): # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
                        name = par.get_param("name") #如果是附件，这里就会取出附件的文件名
                        print name
                        if name:
                        #有附件
                        # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
                            h = email.Header.Header(name)
                            dh = email.Header.decode_header(h)
                            fname = dh[0][0]
                            print '附件名:', fname
                            data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中

                            try:
                                f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                            except:
                                print '附件名有非法字符，自动换一个'
                                f = open('aaaa', 'wb')
                            f.write(data)
                            f.close()
                        else:
                        #不是附件，是文本内容
                            print par.get_payload(decode=True) # 解码出文本内容，直接输出来就可以了。

                        print '+'*60 # 用来区别各个部分的输出
                except:
                    pass
        else:
            continue
    M.quit()
    print 'exit'

if __name__ == '__main__':  
    # SaveAttach("pop.126.com",995,"your_mail","your_pass")
    SaveAttach("pop.qq.com",995,"your_mail","your_pass")