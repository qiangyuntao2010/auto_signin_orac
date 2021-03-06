#!/usr/bin/env python
# coding=utf-8
 
import requests
import sys
import webbrowser as web 
import time
import urllib3
from pymouse import PyMouse

urllib3.disable_warnings()

def login(type):
    """login work"""
    web.open_new_tab("http://gccaa.us.oracle.com/")
    time.sleep(4)
    '''
    headers =  {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate, br',
         'Accept-Language': 'en-US,en;q=0.5',
         'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"}
    s = requests.Session()
    s.headers = headers
    post_data = {'sso_username': '*', 'ssopassword': '*', 'iprange': type}
    r = s.post('https://login.oracle.com/', data=post_data, verify=False)
    print "log in, status = %s" % r.status_code
    '''
    m=PyMouse()
    m.position()
    x=737
    y=438
    m.move(x,y)
    m.click(x,y,1)
    
def logout(type):
    """logout work"""
    headers =  {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate, sdch, br',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    s = requests.Session()
    s.headers = headers
    post_data = {'username': 'username', 'password': 'password', 'iprange': 'no'}
    s.post('https://its.pku.edu.cn/cas/webLogin', data=post_data, verify=False)
    #to logout!!
    r = s.get('https://its.pku.edu.cn/netportal/ITSipgw?cmd=close&type=%s&sid=478' % type, verify=False, headers=headers)
    print "log out, status = %s" % r.status_code
 
 
if __name__ == '__main__':
    login('yes')
    '''
    if len(sys.argv) != 2:
        print "usage <option: 1 (connect free), 2 (connect global), 3 (disconnect this computer), 4 (disconnect all), 5(disconnect this computer and connect free)"
        exit(1)
 
    option = int(sys.argv[1])
    if option == 1:
        print "try to connect free"
        login('no')
    elif option == 2:
        print "try to connect global"
        login('yes')
    elif option == 3:
        print "try to disconnect self"
        logout('self')
    elif option == 4:
        print "try to disconnect all"
        logout('all')
    '''
