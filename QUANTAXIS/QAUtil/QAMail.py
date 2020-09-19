# coding=utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2020 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def QA_util_send_mail(msg, title, from_user, from_password, to_addr, smtp):
    
    """
    explanation:
        邮件发送	

    params:
        * msg ->:
            meaning: 邮件内容
            type: str
            optional: [null]
        * title ->:
            meaning: 标题
            type: str
            optional: [null]
        * from_user ->:
            meaning: 来自用户
            type: str
            optional: [null]
        * from_password ->:
            meaning: 密码
            type: null
            optional: [null]
        * to_addr ->:
            meaning: 邮件发送地址
            type: null
            optional: [null]
        * smtp ->:
            meaning: smtp地址
            type: null
            optional: [null]

    return:
        None
	
    demonstrate:
        Not described
	
    output:
        Not described
    """
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8').encode()

    server = smtplib.SMTP(smtp, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_user, from_password)
    server.sendmail(from_user, [to_addr], msg.as_string())



